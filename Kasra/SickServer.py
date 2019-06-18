import socket
import time
import threading
import subprocess
import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logging.info("Sick Server started")
cnt = 0
ls = []
sema = 1
res = 0
def Acc():
	global res
	global sema
	print("checker starts")
	while True:
		try:
			sema = 0
			t = float(time.time()) - ls[-1]
			del ls[:]
			res = 0
			sema = 1
		except Exception as e: #it means empty list
			res = res + 1
			sema = 1
			logging.info("Sick Server little error")
			if (res == 5):
				logging.info("Sick Server LtClient restart")
				subprocess.call("systemctl restart LtClient.service",shell=True,stderr=subprocess.STDOUT)
			elif( res == 60 ):
				res = 0
				logging.info("Sick Server system restart")
				subprocess.call("reboot",shell=True,stderr=subprocess.STDOUT)

		time.sleep(60) #check every 60 seconds

def Handler():
    global sema
    global cnt
    try:
        clientsocket = socket.socket()
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port=60006
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(("0.0.0.0", port))
        serversocket.listen(1)
        print("Listen to Internal socket")
        Client,addr = serversocket.accept()
        clientsocket = Client
        print("Got a connection from Internal socket")
        while True:
            msg = clientsocket.recv(1000)
            msg = msg.decode("ascii")
            if(msg=="Alive"):
                while True:
                    if sema == 1:
                        logging.info("added")
                        ls.append(float(time.time()))
                        break
            elif(msg == ""):
                print("Empty packet from Internal Socket")
                raise Exception

    except Exception as e:
        print(e)
        serversocket.close()
        raise Exception

print("ALINE?????")
t1 = threading.Thread(target=Handler, args=())
t1.start()
t2 = threading.Thread(target=Acc, args=())
t2.start()
while(1):
        t1.join()
        time.sleep(5)
        t1 = threading.Thread(target=Handler, args=())
        t1.start()
