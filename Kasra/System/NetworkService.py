from subprocess import check_output
import subprocess
import os.path
import sys
import RPi.GPIO as GPIO
import threading 
import time
import KeyLcd
import Wifi

Eth0 = "cat /sys/class/net/eth0/carrier"
Wlan0 = "cat /sys/class/net/wlan0/carrier"
while(1):
	try:
		ResEth = check_output(Eth0,shell=True,universal_newlines=True)
		ResWifi = check_output(Wlan0,shell=True,universal_newlines=True)
		if(ResEth == "0\n"):
			if(ResWifi == "0\n"):
				wifi = Wifi.Wifi()
				wifi.start()
				wifi.join()
			else:
				print("Wifi Connected")
		else:
			print("Lan Connected")
		time.sleep(5)
	except Exception as e:
		print(e)


