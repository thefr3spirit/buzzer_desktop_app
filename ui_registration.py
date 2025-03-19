# desktop_app/ui_registration.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit,
    QPushButton, QLabel, QGroupBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        
        # Header
        header = QLabel("National Petroleum Competition")
        header.setFont(QFont("Arial", 24))
        header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(header)
        
        # Horizontal layout for team registration forms
        teams_layout = QHBoxLayout()
        
        # --- Team 1 Registration ---
        team1_group = QGroupBox("Team 1 Registration")
        team1_group.setFont(QFont("Arial", 16))
        team1_layout = QFormLayout()
        
        # Team 1 Name
        self.team1_name = QLineEdit()
        self.team1_name.setPlaceholderText("Enter Team 1 Name")
        team1_layout.addRow("Team Name:", self.team1_name)
        
        # Team 1 Players (Buzzers 1-4)
        self.team1_players = []
        for i in range(1, 5):
            player_field = QLineEdit()
            player_field.setPlaceholderText(f"Player {i} Name (Buzzer {i})")
            self.team1_players.append(player_field)
            team1_layout.addRow(f"Buzzer {i}:", player_field)
            
        team1_group.setLayout(team1_layout)
        teams_layout.addWidget(team1_group)
        
        # --- Team 2 Registration ---
        team2_group = QGroupBox("Team 2 Registration")
        team2_group.setFont(QFont("Arial", 16))
        team2_layout = QFormLayout()
        
        # Team 2 Name
        self.team2_name = QLineEdit()
        self.team2_name.setPlaceholderText("Enter Team 2 Name")
        team2_layout.addRow("Team Name:", self.team2_name)
        
        # Team 2 Players (Buzzers 5-8)
        self.team2_players = []
        for i in range(5, 9):
            player_field = QLineEdit()
            player_field.setPlaceholderText(f"Player {i} Name (Buzzer {i})")
            self.team2_players.append(player_field)
            team2_layout.addRow(f"Buzzer {i}:", player_field)
            
        team2_group.setLayout(team2_layout)
        teams_layout.addWidget(team2_group)
        
        self.layout.addLayout(teams_layout)
        
        # Register Button
        self.register_button = QPushButton("Register")
        self.register_button.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.register_button)
        
        self.setLayout(self.layout)
    
    def get_registration_data(self):
        """
        Returns a dictionary with the registration data for each team.
        Example:
        {
            "team1": {
                "name": "Team A",
                "players": ["Alice", "Bob", "Charlie", "David"]
            },
            "team2": {
                "name": "Team B",
                "players": ["Eva", "Frank", "Grace", "Henry"]
            }
        }
        """
        data = {
            "team1": {
                "name": self.team1_name.text().strip() or "Team 1",
                "players": [
                    field.text().strip() or f"Player {i}"
                    for i, field in enumerate(self.team1_players, start=1)
                ]
            },
            "team2": {
                "name": self.team2_name.text().strip() or "Team 2",
                "players": [
                    field.text().strip() or f"Player {i}"
                    for i, field in zip(range(5, 9), self.team2_players)
                ]
            }
        }
        return data
