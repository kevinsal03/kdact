## Do not even bother reading this, it has too many issues
-------
KDACT
-------
KDACT is a basic 'DACT' that can send emails using a gmail account. This is ment to be a solution for
fire alarm collectors with their own system that they would like to monitor without having to pay for
expensive equipment.

THIS SOFTWARE COMES WITH NO WARRANTY!
This Software is (C) Kevin Salvatorelli (Kevinsal03/FireAlarmTech9) Some Rights Reserved
Feel free to look at the source, you may use it as you like as long as it is not being used to for actual
life saftey systems. Feel free to modify the code, but be sure to give credit to Kevin Salvatorelli.
This softare shal never be used in an actual life saftey system, DO NOT USE THIS TO PROTECT PROPERTY OR LIVES!
You shall NEVER distribute this software, without crediting the author, you may also NEVER sell this software!
Kevin Salvatorelli is not liable if this software fails to function or damage is caused by it!
Failure to comply with these terms will require you to stop using the software immediately.
These terms may be updated with or with no notification, you agree to the new terms by using the software.
The terms will be on my website or listed from where you got this download!



====================
HOW TO INSTALL
====================

Step 1.
Register a GMail account.
Step 2.
Enable "Less Secure Apps" in GMail @ https://www.google.com/settings/security/lesssecureapps
Step 3.
Add the account details into the 3 Python files where it is asked. WARINING: These files are
not encrypted! I would recomend creating a email account for this and this only!
Step 4.
Under the "OTHER EMAIL" spaces put the email you would like these messages to go to. What I
would recomend is to have it send to your phone.
In order to do this enter this email:
If you have Verizon: (phonenumberhere)@vtext.com
If you have AT&T: (phonenumberhere)@txt.att.net
If you have TMobile: (phonenumberhere)@tmomail.net
If you have Sprint: (phonenumberhere)@messaging@sprintpcs.com
DO NOT PUT DASHES or () IN THE NUMBER!
If you need to find the email for your carrier, search on Google, "(carriernamehere) email to text"
Using one of these emails will send you a text containing info about the dact!
Step 5.
Save the Python files!
Step 6.
Connect the Common connection on your fire alarm panel's ALARM relay to any ground PIN on the
RPI
Step 7.
Connect the Normally Closed connection of the FACP to GPIO pin 17 on the RPI. Use a pinout
diagram to see what pin is the right one.
Step 8.
Run the "Install.sh" that is included with these files by typing in the BASH Terminal "sudo sh Install.sh"
Step 9.
Let the installer finish, it will restart the RPI and this script will run when it gets back to the login
screen, you do not need to login! You should get an email/text from the Gmail you specified in the Python
files.

The DACT should now be up and running!

Need help or support? Tweet me @Kevinsal03 (https://twitter.com/kevinsal03)
