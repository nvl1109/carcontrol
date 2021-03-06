#/usr/bin/env python2.7

import RPi.GPIO as GPIO
from time import sleep

# Numbering by GPIO number, not header pin numberring
GPIO.setmode(GPIO.BCM)

# Use GPIO12 (PWM0) J8-32 to control speed of motor A
#	  GPIO13 (PWM1) J8-33 to control speed of motor B
# Use GPIO07 J8-26   |
#     GPIO08 J8-24  | to control direction of motor A
# Use GPIO25 J8-22  |
#     GPIO24 J8-18  | to control direction of motor B

# Config pins
# Motor A
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT, initial=0)
GPIO.setup(8, GPIO.OUT, initial=0)
motorA = GPIO.PWM(12, 1000)
# Motor B
GPIO.setup(13, GPIO.OUT)
GPIO.setup(25, GPIO.OUT, initial=0)
GPIO.setup(24, GPIO.OUT, initial=0)
motorB = GPIO.PWM(13, 1000)

# Motor A, fullspeed, back
motorA.start(100)
GPIO.output(7, 0)
GPIO.output(8, 1)
# Motor B, full speed, back
motorB.start(100)
GPIO.output(25, 0)
GPIO.output(24, 1)

sleep(1)
# Stop
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(25, 0)
GPIO.output(24, 0)
sleep(0.5)

# Motor A, fullspeed, front
motorA.ChangeDutyCycle(100)
GPIO.output(7, 1)
GPIO.output(8, 0)
# Motor B, full speed, front
motorB.ChangeDutyCycle(100)
GPIO.output(25, 1)
GPIO.output(24, 0)

sleep(1)

# Stop
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(25, 0)
GPIO.output(24, 0)
sleep(0.5)

# Motor A, fullspeed, front
motorA.ChangeDutyCycle(100)
GPIO.output(7, 1)
GPIO.output(8, 0)
# Motor B, full speed, back
motorB.ChangeDutyCycle(100)
GPIO.output(25, 0)
GPIO.output(24, 1)

sleep(1)

# Stop
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(25, 0)
GPIO.output(24, 0)
sleep(0.5)

# Motor A, fullspeed, back
motorA.ChangeDutyCycle(100)
GPIO.output(7, 0)
GPIO.output(8, 1)
# Motor B, full speed, front
motorB.ChangeDutyCycle(100)
GPIO.output(25, 1)
GPIO.output(24, 0)

sleep(1)



# Stop and clean
motorA.stop()
motorB.stop()
GPIO.cleanup()
