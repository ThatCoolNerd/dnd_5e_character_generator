#!/usr/bin/python

from enum import Enum

class World(Enum):
    RACES = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", \
             "Half-Elf", "Half-Orc", "Tiefling"]
    R_SH = ["dwa", "elf", "halfling", "hum", "dra", "gno", "halfelf", \
            "halforc", "tiefling"]
    CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", \
               "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    ALIG = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", \
            "True Neutral", "Chaotic Neutral", "Lawful Evil", \
            "Neutral Evil", "Chaotic Evil"]