#!/usr/bin/python

from enum import Enum

class World(Enum):
    RACES = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", \
        "Half-Elf", "Half-Orc", "Tiefling"]
    R_SH = ["dwa", "elf", "halfling", "hum", "dra", "gno", "halfelf", \
        "halforc", "tiefling"]
    CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", \
        "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    CL_SH = ["barb", "bard", "cler", "dru", "fig", "monk", "pal", "rang", \
        "rogue", "sorc", "warl", "wiz"]
    ALIG = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", \
        "True Neutral", "Chaotic Neutral", "Lawful Evil", \
        "Neutral Evil", "Chaotic Evil"]
    ALIG_CHART = [["Lawful", "Neutral", "Chaotic"], \
        ["Good", "Neutral", "Evil"]]
    W_THRESH = [100, 1150, 3700, 6800, 11000]
    WEAP_TYPE = {
        "Simple Melee": "configs/config_simple_melee.ini", 
        "Simple Ranged": "configs/config_simple_ranged.ini", 
        "Martial Melee": "configs/config_martial_melee.ini", 
        "Martial Ranged": "configs/config_martial_ranged.ini"
    }
    ARM_TYPE = {
        "Light": "configs/config_armor_light.ini", 
        "Medium": "configs/config_armor_medium.ini", 
        "Heavy": "configs/config_armor_heavy.ini"
    }
    
