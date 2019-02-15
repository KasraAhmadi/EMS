
import subprocess
import os
import time

path = "/home/pi/Files/IP.txt"
UP = "ip link set eth0 up"
REMOVE = "ip addr flush dev eth0"

def read(subject):

	file = open(path,"r")
	data = file.readlines()
	for line in data:
		sec = line.split(":")
		if(sec[0] == subject):
			file.close()
			out = sec[1].replace('\n',"")
			return out
	return "Subject not found"


try:
	time.sleep(5)
	Ip = read("Ip")
	BroadCast = read("Broadcast")
	Router = read("Router")
	PhaseOne = "ip addr add " + str(Ip) + " broadcast " + str(BroadCast) + " dev eth0"
	PhaseTwo = "ip route add default via " + str(Router)
	
	print(PhaseOne)
	print(PhaseTwo)
	subprocess.call(UP,shell=True)
	subprocess.call(REMOVE,shell=True)
	subprocess.call(PhaseOne,shell=True)
	subprocess.call(PhaseTwo,shell=True)

except Exception as e:
	print(e)







