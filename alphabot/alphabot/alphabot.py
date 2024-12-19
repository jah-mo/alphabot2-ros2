#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

class Alphabot():
    def __init__(self):
        # Motors
        self.MOTOR_A            = 6
        self.MOTOR_A_FORWARD    = 13
        self.MOTOR_A_REVERSE    = 12
        
        self.MOTOR_B            = 26
        self.MOTOR_B_FORWARD    = 21
        self.MOTOR_B_REVERSE    = 20

        # Front Sensors
        self.IR_SENSOR_LEFT     = 19
        self.IR_SENSOR_RIGHT    = 16

        # Button
        self.BUTTON             = 7

        # Buzzer
        self.BUZZER             = 4

        # Setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)


    # Motor functions ----------------------------------------------------

    def init_motors(self):
        # Initialize motor A
        GPIO.setup(self.MOTOR_A, GPIO.OUT)
        GPIO.setup(self.MOTOR_A_FORWARD, GPIO.OUT)
        GPIO.setup(self.MOTOR_A_REVERSE, GPIO.OUT)
        self.MOTOR_A_PWM = GPIO.PWM(self.MOTOR_A, 500)

        # Initialize motor B
        GPIO.setup(self.MOTOR_B, GPIO.OUT)
        GPIO.setup(self.MOTOR_B_FORWARD, GPIO.OUT)
        GPIO.setup(self.MOTOR_B_REVERSE, GPIO.OUT)
        self.MOTOR_B_PWM = GPIO.PWM(self.MOTOR_B, 500)

        # Start motors
        self.MOTOR_A_PWM.start(0)
        self.MOTOR_B_PWM.start(0)

    def move_forward(self, power):
        # Change motor power
        self.MOTOR_A_PWM.ChangeDutyCycle(power)
        self.MOTOR_B_PWM.ChangeDutyCycle(power)

        # Change motor direction
        GPIO.output(self.MOTOR_A_FORWARD, GPIO.HIGH)
        GPIO.output(self.MOTOR_A_REVERSE, GPIO.LOW)
        GPIO.output(self.MOTOR_B_FORWARD, GPIO.HIGH)
        GPIO.output(self.MOTOR_B_REVERSE, GPIO.LOW)

    def move_backward(self, power):
        # Change motor power
        self.MOTOR_A_PWM.ChangeDutyCycle(power)
        self.MOTOR_B_PWM.ChangeDutyCycle(power)

        # Change motor direction
        GPIO.output(self.MOTOR_A_FORWARD, GPIO.LOW)
        GPIO.output(self.MOTOR_A_REVERSE, GPIO.HIGH)
        GPIO.output(self.MOTOR_B_FORWARD, GPIO.LOW)
        GPIO.output(self.MOTOR_B_REVERSE, GPIO.HIGH)

    def turn_left(self, power):
        # Change motor power
        self.MOTOR_A_PWM.ChangeDutyCycle(power)
        self.MOTOR_B_PWM.ChangeDutyCycle(power)

        # Change motor direction
        GPIO.output(self.MOTOR_A_FORWARD, GPIO.LOW)
        GPIO.output(self.MOTOR_A_REVERSE, GPIO.HIGH)
        GPIO.output(self.MOTOR_B_FORWARD, GPIO.HIGH)
        GPIO.output(self.MOTOR_B_REVERSE, GPIO.LOW)

    def turn_right(self, power):
        # Change motor power
        self.MOTOR_A_PWM.ChangeDutyCycle(power)
        self.MOTOR_B_PWM.ChangeDutyCycle(power)

        # Change motor direction
        GPIO.output(self.MOTOR_A_FORWARD, GPIO.HIGH)
        GPIO.output(self.MOTOR_A_REVERSE, GPIO.LOW)
        GPIO.output(self.MOTOR_B_FORWARD, GPIO.LOW)
        GPIO.output(self.MOTOR_B_REVERSE, GPIO.HIGH)

    def stop(self):
        # Change motor power
        self.MOTOR_A_PWM.ChangeDutyCycle(0)
        self.MOTOR_B_PWM.ChangeDutyCycle(0)

        # Change motor direction
        GPIO.output(self.MOTOR_A_FORWARD, GPIO.LOW)
        GPIO.output(self.MOTOR_A_REVERSE, GPIO.LOW)
        GPIO.output(self.MOTOR_B_FORWARD, GPIO.LOW)
        GPIO.output(self.MOTOR_B_REVERSE, GPIO.LOW)


    # IR Sensor functions ------------------------------------------------

    def init_ir_sensors(self):
        GPIO.setup(self.IR_SENSOR_LEFT, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.IR_SENSOR_RIGHT, GPIO.IN, GPIO.PUD_UP)

    def get_ir_sensors_status(self) -> bool:
        # Check if a sensor detects an obstacle
        return GPIO.input(self.IR_SENSOR_LEFT) == 0 or GPIO.input(self.IR_SENSOR_RIGHT) == 0
    

    # Button functions ---------------------------------------------------

    def init_button(self):
        GPIO.setup(self.BUTTON, GPIO.IN, GPIO.PUD_UP)

    def get_button_status(self) -> bool:
        return GPIO.input(self.BUTTON) == 0
    

    # Buzzer functions ---------------------------------------------------

    def init_buzzer(self):
        GPIO.setup(self.BUZZER, GPIO.OUT)

    def beep(self):
        GPIO.output(self.BUZZER, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.BUZZER, GPIO.LOW)