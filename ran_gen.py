#!/usr/bin/python

# imports
from dnd_world import World
import random
import die
import re

# functions
def rname(r, pos):
    "Pull a random first name from a text file based on race"
    if pos == "First": f_or_l = "f"
    else: f_or_l = "l"
    
    for i in range(len(World.RACES.value)):
        if r == World.RACES.value[i]:
            path = f"names/{World.R_SH.value[i]}_{f_or_l}names.txt"
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
