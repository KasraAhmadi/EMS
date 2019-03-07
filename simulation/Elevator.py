'''
	Project: Recommender Elevator Managment System (REMS)
	Author: Kasra Ahmadi
	Date: Nov 2019
'''

import gevent
import sys
import time
from gevent import Greenlet
from Order import Order
from operator import attrgetter
import datetime
import logging
from random import randint



time = datetime.datetime(2019,1,1,5,0,0)
completed = []
logging.basicConfig(stream=sys.stdout,level=logging.INFO)




class Elevator(Greenlet):
	t_door_operation = 6
	t_floor_to_floor = 3
	hit_list = []

	in_call = []
	out_call_down = []
	out_call_up = []

	possible_state = {"Stop": "Stop", "Up_Going": "Up_Going", "Down_Going": "Down_Going",
					  "Door_Operation": "Door_Operation"}



	def __init__(self, name, floor_list):
		Greenlet.__init__(self)
		self.name = name
		self.floor_list = floor_list
		self.now_position = 'G'
		self.state = self.possible_state["Stop"]
		#order list will be sorted at every clock of system
		self.order_list = []
		self.general_order_list = []


	def _run(self):
		while True:
			self.order_checker()
			self.elv_checker()
			gevent.sleep(1)
			self.elv_move()
			print("in_call:::{0}\nout_call_up:::{1}\nout_call_down:::{2}\n"
			.format(self.in_call,self.out_call_up,self.out_call_down))


	def elv_checker(self):
		global time
		if self.state == self.possible_state["Stop"] and len(self.order_list) == 0:
			self.state = self.possible_state["Stop"]
			time = time + datetime.timedelta(0, 1)

		else:
			''' Parking state Machine
			2 halate inke mosafer dakhel khod darad ya na ra barresi mikonad
			I) Agar mosafer dasht Faghat list maghsad ra barresi mikonad
			II) Agar mosafer nadasht list kasani ke montazerand ra barresi mikonad
			'''
			if self.state == self.possible_state["Stop"]:
				if len(self.ridden_order_list()) == 0: #HichKas savar nashode
					if self.get_floor_number(self.collective_mode().source ) > self.get_floor_number(self.now_position):
						#Avalin kasi ke darkhast dade self.order_list[0]
						self.state = self.possible_state["Up_Going"]
						self.is_anyone_onway()

						#Ooon TK Code ke moshkhas mikone too halate 6-->G va 2--->G aval 6 ro javab bede ya aval 2 ro
					elif len(self.waited_order_list())!= 0 and self.get_floor_number(self.collective_mode().source ) == self.get_floor_number(self.now_position):
						self.take_new_order()

					elif self.get_floor_number(self.collective_mode().source ) < self.get_floor_number(self.now_position):
						self.state = self.possible_state["Down_Going"]
						self.is_anyone_onway()

				else: # savar shode darim

					#Pro Mode

					if self.get_floor_number(self.ridden_order_list()[0].goal) > self.get_floor_number(self.now_position):
						self.state = self.possible_state["Up_Going"]
					elif self.get_floor_number(self.ridden_order_list()[0].goal) == self.get_floor_number(self.now_position):
						self.state = self.possible_state["Door_Operation"]
					elif self.get_floor_number(self.ridden_order_list()[0].goal ) < self.get_floor_number(self.now_position):
						self.state = self.possible_state["Down_Going"]

					''' Up_Going state Machine
					2 Halete inke asansor beistad
					I) Agar mosafer dasht va Mosafer be maghsad reside bood
					II) Agar kasi hame be samte bala miraft vaysa ta be oon ham service bedi
					'''
			elif self.state == self.possible_state["Up_Going"]:
				self.is_anyone_onway()
				self.check_reach()
				if len(self.waited_order_list())!= 0 and self.get_floor_number(self.collective_mode().source) == self.get_floor_number(self.now_position):
					self.take_new_order()



			elif self.state == self.possible_state["Down_Going"]:
				self.is_anyone_onway()
				self.check_reach()

				# TODO: Compelete this section
				if len(self.waited_order_list())!= 0 and self.get_floor_number(self.collective_mode().source) == self.get_floor_number(self.now_position):
					self.take_new_order()


			elif self.state == self.possible_state["Door_Operation"]: #Opening_Door state Machine
				#print("Door Operation :::: In position {0}.".format(self.now_position))
				self.clear_call_lists()
				self.state = self.possible_state["Stop"]


	#Clear in_call,out_call_up,out_call_down
	def clear_call_lists(self):
		if self.now_position in self.in_call:
			self.in_call.remove(self.now_position)
		if self.now_position in self.out_call_up:
			self.out_call_up.remove(self.now_position)
		if self.now_position in self.out_call_down:
			self.out_call_down.remove(self.now_position)



	'''Return the Top or Low Order source'''
	def collective_mode(self):
		down_collective_list = []
		up_collective_list = []
		for element in self.waited_order_list():
			if self.get_floor_number(element.goal) - self.get_floor_number(element.source) > 0 :
				down_collective_list.append(element)
			else:
				up_collective_list.append(element)

		self.sort_orders(down_collective_list)
		self.sort_orders(up_collective_list)
		if self.get_floor_number(self.waited_order_list()[0].goal) - self.get_floor_number(self.waited_order_list()[0].source) > 0:
			return down_collective_list[-1]
		else:
			return up_collective_list[0]



	def take_new_order(self):
		if len(self.ridden_order_list()) == 0:
			list = self.waited_order_list()
			self.same_floor(list)


	def same_floor(self,list):
		check = False
		global time
		for element in list:
			if self.get_floor_number(element.source) == self.get_floor_number(self.now_position):
				time = time + datetime.timedelta(0, self.t_door_operation)
				#print("Found A person :::: In position {0}.".format(self.now_position))
				element.change_state(time)
				check = True

		if check == True:
			self.state = self.possible_state["Door_Operation"]



	#in function barresi mikonad ke asansor be jahati miravad va mosafer niz be an jahat miravad , an ra savar konad
	def is_anyone_onway(self):
		global time
		list = self.waited_order_list()
		for element in list:
			if self.get_floor_number(element.goal) - self.get_floor_number(element.source) > 0 and self.state == self.possible_state["Up_Going"]:
				if self.get_floor_number(self.now_position) == self.get_floor_number(element.source):
					#print("Found A person in Up_Going  :::: In position {0}.".format(self.now_position))
					time = time + datetime.timedelta(0, self.t_door_operation)
					element.change_state(time)
					self.state = self.possible_state["Door_Operation"]

			elif self.get_floor_number(element.goal) - self.get_floor_number(element.source) < 0 and self.state == self.possible_state["Down_Going"]:
				if self.get_floor_number(self.now_position) == self.get_floor_number(element.source):
					#print("Found A person in Down_Going  :::: In position {0}.".format(self.now_position))
					time = time + datetime.timedelta(0, self.t_door_operation)
					element.change_state(time)
					self.state = self.possible_state["Door_Operation"]


	'''
		in function barresi mikonad ke aya az kasani ke savar shodeand kasi be maghsad reside ast ya na
	'''
	def check_reach(self):
		global completed
		global time
		list = self.ridden_order_list()
		for element in list:
			if self.get_floor_number(self.now_position) == self.get_floor_number(element.goal):
				# print("Be Maghsad reside shod :::: In position {0}.".format(self.now_position))
				time = time + datetime.timedelta(0, 3)
				element.end(time)
				#time = time + datetime.timedelta(0, 3)
				# logging.info("###############")
				print("#################")
				print("{0} ===> {1}".format(element.source,element.goal))
				print("{0} ===> {1} ===> {2}".format(element.time_to_start.strftime('%H:%M:%S'),element.time_to_take.strftime('%H:%M:%S'),element.time_to_end.strftime('%H:%M:%S')))
				completed.append(element)
				self.order_list.remove(element)
				self.state = self.possible_state["Door_Operation"]

	'''
		in function vazife darad ke asansor ra bar asase halete tain shode harkat dahad
	'''
	def elv_move(self):
		global time
		try:
			if self.state == self.possible_state["Up_Going"]:
				time = time + datetime.timedelta(0, self.t_floor_to_floor)
				self.now_position = self.floor_list[self.get_floor_number(self.now_position) + 1]
				# print("UpGoing :::: In position {0}.".format(self.now_position))
			elif self.state == self.possible_state["Down_Going"]:
				time = time + datetime.timedelta(0, self.t_floor_to_floor)
				# print("DownGoing :::: In position {0}.".format(self.now_position))
				self.now_position = self.floor_list[self.get_floor_number(self.now_position) - 1]
			# elif self.state == self.possible_state["Stop"]:
			#     time = time + datetime.timedelta(0, 1)

		except Exception as e:
			print("Moshkel dar harkat asansor")

	def sort_orders(self,list):
		for element in list:
			#calcuate the distance between G and other floor
			element.distance = self.get_floor_number(element.source)

		# source_lists = (element.source for element in list)
		# distination_lists = (element.distance for element in list)

		#sort based on distance to now_position
		list.sort(key=attrgetter('distance'), reverse=True)

	def waited_order_list(self):
		list = []
		for element in self.order_list:
			if element.order_state == Order.possible_state["waited"]:
				list.append(element)
		return list

	def ridden_order_list(self):
		list = []
		for element in self.order_list:
			if element.order_state == Order.possible_state["ridden"]:
				list.append(element)
		return list

	def get_floor_number(self,input):
		return self.floor_list.index(input)

	def distance_floor(self,next):
		return abs(self.get_floor_number(self.now_position)-self.get_floor_number(next))

	def order_generator(self,fromTime,untilTime,orderFrom,orderTo,traffic):

		step = 0
		if traffic == "High":
			step = 20
		elif traffic == "Medium":
			step = 40
		elif traffic == "Low":
			step = 60

		myTime = fromTime
		i = 0

		while  myTime < untilTime:
			self.general_order_list.append(Order(orderFrom, orderTo, myTime))
			myTime = myTime + datetime.timedelta(0, step)


	def generate_Bus_Data(self,element):
		if self.get_floor_number(element.source ) > self.get_floor_number(element.goal):
			self.out_call_down.append(element.source)
		elif self.get_floor_number(element.source ) < self.get_floor_number(element.goal):
			self.out_call_up.append(element.source)
		self.in_call.append(element.goal)


	def order_checker(self):
		global time
		for element in self.general_order_list:
			if element.time_to_start <= time:
				self.order_list.append(element)
				self.general_order_list.remove(element)
				self.generate_Bus_Data(element)

	def reset_time(self):
		global time
		time = datetime.datetime(2019,1,1,5,0,0)


	def generate_Random(self,fromTime,untilTime,traffic):

		step = 0
		if traffic == "High":
			step = 5
		elif traffic == "Medium":
			step = 15
		elif traffic == "Low":
			step = 60

		print(untilTime)
		myTime = fromTime

		while  myTime < untilTime:
			fromOrder = self.floor_list[randint(0, len(self.floor_list) - 1)]
			toOrder = self.floor_list[randint(0, len(self.floor_list) -1)]
			if fromOrder != toOrder:
				self.general_order_list.append(Order(fromOrder, toOrder, myTime))
			myTime = myTime + datetime.timedelta(0, step)



		print("DONE")



	def test_order(self):

		print('##################')
		# self.order_list.append(Order('3', '6', "10:00:00"))
		# self.order_list.append(Order('2','1',"10:00:00"))
		# self.order_list.append(Order('2', 'G', "10:00:00"))
		# self.order_list.append(Order('6', 'G', "10:00:00"))
		# self.order_list.append(Order('4', '2', "10:00:00"))
		#
		# self.order_list.append(Order('6', '1', "10:00:00"))
		# self.order_list.append(Order('G', '6', "10:00:00"))
		# self.order_list.append(Order('5','3',"10:00:00"))
		# self.order_list.append(Order('6', '2', "10:03:00"))
		# self.order_list.append(Order('P2', '3', "10:00:00"))
		#
		#
		# self.order_list.append(Order('G', '5', time))
		# self.order_list.append(Order('4', 'P1', time))
		# self.order_list.append(Order('5', '6', time))
		# self.order_list.append(Order('6', 'G', time))
		#
		#
		#
		#
		#
		#
		# self.order_list.append(Order('2', '3', time))
		# self.order_list.append(Order('4', '6', time))
		#
		# self.order_list.append(Order('3', 'G', time))
		# self.order_list.append(Order('P2', '3', time))
		# self.order_list.append(Order('6', 'P2', time))

		# self.order_generator(time,time + datetime.timedelta(0, 9000),"G","4","Medium")
		# self.order_generator(time,time + datetime.timedelta(0, 9000),"3","P1","Medium")
		# self.generate_Random(time,time + datetime.timedelta(0, 9000),"High")
		#
		#self.general_order_list.append(Order('P1', '6', time + datetime.timedelta(0, 7)))
		self.general_order_list.append(Order('3', '1', time + datetime.timedelta(0, 3)))
		self.general_order_list.append(Order('G', '5', time + datetime.timedelta(0, 1)))
		# self.general_order_list.append(Order('G', '6',time))
		#
		# self.general_order_list.append(Order('4', '6', time))
		# self.general_order_list.append(Order('6', '1', time))


	   # self.order_list.sort(key=lambda x: x.time_to_start, reverse=True)

	   # self.order_list.append(Order('3', '8', "10:00:00"))




if __name__ == "__main__":
	Elv_A = Elevator("A", ['P2','P1','G','1','2','3','4','5','6','7','8'])
	Elv_A.start()
	Elv_A.test_order()
	Elv_A.join()

	print("Program completed")
