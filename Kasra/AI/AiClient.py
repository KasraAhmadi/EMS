from socketIO_client_nexus import SocketIO, LoggingNamespace
import time
from threading import Thread
import socket
import queue as queue
import datetime
import os
import json
import Identity
import sqlite3
import subprocess
import logging
import sys




BUF_SIZE = 100
q = queue.Queue(BUF_SIZE)
dbconnect = None
Simulation = False

logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logging.info("AiClient started")

class resourceMonitor(Thread):

	def ssh(self,*args):
		Command = "sshpass -p  HammerOn070oahdhvHvdkliv4731 ssh -t -t -R 32320:localhost:22 -o StrictHostKeyChecking=no root@emspaarcontrol.com &"
		logging.info("ssh called")
		subprocess.call(Command,shell=True,stderr=subprocess.STDOUT)

	def kill_ssh(self,*args):
		Command = "killall ssh"
		subprocess.call(Command,shell=True,stderr=subprocess.STDOUT)

	def reboot(self,*args):
		Command = "reboot"
		subprocess.call(Command,shell=True,stderr=subprocess.STDOUT)

	def Alive(self,*args):
		self.SickSocket.send("Alive".encode('ascii'))




	def __init__(self):
		self.id = 0
		Thread.__init__(self)

	def run(self):
		try:
			self.SickSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.SickSocket.connect((socket.gethostname(),60008))
			self.socket = SocketIO("31.184.135.192", 80)
			print("SocketIO connection established")
			self.socket.on('ssh', self.ssh)
			self.socket.on('Alive', self.Alive)
			self.socket.on('kill_ssh', self.kill_ssh)
			self.socket.on('reboot', self.reboot)

			if Simulation == False:
				file = Identity.Identity()
				init = file.read("Initial")
				if(init == "True"):
					self.id = file.read("Id")
			reg_data = {"moduleId":self.id}
			self.socket.emit("Register",reg_data)

			while True:
				self.socket.wait(2)
				if not q.empty():
					data = q.get()
					self.socket.emit("data",data)

		except Exception as e:
			print(e)


class AIListener(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.id = 0
		if Simulation == False:
			file = Identity.Identity()
			init = file.read("Initial")
			if(init == "True"):
				self.id = file.read("Id")
		self.port = 60007
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serversocket.bind(("0.0.0.0", self.port))
		self.serversocket.listen(1)


	def checkValidity(self,jData):
		try:
			if len(jData['elevators'][0]['in call']) != 0:
				return True
			if len(jData['elevators'][0]['out call up']) != 0:
				return True
			if len(jData['elevators'][0]['out call down']) != 0:
				return True
			return False
		except Exception as e:
			print(e)


	def cleanData(self,data):

		msg_str = str(data.decode("ascii"))  # cast shared to string
		json_input = json.loads(msg_str)
		if(self.checkValidity(json_input)):
			try:
				out_data = {}
				out_data['data'] = {}
				now = datetime.datetime.now()
				time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)
				out_data['module_id'] = self.id
				out_data['data']['direction'] = json_input['elevators'][0]['direction']
				out_data['data']['time'] = time_now
				out_data['data']['in_call'] = json_input['elevators'][0]['in call']
				out_data['data']['out_call_up'] = json_input['elevators'][0]['out call up']
				out_data['data']['out_call_down'] = json_input['elevators'][0]['out call down']
				out_data['data']['numerator'] = json_input['elevators'][0]['numerator']
				out_data['data']['lift_status'] = json_input['elevators'][0]['lift status']
				out_data['data']['elv_id'] = json_input['elevators'][0]['id']


				json_data = json.dumps(out_data)
			except Exception as e:
				print(e)
			return json_data
		else:
			return "None"



	def connect_to_db(self):
		global dbconnect
		try:
			if Simulation:
				dbconnect = sqlite3.connect("/Users/Kas/Documents/GitHub/EMS/Elv.db");
			else:
				dbconnect = sqlite3.connect("/media/usbsda1/Elv.db");
			dbconnect.row_factory = sqlite3.Row
		except Exception as e:
			print(e)


	def write_to_db(self,msg):
		global dbconnect
		if dbconnect != None:
			myData = json.loads(msg)
			try:
				cursor = dbconnect.cursor()
				product_sql = "INSERT INTO Data VALUES (?,?,?,?,?,?,?,?)"
				val = (str(myData['data']['in_call']),str(myData['data']['out_call_up']),str(myData['data']['out_call_down']),
							myData['data']['elv_id'],str(myData['data']['time']),myData['data']['direction'],
							myData['data']['numerator'],myData['data']['lift_status'])

				cursor.execute(product_sql,val)
				dbconnect.commit()
			except Exception as e:
				print(e)
		else:
			print("DbConnect is None")

	def run(self):
		try:
			self.connect_to_db()
			Client,addr = self.serversocket.accept()
			self.clientsocket = Client
			self.clientsocket.setblocking(1)
			self.clientsocket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
			while True:
				msg = self.clientsocket.recv(90000)
				if(msg == ""):
					pass
				else:
					myOut = self.cleanData(msg)
					if(myOut != "None"):
						self.write_to_db(myOut)
						if not q.full():
							q.put(myOut)
		except Exception as e:
			print(e)
			self.serversocket.close()


AIMonitor = AIListener()
socketIOMonitor = resourceMonitor()
socketIOMonitor.start()
AIMonitor.start()
AIMonitor.join()
os.system('kill %d' % os.getpid())
print("Program completed")
