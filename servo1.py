#SERVO MENARIK
#IMPOR LIBRARY GPIO
import RPi.GPIO as GPIO
#IMPORT WAKTU
import time
#PIN GPIO YANG DIPAKAI
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
for i in range(0,1):
	p.ChangeDutyCycle(5)
	time.sleep(0.2)
	p.ChangeDutyCycle(12.5)
	time.sleep(0.2)
	p.ChangeDutyCycle(5)
	time.sleep(0.2)
p.stop()
GPIO.cleanup()