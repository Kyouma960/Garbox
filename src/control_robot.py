import RPi.GPIO as GPIO
import time
from utils import move_forward, move_backward, stop, pick_up_trash, drop_trash

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# Define motor and servo pins
MOTOR_LEFT_PIN = 17
MOTOR_RIGHT_PIN = 18
SERVO_PIN = 27

# Initialize the motors and servos
GPIO.setup(MOTOR_LEFT_PIN, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM for the servo
servo.start(0)

# Function to move the robot to the trash location
def go_to_trash():
    move_forward()
    time.sleep(2)  # Move for 2 seconds (adjust based on distance)
    stop()

# Function to deposit trash in the bin
def go_to_bin():
    move_backward()
    time.sleep(2)  # Move for 2 seconds to the bin
    stop()

try:
    while True:
        # Move to detected trash
        go_to_trash()
        
        # Pick up the trash
        pick_up_trash(servo)
        
        # Move to the bin and drop the trash
        go_to_bin()
        drop_trash(servo)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
