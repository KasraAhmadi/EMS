import time
import RPi.GPIO as GPIO
import socket
import ColorSubmit
import datetime
import subprocess

Attemp = 0

color = ColorSubmit.ColorSubmit()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#For Cathode Led the form is GRB 
RED = GPIO.PWM(11, 100)
BLUE = GPIO.PWM(13, 100)
GREEN = GPIO.PWM(15, 100)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

NoInt = [0,100,0]
NoServer = [100,100,0]
NoElv = [0,0,100]
AllFine = [100,0,0]


def CheckInternet(host="8.8.8.8",port=53,timeout=3):
	global Attemp
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect((host,port))
		Attemp = 0
		if(not color.read("Internet") == "True"):
			color.ChangeSharedPref("Internet","True")
	except Exception as e:
		Attemp = Attemp + 1
		if(not color.read("Internet") == "False"):
			color.ChangeSharedPref("Internet","False")
		
def setColor(rgb = []):
	RED.ChangeDutyCycle(rgb[0])
	GREEN.ChangeDutyCycle(rgb[1])
	BLUE.ChangeDutyCycle(rgb[2])

try:
	while 1:
		CheckInternet()
		print(Attemp)
		if(Attemp==5): 
			subprocess.call("ifdown eth0",shell=True,stderr=subprocess.STDOUT)
			subprocess.call("ifup eth0",shell=True,stderr=subprocess.STDOUT)
			subprocess.call("systemctl restart LtClient.service",shell=True,stderr=subprocess.STDOUT)
			Attemp = 0
		if( color.read("Internet") == "False" ):
			setColor(NoInt)
		#elif(color.read("Server") == "False"):
			#print("No Server")
			#setColor(NoServer)
		#elif(color.read("Physical") == "False"):
			#setColor(NoElv)
		else:	
			setColor(AllFine)
		time.sleep(120)

except Exception as e:
	print(e)

