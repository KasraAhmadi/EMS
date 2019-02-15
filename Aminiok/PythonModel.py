# Python Model : A Simulator for Elevators Main Board

import Constants
from random import random


class PythonModel:
    elvHasFault = 0
    elvFault = 0

    elvDownMove = 0
    elvDownMovePerv = 0

    elvUpMove = 0
    elvUpMovePerv = 0

    elvFloorNu = 0
    elvFloorNuPerv = 0

    elvPosition = 0
    elvPositionPerv = 0

    elvDstFloor = 0
    elvDstFloorPerv = 0

    elvDoorOpen = 0
    elvDoorOpenPerv = 0

    elvInCall = bytearray([0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
    elvOutCallUp = bytearray([0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
    elvOutCallDown = bytearray([0xff, 0xff, 0xff, 0xff, 0xff, 0xff])

    inCall = 0
    inCallPerv = 0

    outCallUp = 0
    outCallUpPerv = 0

    outCallDown = 0
    outCallDownPerv = 0

    faultCounter = 0

    def __init__(self):
        print('Python Model Class was Invoked')
        self.elvDstFloor = int((random() * 100) % Constants.PYTHON_MODEL_MAX_FLOORS)

    def set_parameters(self):

        self.elvPosition = self.elvFloorNu * 230  # 230 is pure BS. for test only

        if self.elvFloorNu < self.elvDstFloor:
            self.elvUpMove = 1
            self.elvDownMove = 0
            self.elvFloorNu += 1
        elif self.elvFloorNu > self.elvDstFloor:
            self.elvUpMove = 0
            self.elvDownMove = 1
            self.elvFloorNu -= 1
        else:
            self.elvUpMove = 0
            self.elvDownMove = 0
            self.elvDstFloor = int((random() * 100) % Constants.PYTHON_MODEL_MAX_FLOORS)

        self.faultCounter += 1
        if self.faultCounter > 3:
            self.faultCounter = 0
            self.elvHasFault = 1
            self.elvFault = int(random() * 100) % 25  # 25 kinds of error
        else:
            self.elvHasFault = 0

        self.inCall = int((random() * 100) % Constants.PYTHON_MODEL_MAX_FLOORS)
        self.outCallUp = int((random() * 100) % Constants.PYTHON_MODEL_MAX_FLOORS)
        self.outCallDown = int((random() * 100) % Constants.PYTHON_MODEL_MAX_FLOORS)
        self.elvDoorOpen = int((random() * 100) % 2)
