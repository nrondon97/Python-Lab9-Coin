#Naylene Rondon
#4/3/17
#Lab 8
import random

class coin():
    """Simulates a coin that flips"""
    def __init__(self):
        self_sideup = "heads"

    def toss(self):
        if random.randint(0,1) == 0:
            self_sideup = "heads"

        else:
            self_sideup = "tails"

    def get_side(self):
        return self.__sideup

