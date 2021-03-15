#!/usr/bin/python

##imports
import random
import die

##functions
def rfname(r) :
    "Pull a random first name from a text file based on race"
    
    if r == "Dwarf" :
        names = open("names/dwa_fnames.txt", "r")
    
    elif r == "Elf" :
        names = open("names/elf_fnames.txt", "r")
    
    elif r == "Halfling" :
        names = open("names/halfling_fnames.txt", "r")
    
    elif r == "Human" :
        names = open("names/hum_fnames.txt", "r")
    
    elif r == "Dragonborn" :
        names = open("names/dra_fnames.txt", "r")
    
    elif r == "Gnome" :
        names = open("names/gno_fnames.txt", "r")
    
    elif r == "Half-Elf" :
        names = open("names/halfelf_fnames.txt", "r")
    
    elif r == "Half-Orc" :
        names = open("names/halforc_fnames.txt", "r")
    
    elif r == "Tiefling" :
        names = open("names/tiefling_fnames.txt", "r")
    
    else :
        return "Error determining name based on race."
    
    name = names.read().split(', ')
    names.close()
    return name[int(random.random() * (len(name) - 1))]

def rlname(r) :
    "Pull a random last name from a text file based on race"
    
    if r == "Dwarf" :
        names = open("names/dwa_lnames.txt", "r")
    
    elif r == "Elf" :
        names = open("names/elf_lnames.txt", "r")
    
    elif r == "Halfling" :
        names = open("names/halfling_lnames.txt", "r")
    
    elif r == "Human" :
        names = open("names/hum_lnames.txt", "r")
    
    elif r == "Dragonborn" :
        names = open("names/dra_lnames.txt", "r")
    
    elif r == "Gnome" :
        names = open("names/gno_lnames.txt", "r")
    
    elif r == "Half-Elf" :
        names = open("names/halfelf_lnames.txt", "r")
    
    elif r == "Half-Orc" :
        names = open("names/halforc_lnames.txt", "r")
    
    elif r == "Tiefling" :
        names = open("names/tiefling_lnames.txt", "r")
    
    else :
        return "Error determining name based on race."
    
    name = names.read().split(', ')
    names.close()
    return name[int(random.random() * (len(name) - 1))]
    
def rrace() :
    "Return random race"
    
    races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", \
             "Half-Elf", "Half-Orc", "Tiefling"]
    return races[int(random.random() * len(races))]

def rclass() : 
    "Return random class"
    
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", \
               "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    return classes[int(random.random() * len(classes))]
    
def ralignment() : 
    "Return random alignment"
    
    alig = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
    return alig[int(random.random() * len(alig))]

def rwealth() :
    "Return a random amount of wealth (in GP)"
    
    return int(die.rolld(15000) * (random.randrange(82, 99) / 100))
