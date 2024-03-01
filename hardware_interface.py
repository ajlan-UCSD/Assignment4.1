# hardware_interface.py

import time

class MotorController:
    def __init__(self, enable_pin, input1_pin, input2_pin):
        self.enable_pin = enable_pin
        self.input1_pin = input1_pin
        self.input2_pin = input2_pin
        # Initialize GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.input1_pin, GPIO.OUT)
        GPIO.setup(self.input2_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.enable_pin, 1000)
        self.pwm.start(0)

    def set_speed(self, speed):
        if speed > 0:
            GPIO.output(self.input1_pin, GPIO.HIGH)
            GPIO.output(self.input2_pin, GPIO.LOW)
        elif speed < 0:
            GPIO.output(self.input1_pin, GPIO.LOW)
            GPIO.output(self.input2_pin, GPIO.HIGH)
        else:
            GPIO.output(self.input1_pin, GPIO.LOW)
            GPIO.output(self.input2_pin, GPIO.LOW)
        self.pwm.ChangeDutyCycle(abs(speed))

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup()

class Buzzer:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def buzz(self, frequency, duration):
        p = GPIO.PWM(self.pin, frequency)
        p.start(50)
        time.sleep(duration)
        p.stop()

    def play_tone(self, tone, duration):
        # Define tones
        NOTES = {'C':261, 'D':294, 'E':329, 'F':349, 'G':392, 'A':440, 'B':493}
        frequency = NOTES.get(tone.upper(), 0)
        if frequency == 0:
            print("Invalid note")
            return
        self.buzz(frequency, duration)

    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()

# Additional classes or functions can be added here based on your project requirements
