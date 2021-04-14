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
    #for kind, choices in World.CL_GEAR_STER.value.items():
    #    print(f"{kind}: {choices}")
    return re.sub("\n", "", random.choice(names))

def rrace(): return random.choice(World.RACES.value)
def rclass(): return random.choice(World.CLASSES.value)
def ralignment(): return random.choices(World.ALIG.value)

def rwealth():
    "Return a random amount of wealth (in GP)"
    return int(die.rolld(World.W_THRESH.value[-1]) * \
        (random.randrange(82, 99) / 100))

def rclothing():
    "Return a randomly generated article of outside clothing"
    armor_type = random.choice(list(World.ARMOR.value.keys()))
    armor = random.choice(World.ARMOR.value[armor_type]["ar_kind"])
    return armor

def rweapon():
    kind = random.choice(list(World.WEAPON.value.keys()))
    weapon = random.choice(list(World.WEAPON.value[kind].keys()))
    
    if weapon == "Dart":
        return "handful of darts"
    else:
        return weapon

def get_wealth_desc(w): 
    "Return a random description of the character's appearance (GP based)"
    wd_txt_name = ["s_poor", "poor", "moderate", "wealthy", "s_wealthy"]
    
    for i in range(len(wd_txt_name)):
        if w <= World.W_THRESH.value[i]:
            txt = open(f"wealth_descs/{wd_txt_name[i]}.txt", "r")
            break
        
    if w > World.W_THRESH.value[-1]:
        txt = open(f"wealth_descs/{wd_txt_name[-1]}.txt", "r")
    
    pot_descs = txt.read().split(";")
    txt.close()
    return re.sub("\n", "", random.choice(pot_descs))

def print_weapons():
    for typee, listt in World.WEAPON.value.items():
        print(f"{typee}:\n")
        for weapon, price in listt.items():
            if price < .1:
                cost = int(price * 100)
                currency = "CP"
            elif price < 1:
                cost = int(price * 10)
                currency = "SP"
            else:
                cost = price
                currency = "GP"
            
            print("   ", end = "")
            print(weapon.ljust(18, "."), end = "")
            print("| {:>2} ".format(cost), end = "")
            print(currency)
        print()
