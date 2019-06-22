
import os.path

class Identity():
	path = "/home/pi/Kasra/Identity.log"
	#path = "./Identity.log"



	def __init__(self):
		if(not os.path.isfile(self.path)):
			file = open(self.path,"w+")
			file.write("Initial:False\nId:Null")
			file.close()

	def ChangeSharedPref(self,subject,Replace):
		NewData = ""
		file = open(self.path,"r")
		data = file.readlines()
		for line in data:
			sec = line.split(":")
			if(sec[0] == subject):
				NewData = NewData + str(sec[0]) + ":" + Replace + "\n"
			else:
				NewData = NewData + str(sec[0]) + ":" + str(sec[1])
		file.close()
		file = open(self.path,"w")
		file.write(NewData)

	def read(self,subject):
		file = open(self.path,"r")
		data = file.readlines()
		for line in data:
			sec = line.split(":")
			if(sec[0] == subject):
				file.close()
				out = sec[1].replace('\n',"")
				return out
		return "Subject not found"
