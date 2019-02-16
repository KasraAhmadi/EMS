#!/usr/bin/env python

# import os
import socket
import time
import Constants
# from PythonModel import PythonModel
from HardwareInterface import HardwareInterface
from ElevatorParams import ElevatorParams
import json
import threading
# import datetime
# import sys
from multiprocessing import Process, Value
import ColorSubmit

common = 0
check = 0

#color = ColorSubmit.ColorSubmit()

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((Constants.WRAPPER_IP, Constants.WRAPPER_PORT))  # TODO: Exception Handling for timeout and refuse

	#AI Socket
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2.connect((Constants.WRAPPER_IP, 60007))  # TODO: Exception Handling for timeout and refuse

except Exception as e:
	print "Problem in Internal Connection"

hardware_interface = HardwareInterface()
elevators = []

while not(hardware_interface.reconnect_to_board()):
	#color.ChangeSharedPref("Physical", "False")
	s.sendall("ErrorConnection")
	print 'Problem in Serial Interface'
	#Form One

#color.ChangeSharedPref("Physical", "True")

elv_count = hardware_interface.get_elv_count()

print '*************************'
print elv_count
print '*************************'

for i in range(elv_count):
	elevators.append(ElevatorParams())

elevators.append(ElevatorParams())	#one extra, since out id is 1-based

def receive(sm, c, lock, common):

	global check
	global elevators
	try:
		while 1:
			if c.value == 0:
				txt = s.recv(9000)
				if txt != "":
					txt_str = txt.decode('ascii')
					print "loading Json"
					json_object = json.loads(txt_str)
					print "msg recvd from server"
					op = json_object["OP"]
					if op == 'C':
						elv_id = int(json_object["id"])
						elv_floor = int(json_object["floor"])
						print elv_floor
						if (elv_id <= elv_count) and (elv_floor < Constants.MAX_FLOORS):
							with lock:
								elevators[elv_id].control_elevator(elv_id, elv_floor)
					elif op == 'B':
						sm.value = 1
						hardware_interface.reconnect_to_board()
						time.sleep(1)
						sm.value = 0
					elif op == 'R':
						if json_object["Type"] != 'S':
							print 'type not as expected!'
						else:
							sm.value = 1
							elv_id = int(json_object["ST"])
							print "reading setting id = "
							print elv_id
							json_to_send = elevators[elv_id].read_setting(elv_id)
							print json_to_send
							s.sendall(json_to_send)
							time.sleep(1)
							print "finished reading setting"
							sm.value = 0
					elif op == 'S':
						print "writing setting for id "
						sm.value=1
						time.sleep(1)
						elv_id = int(json_object["id"])
						print elv_id
						elevators[elv_id].write_setting(elv_id, json_object)
						time.sleep(40)  #TODO: fix this value
						print "write setting finished"
						  sm.value=0
					elif op == 'L':
						print "learn command recved"
						sm.value = 1
						elv_id = int(json_object["id"])
						print elv_id
						elevators[elv_id].enter_learn_mod(elv_id)
						time.sleep(1)
						sm.value = 0
					elif op == 'E':
						sm.value = 1
						time.sleep(1)
						json_to_send = json.dumps({"ECOUNT": elv_count})
						s.sendall(json_to_send)
						time.sleep(1)
						sm.value = 0
				else:
					raise Exception


	except Exception as e:
		print e
		common.value = 1


def check_changer(n, common):

	global check
	while 1:
		time.sleep(1)
		if n.value == 0:
			n.value = 1
		else:
			n.value = 0


def send(setM, m, lock, common):

		global elevators
		try:
			while True:
				if m.value == 1:
					elv_iter = 1
					while elv_iter <= elv_count:
						if setM.value == 0:
							fin = []
							with lock:
								elevators[elv_iter].monitor_elevator(elv_iter)
							if elevators[elv_iter].elv_lift_fault != elevators[elv_iter].elv_perv_fault:
								elevators[elv_iter].elv_perv_fault = elevators[elv_iter].elv_lift_fault
							else:
								elevators[elv_iter].elv_lift_fault = 0
							mon = {"id": elv_iter, "mode": elevators[elv_iter].elv_mode,
								"floor number": elevators[elv_iter].elv_floor,
								"position": elevators[elv_iter].elv_car_position,
								"fault": elevators[elv_iter].elv_lift_fault,
								"in call": elevators[elv_iter].elv_call_car,
								"out call up": elevators[elv_iter].elv_call_hall_up,
								"out call down": elevators[elv_iter].elv_call_hall_down,
								"lift status": elevators[elv_iter].elv_lift_stat,
								"numerator": elevators[elv_iter].elv_numerator_concat,
								"direction": elevators[elv_iter].elv_direction,
								"ErrorConnection": elevators[elv_iter].hasErrorB
								}
							fin.append(mon)
							json_to_send = json.dumps({"elevators": fin})
							time.sleep(0.4)
							elv_iter += 1
							s.sendall(json_to_send)
							s2.sendall(json_to_send)
		except Exception as e:
				print e
				common.value = 1


#  Hardware Interface Mode
if Constants.HARDWARE_INTERFACE == 1:
	share = Value('i', 1)
	common = Value('i', 0)
	settingMut = Value('i',0)
	lock = threading.Lock()

	p1 = Process(target=send, args=(settingMut, share, lock, common))
	p2 = Process(target=receive, args=(settingMut, share, lock, common))
	p3 = Process(target=check_changer, args=(share, common))

	p1.start()
	p2.start()
	p3.start()

	while 1:
		time.sleep(1)
		if common.value == 1:
			p1.terminate()
			p2.terminate()
			p3.terminate()
			raise Exception
