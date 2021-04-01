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
    ST_PERM = {
        "Barbarian":
            {
                50: 
                    {
                        "str": 0,
                        "con": 1,
                        "dex": 2,
                        "cha": 3,
                        "int": 4,
                        "wis": 5
                    },
                100:
                    {
                        "str": 0,
                        "con": 1,
                        "cha": 2,
                        "dex": 3,
                        "int": 4,
                        "wis": 5
                    }
            },
        "Bard":
            {
                100:
                    {
                        "cha": 0,
                        "dex": 1,
                        "wis": 2,
                        "con": 3,
                        "int": 4,
                        "str": 5
                    }
            },
        "Cleric":
            {
                50:
                    {
                        "wis": 0,
                        "str": 1,
                        "con": 2,
                        "dex": 3,
                        "cha": 4,
                        "int": 5
                    },
                100:
                    {
                        "wis": 0,
                        "con": 1,
                        "str": 2,
                        "dex": 3,
                        "cha": 4,
                        "int": 5
                    }
            },
        "Druid":
            {
                100:
                    {
                        "wis": 0,
                        "con": 1,
                        "dex": 2,
                        "cha": 3,
                        "int": 4,
                        "str": 5
                    }
            },
        "Fighter":
            {
                47:
                    {
                        "str": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "cha": 4,
                        "int": 5
                    },
                94:
                    {
                        "dex": 0,
                        "con": 1,
                        "wis": 2,
                        "cha": 3,
                        "int": 4,
                        "str": 5
                    },
                100:
                    {
                        "int": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "str": 4,
                        "cha": 5
                    }
            },
        "Monk":
            {
                100:
                    {
                        "dex": 0,
                        "wis": 1,
                        "con": 2,
                        "cha": 3,
                        "int": 4,
                        "str": 5
                    }
            },
        "Paladin":
            {
                50:
                    {
                        "str": 0,
                        "cha": 1,
                        "wis": 2,
                        "dex": 3,
                        "con": 4,
                        "int": 5
                    },
                100:
                    {
                        "str": 0,
                        "cha": 1,
                        "con": 2,
                        "dex": 3,
                        "wis": 4,
                        "int": 5
                    }
            },
        "Ranger":
            {
                92:
                    {
                        "dex": 0,
                        "wis": 1,
                        "con": 2,
                        "str": 3,
                        "int": 4,
                        "cha": 5
                    },
                100:
                    {
                        "str": 0,
                        "wis": 1,
                        "con": 2,
                        "dex": 3,
                        "int": 4,
                        "cha": 5
                    }
            },
        "Rogue":
            {
                60: 
                    {
                        "dex": 0,
                        "cha": 1,
                        "con": 2,
                        "wis": 3,
                        "int": 4,
                        "str": 5
                    },
                100:
                    {
                        "dex": 0,
                        "int": 1,
                        "con": 2,
                        "wis": 3,
                        "cha": 4,
                        "str": 5
                    }
            },
        "Sorcerer":
            {
                50: 
                    {
                        "cha": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "int": 4,
                        "str": 5
                    }, 
                100: 
                    {
                        "cha": 0,
                        "con": 1,
                        "wis": 2,
                        "dex": 3,
                        "int": 4,
                        "str": 5
                    }
            },
        "Wizard":
            {
                50:
                    {
                        "int": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "str": 4,
                        "cha": 5
                    },
                66: 
                    {
                        "int": 0,
                        "dex": 1,
                        "con": 2,
                        "wis": 3,
                        "str": 4,
                        "cha": 5
                    },
                100:
                    {
                        "int": 0,
                        "dex": 1,
                        "con": 2,
                        "con": 3,
                        "str": 4,
                        "cha": 5
                    }
            },
        "Warlock":
            {
                50: 
                    {
                        "cha": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "int": 4,
                        "str": 5
                    }, 
                100:
                    {
                        "cha": 0,
                        "con": 1,
                        "wis": 2,
                        "dex": 3,
                        "int": 4,
                        "str": 5
                    }
            }
    }
