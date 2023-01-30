import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

servoPIN1 = 22
servoPIN2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

p = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
q = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5)
q.start(2.5)# Initialization
try:
  while True:
    p.ChangeDutyCycle(5)
    q.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    q.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    q.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    q.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    q.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    q.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    q.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    q.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  q.stop()

GPIO.cleanup()