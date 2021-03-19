#!/usr/bin/python

##imports
import random
import die

races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", \
         "Half-Elf", "Half-Orc", "Tiefling"]
r_sh = ["dwa", "elf", "halfling", "hum", "dra", "gno", "halfelf", "halforc", \
        "tiefling"]

##functions
def rfname(r) :
    "Pull a random first name from a text file based on race"
    
    for i in range(len(races)) :
        if r == races[i] :
            path = f"names/{r_sh[i]}_fnames.txt"
            name = open(path, "r")
            break
    
    names = name.read().split(', ')
    name.close()
    return random.choice(names)

def rlname(r) :
    "Pull a random last name from a text file based on race"
    
    for i in range(len(races)) :
        if r == races[i] :
            path = f"names/{r_sh[i]}_lnames.txt"
            name = open(path, "r")
            break
    
    names = name.read().split(', ')
    name.close()
    return random.choice(names)
    
def rrace() :
    "Return random race"
    return random.choice(races)

def rclass() : 
    "Return random class"
    
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", \
               "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    return random.choice(classes)
    
def ralignment() : 
    "Return random alignment"
    
    alig = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", \
            "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", \
            "Chaotic Evil"]
    return random.choices(alig)

def rwealth() :
    "Return a random amount of wealth (in GP)"
    
    return int(die.rolld(15000) * (random.randrange(82, 99) / 100))
