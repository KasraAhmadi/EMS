from subprocess import check_output
import subprocess
import os.path
import sys
import time


DicRep = {}
DicSignal = {}
SharedPrefPath = "/home/pi/Files/WifiFiles/wpa_suplicant.conf"
InsOne = "ip link set wlan0 up"
InsTwo = "iw dev wlan0 link"
PassOne = "--- :) Dungle is attached"
InsThree = "iw dev wlan0 scan | grep -e 'SSID\|signal' "
InsFour ="wpa_supplicant -B -D nl80211,wext -f /home/pi/Files/WifiFiles/WifiLog.log -i wlan0 -c /home/pi/Files/WifiFiles/wpa_suplicant.conf 2>/home/pi/Files/WifiFiles/Error.log 1>/home/pi/Files/WifiFiles/out.log "
InsSix = "dhcpcd"
kill = "killall wpa_supplicant"

def connect():
	subprocess.call(kill,shell=True)
	time.sleep(1)
	subprocess.call(InsFour,shell=True)
	time.sleep(5)

	#Check if a connection is stablished
	ResTwo = check_output(InsTwo,shell=True,universal_newlines=True)

	if(ResTwo == "Not connected.\n"):
		print("--- :( Wifi can not be connect \n maybe because of Wrong password ")
		subprocess.call(kill,shell=True)
		get = input("press 'y' to try again:\n")
		if(get == 'y'):
			search()
		else:
			subprocess.call(kill,shell=True)
			print("GoodBye")
			sys.exit()

	else:
		print("--- :) Wifi is connected")
		subprocess.call(InsSix,shell=True)
		sys.exit()

def Correct(string):
	if string.startswith(' '):
		string = string[1:]
	if string.endswith(' '):
		string = string[:-1]
	return string

def search():
	for i in range(8):
	#List all of SSIDs
		ResThree = check_output(InsThree,shell=True,universal_newlines=True)
		for ch in ['\t','\n',"dBm","signal:"]:
			if ch in ResThree:
				ResThree = ResThree.replace(ch,"")
		tmp = ResThree.split()
		tmp2=[]
	#Give the power of ssid
		for a in tmp:
			if a[0] == '-':
				m = float(a)
				if (m <= -100):
					q = 0
				elif (m >= -50):
					q = 100
				else:
					q = 2 * (m + 100)	
				tmp2.append(q)
				tmp.remove(a)
	
		i = 0	
		
		str1 = ' '.join(tmp)
		final = str1.split("SSID:")
		fin = []
		for a in final:
			if not a=='':
				fin.append(Correct(a))
		print("#######")
		print(fin)
		for a in fin :
			if(a in DicRep):
				num = DicRep[a] + 1
				DicRep[a] = num
			else:
				#print("kasra")
				DicRep[a] = 1
			DicSignal[a] = tmp2[i]
			i = i + 1
				
		#print(DicSignal)

	print("Final is:")
		
		#Show all final that are checked
	for a in DicRep:
		if (DicRep[a] >= 6 and DicSignal[a]>50):
			print(a)
		
	SSID = input("Please enter SSID:\n")
	Pass = input("Enter password:\n")
	subprocess.call("wpa_passphrase '"+SSID+"' "+ Pass + "> /home/pi/Files/WifiFiles/wpa_suplicant.conf",shell=True) 
	connect()

try:	
	
	#Check if Dungele is Pluged
	ResOne = check_output(InsOne,shell=True,universal_newlines=True)
	print(PassOne)
	
	#check SharedPrefernces
	file = open(SharedPrefPath,"r+")
	FileCheck = os.path.isfile(SharedPrefPath)

	if (FileCheck == True):
		connect()
	else :
		search()

		
except Exception as e:
	#print(e.output)
	#print("Error")
	print(e)
	
















