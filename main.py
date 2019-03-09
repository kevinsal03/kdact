import base
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
active = 1

GPIO.setup(alarmPin,GPIO.IN)

def waitForClear():
    while GPIO.input(alarmPin):
        print "Still In Alarm"
        time.sleep(30)

print("System Startup Successful")

time.sleep(1)
while active == 1 :
	if (GPIO.input(alarmPin)):
		msg = "FIRE ALARM ACTIVATED"
        base.send(msg)
		waitForClear()
    time.sleep(5)
