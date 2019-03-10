from socketIO_client_nexus import SocketIO, LoggingNamespace
import json
def on_connect():
	print('connect')

def on_disconnect():
	print('disconnect')

def on_reconnect():
	print('reconnect')

def on_aaa_response(*args):
	print('on_aaa_response', args)

def Alive(*args):
	print("Broadcast")

socketIO = SocketIO('31.184.135.192', 80)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)
reg_data = {"moduleId":0}
socketIO.emit("Register",json.dumps(reg_data))
socketIO.on("Alive",Alive)

while 1:
	pass
