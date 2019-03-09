import time
import base

print("SYSTEM CRASH ATTEMPTING RESTART")

time.sleep(1)

msg = "The DACT has crashed, the system will attempt to restart, if the problem contines check the manual."

base.send(msg)
