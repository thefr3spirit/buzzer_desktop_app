# desktop_app/ui_game.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton,
    QHBoxLayout, QGroupBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GamePage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        
        # Header
        header = QLabel("National Petroleum Competition")
        header.setFont(QFont("Arial", 24))
        header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(header)
        
        # Buzz Order Display
        buzz_group = QGroupBox("Buzz Order")
        buzz_layout = QVBoxLayout()
        self.buzz_list = QListWidget()
        self.buzz_list.setFont(QFont("Arial", 16))
        buzz_layout.addWidget(self.buzz_list)
        self.reset_button = QPushButton("Reset")
        self.reset_button.setFont(QFont("Arial", 14))
        buzz_layout.addWidget(self.reset_button)
        buzz_group.setLayout(buzz_layout)
        self.layout.addWidget(buzz_group)
        
        # Team Scores Section
        scores_layout = QHBoxLayout()
        
        # --- Team 1 Score ---
        team1_layout = QVBoxLayout()
        self.team1_label = QLabel("Team 1")
        self.team1_label.setFont(QFont("Arial", 20))
        self.team1_label.setAlignment(Qt.AlignCenter)
        team1_layout.addWidget(self.team1_label)
        self.team1_score = QLabel("00")
        self.team1_score.setFont(QFont("Arial", 36))
        self.team1_score.setAlignment(Qt.AlignCenter)
        team1_layout.addWidget(self.team1_score)
        team1_buttons_layout = QHBoxLayout()
        self.team1_right = QPushButton("Right")
        self.team1_right.setFont(QFont("Arial", 14))
        self.team1_wrong = QPushButton("Wrong")
        self.team1_wrong.setFont(QFont("Arial", 14))
        team1_buttons_layout.addWidget(self.team1_right)
        team1_buttons_layout.addWidget(self.team1_wrong)
        team1_layout.addLayout(team1_buttons_layout)
        scores_layout.addLayout(team1_layout)
        
        # --- Team 2 Score ---
        team2_layout = QVBoxLayout()
        self.team2_label = QLabel("Team 2")
        self.team2_label.setFont(QFont("Arial", 20))
        self.team2_label.setAlignment(Qt.AlignCenter)
        team2_layout.addWidget(self.team2_label)
        self.team2_score = QLabel("00")
        self.team2_score.setFont(QFont("Arial", 36))
        self.team2_score.setAlignment(Qt.AlignCenter)
        team2_layout.addWidget(self.team2_score)
        team2_buttons_layout = QHBoxLayout()
        self.team2_right = QPushButton("Right")
        self.team2_right.setFont(QFont("Arial", 14))
        self.team2_wrong = QPushButton("Wrong")
        self.team2_wrong.setFont(QFont("Arial", 14))
        team2_buttons_layout.addWidget(self.team2_right)
        team2_buttons_layout.addWidget(self.team2_wrong)
        team2_layout.addLayout(team2_buttons_layout)
        scores_layout.addLayout(team2_layout)
        
        self.layout.addLayout(scores_layout)
        self.setLayout(self.layout)
    
    def update_score_display(self, team_scores):
        """Update the score display with the current scores.
           team_scores is a dict with keys 1 and 2.
        """
        self.team1_score.setText(f"{team_scores.get(1, 0):02d}")
        self.team2_score.setText(f"{team_scores.get(2, 0):02d}")
        
    def add_buzz_event(self, message):
        """Add a buzz event message to the buzz list."""
        self.buzz_list.addItem(message)
