#!/bin/bash

#DACT install Script


#BEFORE RUNNING THIS SCRIPT BE SURE TO HAVE FILLED OUT THE INFO IN THE PYTHON FILES!

echo SET VALUES IN THE PYTHON FILES FIRST!
sleep 2
echo SCRIPT MUST BE RUN AS ROOT THRU SUDO. THIS WILL BE PUT IN THE PI USERS HOME DIRECTORY, CHANGE THE SCRIPT TO CHANGE THE INSTALL LOCATION!
sleep 5
echo INSTALLING
sudo mkdir /DACTstartup
sudo cp root/system.startup /DACTstartup/system.startup
sleep 1
sudo mkdir /home/pi/DACTfiles
sleep 1
sudo cp home/system.py /home/pi/DACTfiles/
sleep 1
sudo cp home/crash.py /home/pi/DACTfiles/
sleep 1
sudo cp home/selftest.py /home/pi/DACTfiles/
sleep 1
echo Adding to crontab to run at startup, ^C to cancel
echo Waiting 5 seconds for input
sleep 5s
echo Installing into crontab
line="@reboot sudo sh /system.startup"
(crontab -u root -l; echo "$line" ) | crontab -u root - 
echo Restarting System ^C to cancel!
sleep 15
echo System Will Restart in approx 1 min!
#shutdown -r 
