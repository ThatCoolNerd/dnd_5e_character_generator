#!/usr/bin/python

# imports
from dnd_world import World
import random
import die
import re

# races = World.RACES.value
# r_sh = World.R_SH.value
# classes = World.CLASSES.value
# alig = World.ALIG.value


# functions
def rfname(r):
    "Pull a random first name from a text file based on race"
    
    for i in range(len(World.RACES.value)):
        if r == World.RACES.value[i]:
            path = f"names/{World.R_SH.value[i]}_fnames.txt"
            name = open(path, "r")
            break
    
    names = name.read().split(';')
    name.close()
    return re.sub("\n", "", random.choice(names))

def rlname(r):
    "Pull a random last name from a text file based on race"
    
    for i in range(len(World.RACES.value)):
        if r == World.RACES.value[i]:
            path = f"names/{World.R_SH.value[i]}_lnames.txt"
            name = open(path, "r")
            break
    
    names = name.read().split(';')
    name.close()
    return re.sub("\n", "", random.choice(names))
    
def rrace():
    "Return random race"
    return random.choice(World.RACES.value)

def rclass(): 
    "Return random class"
    return random.choice(World.CLASSES.value)
    
def ralignment(): 
    "Return random alignment"
    return random.choices(World.ALIG.value)

def rwealth():
    "Return a random amount of wealth (in GP)"
    return int(die.rolld(15000) * (random.randrange(82, 99) / 100))

def get_wealth_desc(w): 
        "Return a random description of the character's appearance (GP based)"
        
        if w <= 100:
            txt = open("wealth_descs/s_poor.txt", "r")
        elif w <= 1250:
            txt = open("wealth_descs/poor.txt", "r")
        elif w <= 5800:
            txt = open("wealth_descs/moderate.txt", "r")
        elif w <= 12500:
            txt = open("wealth_descs/wealthy.txt", "r")
        elif w >= 12500:
            txt = open("wealth_descs/s_wealthy.txt", "r")
            
        pot_descs = txt.read().split(",   ")
        txt.close()
        return re.sub("\n", "", random.choice(pot_descs))
