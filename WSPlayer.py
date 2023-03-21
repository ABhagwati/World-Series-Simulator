#
# Name: Arav Bhagwati
# Player Class. This class contains the information for each instance of a player

from random import random


class Player:

    """Each player will have a random hit based on each type
    of hit probability."""

    def __init__(self, name, batting_avg, hits, doubles, triples, homers):
        self.name = name
        self.last_name = name[3:]
        self.base = 0
        self.number_of_singles = hits - (doubles + triples + homers)
        self.batting_avg = batting_avg
        self.probSingle = self.number_of_singles / hits
        self.probDouble = doubles / hits
        self.probTriple = triples / hits
        self.probHomer = homers / hits

        self.homer = False
        self.homers_list = []
            
    def swing(self): # player swings and result is decided below. I chose these numbers because I felt that they would best suit the game of baseball.
        "Player gets a certain type of hit based on their statistics."

        randomizer1 = random() # first random 
        randomizer2 = random() # second random
        if randomizer1 <= self.batting_avg and randomizer1 > 0: # player gets a hit
            self.hit = True
            if (self.probSingle >= 0.5 and self.probSingle <= 1) and (randomizer2 >= 0.5 and randomizer2 <= 1): # single
                self.single = True
                result = 1
                return result
            elif (self.probDouble >= 0.25 and self.probDouble < 0.6) and (randomizer2 >= 0.25 and randomizer2 < 0.6): # double
                self.double = True
                result = 2
                return result
            elif (self.probHomer >= 0.1 and self.probHomer < 0.4) and (randomizer2 >= 0.1 and randomizer2 < 0.4): # Homer
                self.homer = True
                result = 4
                return result
            elif (self.probTriple > 0 and self.probTriple < 0.15) and (randomizer2 > 0 and randomizer2 < 0.15): # triple
                self.triple = True
                result = 3
                return result
            else: # player is out if none of the above is true
                self.hit = False
                result = 0
                return result
        else: # player is out if the first if statement is false
            self.hit = False
            result = 0
            return result
            

    def getName(self):
        "Returns the player's full name. Ex: R. Arozarena"
        return self.name

    def getLastName(self): # getting the last name is helpful for the home run sorting
        "Returns the player's last name. Ex: Arozarena"
        return self.last_name

