from socketIO_client_nexus import SocketIO, LoggingNamespace
import time
from threading import Thread
import socket
import queue as queue


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
        Thread.__init__(self)



    def run(self):
        try:
            print("Trying to connect to socketIO")
            self.socket = SocketIO('localhost', 80)
            print("SocketIO connection established")
            self.socket.on('connect', self.on_connect)
            self.socket.on('disconnect', self.on_disconnect)
            self.socket.on('reconnect', self.on_reconnect)
            self.socket.on('ssh', self.ssh)
            # self.socket.emit('Register', {"moduleId": "10"})
            while True:
                time.sleep(0.4)
                if not q.empty():
                    data = q.get()
                    self.socket.emit("data",data)
                    print("Item used in Q")

        except Exception as e:
            print(e)



class AIListener(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.port = 60007
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversocket.bind(("0.0.0.0", self.port))
        self.serversocket.listen(1)
        print("Listen to Internal socket")


    def run(self):
        try:
            Client,addr = self.serversocket.accept()
            self.clientsocket = Client
            self.clientsocket.setblocking(1)
            self.clientsocket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
            while True:
                msg = self.clientsocket.recv(90000)
                msg = msg.decode("ascii")
                if(msg == ""):
                    logging.error("Empty packet from Internal Socket")
                    raise Exception
                else:
                    if not q.full():
                        q.put(msg)
                        print("Item added in Q")


        except Exception as e:
            print(e)
            self.serversocket.close()

if __name__ == "__main__":

    AIMonitor = AIListener()
    socketIOMonitor = resourceMonitor()

    AIMonitor.start()
    socketIOMonitor.start()


    print("Program completed")
