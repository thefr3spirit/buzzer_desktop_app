# pico_code/config.py

# Define GPIO pin mapping for each buzzer.
# Adjust the pin numbers according to your Pico wiring.
BUZZER_PINS = {
    1: 14,  # Buzzer 1 on GP14
    2: 13,  # Buzzer 2 on GP13
    3: 12,	#Buzzer 3 on GP12
    4: 11, #Buzzer 4 on GP11
   
    5: 19,  # Buzzer 5 on GP19
    6: 20, #Buzzer 6 on GP20
    7: 21, #Buzzer 7 on GP21
    8: 22, #Buzzer 8 on GP22
   
}

# Map each buzzer to a team.
# Buzzers 1-4 belong to Team 1, and buzzers 5-8 to Team 2.
BUZZER_TEAM_MAP = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    
    5: 2,
    6: 2,
    7: 2,
    8: 2
}

# Mapping of team to their sound file.
TEAM_SOUNDS = {
    1: "team1.mp3",
    2: "team2.mp3"
}

