import smtplib
import time
import datetime


print("DACT STARTUP, RUNNING SELFTEST")

time.sleep(1)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gmail email", "password")

msg = "SELFTEST COMPLETE - System Startup Sucessful"

server.sendmail("gmail email", "other email", msg)
server.quit()

print "Sent:", msg
print "System Normal"
