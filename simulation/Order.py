
from enum import Enum

class Order:

    possible_state = {"ridden":"ridden","waited":"waited"}

    def __init__(self,source,goal,time_to_start):

        self.source = source #source
        self.goal = goal #destination
        self.time_to_start = time_to_start #time that this order send to system
        self.order_state = self.possible_state["waited"]#order of state 1)Done 2)Progress
        self.time_to_take = None
        self.time_to_end = None #time that service to this order ends
        self.distance = None #distance from now to source

    def change_state(self,time_to_take):
        if self.order_state == self.possible_state["waited"]:
            self.order_state = self.possible_state["ridden"]
        else:
            raise Exception("This order is ridden before")
        self.time_to_take = time_to_take
    def end(self,time):
            self.time_to_end = time





if __name__ == "__main__":
    a = Order("P2","P1","10:00:00")