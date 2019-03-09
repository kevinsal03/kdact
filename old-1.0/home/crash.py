import smtplib
import time
import datetime

dateString = '%Y%m%d %H%M%S'

print("SYSTEM CRASH ATTEMPTING RESTART")

time.sleep(1)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("GMAIL EMAIL", "GMAIL PASWORD")

msg = "The DACT has crashed, the system will attempt to restart, if the problem contines check the manual."

server.sendmail("GMAIL EMAIL", "OTHER EMAIL", msg)
server.quit()

print "Sent:", msg
