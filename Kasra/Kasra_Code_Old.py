'''
Created on Jun 18, 2016
MAC Version
@author: kas
'''

import asyncio
import websockets
import socket
import logging
import datetime
import Message
import json
import threading
import time
import os.path
import Identity
import socket
import ColorSubmit
import sys
import subprocess

#color = ColorSubmit.ColorSubmit()
shared = None
DataReady = False
clientsocket = socket.socket()
ConnectionChek = 0
#logging.basicConfig(filename='Client.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)

ConnectionLost = 0
num = 0
ToAminSend= 0
DataToAmin = ""

connection = websockets
loop = asyncio.get_event_loop()
file = Identity.Identity()
print("Code is running")
def GetSerial():
    # Extract serial from cpuinfo file
    try:
        f = open('/proc/cpuinfo','r')
        msg = ""
        for line in f:
            if line[0:6]=='Serial':
                msg = line[10:26]
        f.close()
        return msg
    except:
        msg = "UnKnownId"
        return msg
def GetMac(interface):
	try:
		mac = open('/sys/class/net/'+interface+'/address').readline()
	except:
		logging.error(interface+" Mac address not find")
		mac = "Unknown"

	return mac[0:17]
def RunListenToElv():
	t2 = threading.Thread(target=ListenToElevator, args=()) 
	t2.start()
	while(1):
		t2.join()
		t2 = threading.Thread(target=ListenToElevator, args=())
		t2.start()
def ListenToElevator():
	global DataReady
	global shared
	global ToAminSend
	global DataToAmin
	try:
	# create a socket object
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		# get local machine name
		port = 60005                          
		# bind to the port
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
		serversocket.bind(("0.0.0.0", port))                                  
		serversocket.listen(1) 
		logging.info("Listen to Internal socket")                                       
		Client,addr = serversocket.accept()  
		clientsocket = Client
		clientsocket.setblocking(1)    
		clientsocket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
		logging.info("Got a connection from Internal socket")
		while True:
		# establish a connection
			msg = clientsocket.recv(90000)
			msg = msg.decode("ascii")
			shared = msg
			if(shared == ""):
				logging.error("Empty packet from Internal Socket")
				raise Exception
			else:
				if(ToAminSend == 1):
					send = DataToAmin.encode(encoding='UTF-8')
					#logging.info(send + " Send to Elv Board")
					clientsocket.send(send)
					ToAminSend = 0
					DataToAmin = ""
				DataReady = True
	except Exception as e:
		logging.error(e)
		serversocket.close()
async def FirstTimeInit():
	try:
		logging.info("Register Routine called")
		send = json.dumps({'T':"Register",'cpuId':GetSerial() ,'wifiMac':GetMac("wlan0") , 'ethMac':GetMac("eth0")})
		await connection.send(send)
	except Exception as e:
			logging.error(e)

async def Consumer(text):
	global ToAminSend
	global DataToAmin
	if(text == 'A'):
		return True
	JsonObj = json.loads(text)

	if(JsonObj['T'] == "Register"):
		file.ChangeSharedPref("Initial","True")
		file.ChangeSharedPref("Id",JsonObj['label'])
		logging.info("Registeriation Compeleted ")
		return True

	elif(JsonObj['T'] == "Greet"):
		msg = Message.Message(JsonObj['T'],0)
		return msg.getJson()

	elif(JsonObj['T'] == 'D'):
		msg = Message.Message(JsonObj['T'],JsonObj['D'])
		print (msg)
		ToAminSend = 1
		DataToAmin = JsonObj['D']
		return msg.getJson()
	else:
		msg = Message.Message(JsonObj['T'],JsonObj['D'])
		return msg.getJson()

async def CheckConnection():
	try:
		global ServerConnection
		await asyncio.sleep(5)
		while(1):
			#await asyncio.wait_for(connection.send("A"),timeout = 4)
			await connection.send("A")
			await asyncio.sleep(5)
	except Exception as e:
		logging.error(e)
async def ToServerSend():
	global num
	global DataReady
	global ConnectionLost
	prev_data = ["", "", "", "", "", "", "", ""]
	try:
		await asyncio.sleep(10)
		while(1):
			is_data_new = 0	
			if(DataReady):
				######### start filtering data ########
				#print(shared_str)
				shared_str = str(shared)  # cast shared to string
				shared_json_obj = json.loads(shared_str)  # cast shared to json
				try:
					elv_id = shared_json_obj['elevators'][0]['id']  #  get id tag
				except Exception as e:
					elv_id = 1
				# make sure that elv_id is 'int' not 'str' !!!
				if prev_data[elv_id] != str(shared):  # compare each elevator with it's own idww
					prev_data[elv_id] = str(shared)
					is_data_new = 1
				########  end filtering data #########
				if is_data_new:
					#print ("data sent to server from pi")
					#print (shared)
					await connection.send(shared)
					print("Done")
					now = datetime.datetime.now()
					#logging.info("Send to server: " + str(now))
				DataReady = False
			if(ConnectionLost == 1):
				raise Exception
			await asyncio.sleep(0.3)
	except Exception as e:
		logging.error(e)
async def Init_Recieve():
	try:
		global connection
		global check
		global DataReady
		global ConnectionLost
		async with websockets.connect('wss://emspaarcontrol.com/EMS/moduledatahandler') as t:
			logging.info("Connected to Server")
			#color.ChangeSharedPref("Server","True")
			ConnectionLost = 0
			connection = t
			init = file.read("Initial") #SharedPref
			if (init == "False"):
				await FirstTimeInit()
			elif(init == "True"):
				logging.info("Registeration has been compeleted before")
			while 1:
				greeting = await asyncio.wait_for(connection.recv(),timeout = 17)
				#greeting = await connection.recv()
				#logging.info("Got from server: " + greeting)
				answ = await Consumer(greeting)
				if(not answ == True):
					await connection.send(answ)
				await asyncio.sleep(2)          
	except Exception as e :
		logging.error(e)
		#color.ChangeSharedPref("Server","False")
		ConnectionLost = 1
		DataReady = 0 
def run_loop_forever_in_background(loop): 
	def thread_func(l):
		try:
			asyncio.set_event_loop(l)
			tasks = [asyncio.ensure_future(Init_Recieve()),  # @UndefinedVariable
			asyncio.ensure_future(ToServerSend()),
		 	asyncio.ensure_future(CheckConnection()),
		 	]  # @UndefinedVariable
			l.run_until_complete(asyncio.wait(tasks))
		except Exception as e:
			logging("Error in a Main")
	thread = threading.Thread(target=thread_func, args=(loop,)) 
	thread.start()
	return thread
	
b = run_loop_forever_in_background(loop)

t1 = threading.Thread(target=RunListenToElv, args=()) 
t1.start()
while(1):
	b.join()
	#subprocess.call("> /var/log/daemon.log",shell=True,stderr=subprocess.STDOUT)
	#subprocess.call("> /var/log/syslog",shell=True,stderr=subprocess.STDOUT)
	print("Cache has been cleared")
	time.sleep(5)
	b = run_loop_forever_in_background(loop)
