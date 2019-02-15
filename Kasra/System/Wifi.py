from subprocess import check_output
import subprocess
import os.path
import sys
import RPi.GPIO as GPIO
import threading 
import time
import KeyLcd


class Wifi(threading.Thread):

	WifiSSIDs = []
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
	keylcd = KeyLcd.KeyLcd()

	def connect(self):
		try:
			subprocess.call(self.kill,shell=True)
			time.sleep(1)
			subprocess.call(self.InsFour,shell=True)
			time.sleep(5)
			
			#Check if a connection is stablished
			ResTwo = check_output(self.InsTwo,shell=True,universal_newlines=True)
			print(ResTwo)
			if(ResTwo == "Not connected.\n"):
				subprocess.call(self.kill,shell=True)
				self.keylcd.clearLcd()
				get = self.keylcd.input(":( Not connectedPress 'y' to try again: ")
				if(get == 'y'):
					self.keylcd.clearLcd()
					self.keylcd.My_string("Searching...")
					self.search()
				else:
					subprocess.call(self.kill,shell=True)
					get = self.keylcd.input("Error")
					print("GoodBye")
					return
			else:
				self.keylcd.clearLcd()
				self.keylcd.My_string(":) Wifi is      connected")
				time.sleep(0.5)
				subprocess.call(self.InsSix,shell=True)
				return
		except Exception as e:
			self.keylcd.clearLcd()
			self.keylcd.My_string("Error in connecting")

	def Correct(self,string):
		if string.startswith(' '):
			string = string[1:]
		if string.endswith(' '):
			string = string[:-1]
		return string

	def search(self):
		for i in range(8):
		#List all of SSIDs
			ResThree = check_output(self.InsThree,shell=True,universal_newlines=True)
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
					fin.append(self.Correct(a))
			print("#######")
			print(fin)
			for a in fin :
				if(a in self.DicRep):
					num = self.DicRep[a] + 1
					self.DicRep[a] = num
				else:
					self.DicRep[a] = 1
				self.DicSignal[a] = tmp2[i]
				i = i + 1
					
		self.keylcd.clearLcd()
		self.keylcd.My_string("select number:  ")
			
			#Show all final that are checked
		i = 0
		self.WifiSSIDs = []
		for a in self.DicRep:
			if (self.DicRep[a] >= 6 and self.DicSignal[a]>50):
				i = i + 1
				self.WifiSSIDs.append(a)
				self.keylcd.My_string(str(i) + ")" +a + " ")
				print(a)
		
		print(len(self.WifiSSIDs))
		NumSSID = self.keylcd.input("")
		SSID = self.WifiSSIDs[int(NumSSID) - 1]
		self.keylcd.clearLcd()
		Pass = self.keylcd.input(SSID + " selected. Please Enter password: ")
		self.keylcd.clearLcd()
		self.keylcd.My_string("Connecting...")
		subprocess.call("wpa_passphrase '"+SSID+"' "+ Pass + "> /home/pi/Files/WifiFiles/wpa_suplicant.conf",shell=True) 
		self.connect()
		self.WifiSSIDs = []
	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		#Check if Dungele is Pluged
		self.keylcd.clearLcd()
		ResOne = check_output(self.InsOne,shell=True,universal_newlines=True)
		print(self.PassOne)
		
		#check SharedPrefernces
		file = open(self.SharedPrefPath,"r+")
		FileCheck = os.path.isfile(self.SharedPrefPath)

		if (FileCheck == True):
			self.connect()
		else :
			self.search()
