from machine import Pin
import utime
import gc
from config import BUZZER_PINS, BUZZER_TEAM_MAP, TEAM_SOUNDS

# List to store buzz events (buzzer_id and timestamp)
buzz_events = []
MAX_BUZZ_EVENTS = 10  # Limit to store only the most recent 10 events

# Dictionary to map Pin objects to buzzer IDs
pin_to_buzzer = {}

# Dictionary to track last pressed time (in milliseconds) for debounce
last_pressed_time = {}
DEBOUNCE_DELAY_MS = 300  # 300 milliseconds debounce delay

def buzzer_handler(pin):
    # Look up the buzzer ID from our dictionary
    buzzer_id = pin_to_buzzer.get(pin, None)
    if buzzer_id is None:
        print("Error: Unrecognized buzzer pressed!")
        return

    # Capture the current time in milliseconds
    current_time = utime.ticks_ms()

    # Debounce: ignore if pressed too soon after the last press
    if buzzer_id in last_pressed_time and (current_time - last_pressed_time[buzzer_id]) < DEBOUNCE_DELAY_MS:
        return  # Too soon, ignore this press

    last_pressed_time[buzzer_id] = current_time  # Update last press time

    team = BUZZER_TEAM_MAP.get(buzzer_id, "Unknown")
    message = f"Buzzer {buzzer_id} from Team {team} pressed at {current_time}"
    print(message)  # This output goes over USB serial

    # Limit the size of buzz_events list
    if len(buzz_events) >= MAX_BUZZ_EVENTS:
        buzz_events.pop(0)
    buzz_events.append((buzzer_id, current_time))
    
    # Trigger MP3 playback (placeholder)
    play_sound(TEAM_SOUNDS.get(team, ""))
    
    # Run garbage collection to free unused memory
    gc.collect()

def play_sound(sound_file):
    """Placeholder for triggering the MP3 module playback."""
    if sound_file:
        print("Playing sound:", sound_file)
    else:
        print("No sound file defined for this team.")

# Initialize buzzers and store mapping in pin_to_buzzer
buzzers = []
for buzzer_id, gpio_pin in BUZZER_PINS.items():
    buzzer = Pin(gpio_pin, Pin.IN, Pin.PULL_UP)
    pin_to_buzzer[buzzer] = buzzer_id  # Map this Pin object to its buzzer_id
    buzzer.irq(trigger=Pin.IRQ_FALLING, handler=buzzer_handler)
    buzzers.append(buzzer)

print("Buzzer system initialized. Waiting for buzzes...")

# Main loop keeps the program running
while True:
    utime.sleep_ms(100)
