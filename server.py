# server.py

from actions import play_tone, stop_tone
from hardware_interface.pynq_gpio_setup import Buzzer  # Adjust the import based on your actual module structure

def main():
    # Access the buzzer module (adjust as needed based on your setup)
    buzzer = Buzzer()

    # Define a callback function for the button press action
    def button_callback():
        play_tone(buzzer)

    # Attach the callback function to the button press event
    detect_button_press(button_callback)

if __name__ == "__main__":
    main()