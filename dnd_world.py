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
    CL_GEAR_STER = {
        "Barbarian": {
            "ar_kind": ["Light", "Medium"],
            "shield": True,
            "weap_type": ["Simple Melee", "Martial Melee"]
        },
        "Bard": {
            "ar_kind": ["Light"],
            "shield": False,
            "weap_type": ["Simple Melee", "Simple Ranged"]
        },
        "Cleric": {
            "ar_kind": ["Light", "Medium"],
            "shield": True,
            "weap_type": ["Simple Melee", "Simple Ranged"]
        },
        "Druid": {
            "ar_kind": ["Light", "Medium"],
            "shield": True,
            "weap_type": ["Simple Melee", "Simple Ranged"]
        },
        "Fighter": {
            "ar_kind": ["Light", "Medium", "Heavy"],
            "shield": True,
            "weap_type": ["Simple Melee", "Simple Ranged", "Martial Melee", \
                "Martial Ranged"]
        },
        "Monk": {
            "ar_kind": [],
            "shield": False,
            "weap_type": ["Simple Melee", "Simple Ranged"]
        },
        "Paladin": {
            "ar_kind": ["Light", "Medium", "Heavy"],
            "shield": True,
            "weap_type": ["Simple Melee", "Martial Melee"]
        },
        "Ranger": {
            "ar_kind": ["Light", "Medium"],
            "shield": True,
            "weap_type": ["Simple Ranged", "Martial Ranged"]
        },
        "Rogue": {
            "ar_kind": ["Light"],
            "shield": False,
            "weap_type": ["Simple Melee", "Simple Ranged"]
        },
        "Sorcerer": {
            "ar_kind": [],
            "shield": False,
            "weap_type": ["Simple Ranged"]
        },
        "Warlock": {
            "ar_kind": ["Light"],
            "shield": False,
            "weap_type": ["Simple Melee", "Simple Ranged"]
        },
        "Wizard": {
            "ar_kind": [],
            "shield": False,
            "weap_type": ["Simple Ranged"]
        }
    }
    CL_WEAPON_STER = {}
    ALIG = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", \
        "True Neutral", "Chaotic Neutral", "Lawful Evil", \
        "Neutral Evil", "Chaotic Evil"]
    ALIG_CHART = [["Lawful", "Neutral", "Chaotic"], \
        ["Good", "Neutral", "Evil"]]
    W_THRESH = [100, 1150, 3700, 6800, 11000]
    ARMOR = {
        "Light": {
            "ar_kind": ["Padded Leather", "Leather", "Studded Leather"],
            "price": [5, 10, 45]
        },
        "Medium": {
            "ar_kind": ["Hide", "Chain Shirt", "Scale Mail", "Breastplate", "Half Plate"],
            "price": [10, 50, 50, 400, 750]
        },
        "Heavy": {
            "ar_kind": ["Ring Mail", "Chain Mail", "Splint", "Plate"],
            "price": [30, 75, 200, 1500]
        }
    }
    WEAPON = {
        "Simple Melee": {
            "Club": .1,
            "Dagger": 2,
            "Greatclub": .2,
            "Handaxe": 5,
            "Javelin": .5,
            "Light Hammer": 2,
            "Mace": 5,
            "Quarterstaff": .2,
            "Sickle": 1,
            "Spear": 1
        },
        "Simple Ranged": {
            "Light Crossbow": 25,
            "Dart": .05,
            "Shortbow": 25,
            "Sling": .1
        },
        "Martial Melee": {
            "Battleaxe": 10,
            "Flail": 10,
            "Glaive": 20,
            "Greataxe": 30,
            "Greatsword": 50,
            "Halberd": 20,
            "Lance": 10,
            "Longsword": 15,
            "Maul": 10,
            "Morningstar": 15,
            "Pike": 5,
            "Rapier": 25,
            "Scimitar": 25,
            "Shortsword": 10,
            "Trident": 5,
            "Warpick": 5,
            "Warhammer": 15,
            "Whip": 2
        },
        "Martial Ranged": {
            "Blowgun": 10,
            "Hand Crossbow": 75,
            "Heavy Crossbow": 50,
            "Longbow": 50,
            "Net": 1
        }
    }
