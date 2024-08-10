#Naylene Rondon
#4/3/17
#Lab 8
import random

class coin():
    """Simulates a coin that flips"""
    def __init__(self):
        self.__sideup = "heads"

    def toss(self):
        toss = random.randint(0,1)
        if toss == 0:
            self.__sideup = "heads"

        else:
            self.__sideup = "tails"

    def get_side(self):
        return self.__sideup

