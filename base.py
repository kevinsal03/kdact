import smtplib
import time
import datetime
import configparser

#Config file location: Change here if not in default location
configFileLocation = "config.ini"

#get config
config = configparser.ConfigParser()
config.read(configFileLocation)
configSection = "kdact" #most config options
configSection2 = "gpio" #gpio config

#variables gotten from config
user = config[configSection]['sender-email']
passw = config[configSection]['sender-pass']
recipient = config[configSection]['recipient']
smtp = config[configSection]['smtp-server'] #'smtp.gmail.com'
port = int(config[configSection]['smtp-port']) #587

#gpio definitons
alarmPin = int(config[configSection2]['alarm-pin']) #17

#Timestamp format declaration
dateString = '%Y-%m-%d %H:%M:%S'
cTime = datetime.datetime.now().strftime(dateString)


def updateTime(): #update the current time
    cTime = datetime.datetime.now().strftime(dateString)

def send(x):
    #x is message
    updateTime()
    finalMSG = "[" + cTime + "] " + x
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(user, passw)
    server.sendmail(user, recipient, finalMSG)
    server.quit()
    print "Sent: " + finalMSG
