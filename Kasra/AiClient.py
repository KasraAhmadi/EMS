from socketIO_client_nexus import SocketIO, LoggingNamespace
import time
from threading import Thread
import socket
import queue as queue
import datetime
import os
import json
import Identity

BUF_SIZE = 100
q = queue.Queue(BUF_SIZE)

class resourceMonitor(Thread):
	def on_connect(self):
		print('connect')

	def on_disconnect(self):
		print('disconnect')

	def on_reconnect(self):
		print('reconnect')

	def ssh(self,*args):
		print('ssh called', args)


	def __init__(self):
		self.id = 0
		Thread.__init__(self)






	def run(self):
		try:
			print("Trying to connect to socketIO")
			self.socket = SocketIO("31.184.135.192", 80)
			print("SocketIO connection established")
			self.socket.on('connect', self.on_connect)
			self.socket.on('disconnect', self.on_disconnect)
			self.socket.on('reconnect', self.on_reconnect)
			self.socket.on('ssh', self.ssh)
			while True:
				time.sleep(0.4)
				if not q.empty():
					data = q.get()
					self.socket.emit("data",data)

		except Exception as e:
			print(e)



class AIListener(Thread):
	def __init__(self):
		Thread.__init__(self)
		#Id
		self.id = "None"
		file = Identity.Identity()
		init = file.read("Initial")
		if(init == "True"):
			self.id = file.read("Id")
		self.port = 60007
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serversocket.bind(("0.0.0.0", self.port))
		self.serversocket.listen(1)
		print("Listen to Internal socket")

	def cleanData(self,data):
		msg_str = str(data.decode("ascii"))  # cast shared to string
		json_input = json.loads(msg_str)
		json_input['elevators'][0]['id']

		out_data = {}
		now = datetime.datetime.now()
		time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)
		out_data['module_id'] = self.id
		out_data['data'][0]['direction'] = json_input['elevators'][0]['direction']
		out_data['data'][0]['time'] = time_now
		out_data['data'][0]['in_call'] = json_input['elevators'][0]['in call']
		out_data['data'][0]['out_call_up'] = json_input['elevators'][0]['out call up']
		out_data['data'][0]['out_call_down'] = json_input['elevators'][0]['out call down']
		out_data['data'][0]['numerator'] = json_input['elevators'][0]['numerator']
		out_data['data'][0]['lift_status'] = json_input['elevators'][0]['lift status']
		out_data['data'][0]['elv_id'] = json_input['elevators'][0]['id']
		json_data = json.dumps(out_data)
		return json_data


	def run(self):
		try:
			Client,addr = self.serversocket.accept()
			self.clientsocket = Client
			self.clientsocket.setblocking(1)
			self.clientsocket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
			while True:
				msg = self.clientsocket.recv(90000)
				if(msg == ""):
					raise Exception
				else:
					myOut = cleanData(msg)
					print(myOut)
					if not q.full():
						q.put(myOut)
		except Exception as e:
			print(e)
			self.serversocket.close()

AIMonitor = AIListener()
socketIOMonitor = resourceMonitor()
AIMonitor.start()
socketIOMonitor.start()
AIMonitor.join()
os.system('kill %d' % os.getpid())
print("Program completed")
