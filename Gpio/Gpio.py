import RPi.GPIO as GPIO
import time
 
pin = 21
iterations = 10
interval = .1
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
 
for x in range(1, iterations+1):
 
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)
 
    GPIO.output(pin, GPIO.LOW)
    time.sleep(interval)

