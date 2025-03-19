import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_registration import RegistrationPage
from ui_game import GamePage
from serial_thread import SerialThread  # our QThread subclass for serial reading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buzzer System")
        self.setMinimumSize(800, 600)  # Ensure window is big enough
        
        # Data storage for registration and scores
        self.registration_data = {}  # holds team registration details
        self.team_scores = {1: 0, 2: 0}
        
        # Initialize pages
        self.registration_page = RegistrationPage()
        self.game_page = GamePage()
        
        # Set the registration page as the starting central widget
        self.setCentralWidget(self.registration_page)
        print("Registration page is now visible.")
        
        # Connect registration button to complete registration
        self.registration_page.register_button.clicked.connect(self.complete_registration)
        
        # Connect reset button to clear buzz order list on game page
        self.game_page.reset_button.clicked.connect(self.reset_buzz_order)
        
        # Connect score buttons for each team on game page
        self.game_page.team1_right.clicked.connect(self.handle_team1_right)
        self.game_page.team1_wrong.clicked.connect(self.handle_team1_wrong)
        self.game_page.team2_right.clicked.connect(self.handle_team2_right)
        self.game_page.team2_wrong.clicked.connect(self.handle_team2_wrong)
        
        # Set up and start the serial thread (update 'COM6' with your Pico's port)
        self.serial_thread = SerialThread(port='COM6', baudrate=115200)
        self.serial_thread.buzzReceived.connect(self.update_buzz_list)
        self.serial_thread.start()
    
    def complete_registration(self):
        # Retrieve registration data and update team labels
        self.registration_data = self.registration_page.get_registration_data()
        print("Registration Data:", self.registration_data)
        self.game_page.team1_label.setText(self.registration_data["team1"]["name"])
        self.game_page.team2_label.setText(self.registration_data["team2"]["name"])
        # Switch to game page
        self.setCentralWidget(self.game_page)
    
    def handle_team1_right(self):
        self.team_scores[1] += 10
        self.game_page.update_score_display(self.team_scores)
    
    def handle_team1_wrong(self):
        self.team_scores[1] -= 5
        self.game_page.update_score_display(self.team_scores)
    
    def handle_team2_right(self):
        self.team_scores[2] += 10
        self.game_page.update_score_display(self.team_scores)
    
    def handle_team2_wrong(self):
        self.team_scores[2] -= 5
        self.game_page.update_score_display(self.team_scores)
    
    def update_buzz_list(self, message):
        # Debug print to verify incoming message
        print("UI Update with:", message)
        # Filter out any unwanted messages if needed
        if message.startswith("Playing sound"):
            return
        
        # Process the message to display registered player/team names
        try:
            words = message.split()
            buzzer_id = int(words[1])
            team_from_message = int(words[4])
            
            # Determine team key and player index based on buzzer id.
            if 1 <= buzzer_id <= 4:
                team_key = "team1"
                player_index = buzzer_id - 1
            elif 5 <= buzzer_id <= 8:
                team_key = "team2"
                player_index = buzzer_id - 5
            else:
                return
            
            # Use registration data if available; else default values.
            if self.registration_data:
                team_data = self.registration_data.get(team_key, {})
                team_name = team_data.get("name", team_key)
                players = team_data.get("players", [])
                if player_index < len(players):
                    player_name = players[player_index]
                else:
                    player_name = f"Player {buzzer_id}"
            else:
                player_name = f"Player {buzzer_id}"
                team_name = f"Team {team_from_message}"
            
            # Create the display message
            display_message = f"{player_name} from {team_name}"
            self.game_page.add_buzz_event(display_message)
        except Exception as e:
            print("Error processing message:", e)
    
    def reset_buzz_order(self):
        self.game_page.buzz_list.clear()
    
    def closeEvent(self, event):
        # Stop the serial thread when closing the app
        if hasattr(self, 'serial_thread'):
            self.serial_thread.stop()
            self.serial_thread.wait()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
