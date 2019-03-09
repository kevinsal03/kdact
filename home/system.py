import smtplib
import time
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
act = 1

GPIO.setup(17,GPIO.IN)


print("System Startup Successful")

time.sleep(1)
while act == 1 :
	if (GPIO.input(17)):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("gmail email", "gmail password")
		msg = "FIRE ALARM, Point=1, Label=Default Alarm Label"
		server.sendmail("GMAIL EMAIL", "OTHER EMAIL", msg)
		server.quit()
		print "Sent:", msg
		time.sleep(300)


