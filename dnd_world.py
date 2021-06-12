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
    WEAPON = {
        "Simple Melee": {
            "Club": {
                "price": .1,
                "can_wield_shield": True},
            "Dagger": {
                "price": 2,
                "can_wield_shield": True},
            "Greatclub": {
                "price": .2,
                "can_wield_shield": False},
            "Handaxe": {
                "price": 5,
                "can_wield_shield": True},
            "Javelin": {
                "price": .5,
                "can_wield_shield": True},
            "Light Hammer": {
                "price": 2,
                "can_wield_shield": True},
            "Mace": {
                "price": 5,
                "can_wield_shield": True},
            "Quarterstaff": {
                "price": .2,
                "can_wield_shield": True},
            "Sickle": {
                "price": 1,
                "can_wield_shield": True},
            "Spear": {
                "price": 1,
                "can_wield_shield": True}
        },
        "Simple Ranged": {
            "Light Crossbow": {
                "price": 25,
                "can_wield_shield": False},
            "Dart": {
                "price": .05,
                "can_wield_shield": True},
            "Shortbow": {
                "price": 25,
                "can_wield_shield": False},
            "Sling": {
                "price": .1,
                "can_wield_shield": True}
        },
        "Martial Melee": {
            "Battleaxe": {
                "price": 10,
                "can_wield_shield": True},
            "Flail": {
                "price": 10,
                "can_wield_shield": True},
            "Glaive": {
                "price": 20,
                "can_wield_shield": False},
            "Greataxe": {
                "price": 30,
                "can_wield_shield": False},
            "Greatsword": {
                "price": 50,
                "can_wield_shield": False},
            "Halberd": {
                "price": 20,
                "can_wield_shield": False},
            "Lance": {
                "price": 10,
                "can_wield_shield": True},
            "Longsword": {
                "price": 15,
                "can_wield_shield": True},
            "Maul": {
                "price": 10,
                "can_wield_shield": False},
            "Morningstar": {
                "price": 15,
                "can_wield_shield": True},
            "Pike": {
                "price": 5,
                "can_wield_shield": False},
            "Rapier": {
                "price": 25,
                "can_wield_shield": True},
            "Scimitar": {
                "price": 25,
                "can_wield_shield": True},
            "Shortsword": {
                "price": 10,
                "can_wield_shield": True},
            "Trident": {
                "price": 5,
                "can_wield_shield": True},
            "Warpick": {
                "price": 5,
                "can_wield_shield": True},
            "Warhammer": {
                "price": 15,
                "can_wield_shield": True},
            "Whip": {
                "price": 2,
                "can_wield_shield": True}
        },
        "Martial Ranged": {
            "Blowgun": {
                "price": 10,
                "can_wield_shield": True},
            "Hand Crossbow": {
                "price": 75,
                "can_wield_shield": True},
            "Heavy Crossbow": {
                "price": 50,
                "can_wield_shield": False},
            "Longbow": {
                "price": 50,
                "can_wield_shield": False},
            "Net": {
                "price": 1,
                "can_wield_shield": True}
        }
    }
