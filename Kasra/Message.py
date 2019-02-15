import json
import os.path
import subprocess
import Identity
file = Identity.Identity()

class Message():
    #Coming Attr
    Type = None
    PacketNumber = None
    Data = None 
    TimeOut = 20


    #Response Attr
    TypeBack = None
    PacketNumberBack = None
    DataBack = None
    Id = None
    JsonBack = None

    sshInsOne = "sshpass -p  HammerOn070oahdhvHvdkliv4731 ssh -t -t -R "
    sshInsTwo = ":localhost:22 -o StrictHostKeyChecking=no root@emspaarcontrol.com &"
    
    
    def __init__(self,Type = None,Data = None):
        self.Type = Type
        self.Data = Data
        print("A message has been arrived")
        self.Eval()
        self.JsonBack = json.dumps({'T':self.TypeBack,'D':self.DataBack})

    def getJson(self):
        return self.JsonBack
        
    def Eval(self):
        if(self.Type == 'D'):
            #send Data to Can
            self.TypeBack = "RD"
            self.SendByCan(self.Data)

        elif(self.Type == "Greet"):
            Id = file.read("Id")
            self.DataBack = Id
            self.TypeBack = "GreetBack"
            print(Id)

        elif(self.Type == "SSH"):
            #Run commands
            self.TypeBack = "SSHBack"
            Command = self.sshInsOne + self.Data +self.sshInsTwo

            try:
                print(Command)
                self.DataBack = subprocess.call(Command,shell=True,stderr=subprocess.STDOUT)
                print(self.DataBack)
                if(self.DataBack == 0):
                    self.DataBack = "Done"

            except Exception as e:
                print("Errror in Running Commands")
                self.DataBack = "Error"

            #Run that Command
        
    def SendByCan(self,text):    
        '''
            Can Stuff 
        '''
        if(text == "ok"):
            self.DataBack = "ack"
        elif():
            self.DataBack = "Error"
