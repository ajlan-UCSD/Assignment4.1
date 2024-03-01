# pynq_gpio_setup.py

# ... (Previous code)

def detect_button_press(button, action_callback):
    while True:
        if button.read():
            action_callback()  # Execute the specified action
            time.sleep(0.2)  # Add a small delay to debounce the button
        time.sleep(0.01)

# ... (Rest of the code)