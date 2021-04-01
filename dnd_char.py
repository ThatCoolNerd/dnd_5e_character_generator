#!/usr/bin/python

# imports
from configparser import ConfigParser
from dnd_world import World
import ran_gen
import random
import die

config = ConfigParser()
config.read("config.ini")

# functions
def stat_gen(): 
    "Roll 4d6, drop the lowest, return total sum"
    
    rolls = [die.rolld(6), die.rolld(6), die.rolld(6), die.rolld(6)]
    rolls.remove(min(rolls))
            
    return sum(rolls)

def get_alig(alig_list):
    """
        First   [0] is lawful, neutral, chaotic
        Second  [1] is good, neutral, evil
    """
    
    alignment = ""
    if alig_list[0] == 1: 
        alignment = alignment + "Lawful"
    elif alig_list[0] == 2: 
        alignment = alignment + "Neutral"
    else: 
        alignment = alignment + "Chaotic"
        
    if alig_list[1] == 1: 
        alignment = alignment + " Good"
    elif alig_list[1] == 2: 
        alignment = alignment + " Neutral"
    else: 
        alignment = alignment + " Evil"
        
    if alig_list[0] == 2 and alig_list[1] == 2:
        alignment = "True Neutral"

    return alignment

def get_class_ster_nums(cl, data, md, cv):
    """
    cl = class;data = data value to search
    md = mod (how many # per list); cv = should convert to int
    """
    li = []
    li_s = config[cl][data].split(",")
    pos = 0
    
    if cv:
        if md == 1:
            while pos < len(li_s):
                li.append(int(li_s[pos]))
                pos += md
        else:
            while pos < len(li_s):
                li.append([int(li_s[pos]), int(li_s[pos+1])])
                pos += md
        
        return li
    else:
        return li_s

# body
class character:
    
    def __init__(self):
        #character traits
        self.p_race      = ran_gen.rrace()
        self.p_class     = ran_gen.rclass()
        self.p_alig_val  = [die.rolld(3), die.rolld(3)]
        self.p_alignment = get_alig(self.p_alig_val)
        
        #attributes
        self.p_age       = self.smart_age()
        self.p_fname     = ran_gen.rfname(self.p_race)
        self.p_lname     = ran_gen.rlname(self.p_race)
        self.p_name      = self.p_fname + " " + self.p_lname
        
        #financial
        self.p_net_worth = ran_gen.rwealth()
        self.p_wea_desc  = ran_gen.get_wealth_desc(self.p_net_worth)
        
        #stats
        self.str = stat_gen()
        self.dex = stat_gen()
        self.con = stat_gen()
        self.wis = stat_gen()
        self.int = stat_gen()
        self.cha = stat_gen()
        
    def logical_stereotype(self):
        """
            Helps normalize stereotypical alignment and class based 
            on race according to the 5th edition PHB
        """
        
        if self.p_race != "Human":
            # pot_aligns = get_pot_aligns(self.p_race)
            pot_aligns = get_class_ster_nums(self.p_race, "pot_aligns", 1, \
                        True)
            pot_alig_nums = get_class_ster_nums(self.p_race, "pot_alig_nums", \
                        2, True)
            class_nums = get_class_ster_nums(self.p_race, "class_nums", 1, \
                        True)
            pot_classes = get_class_ster_nums(self.p_race, "pot_classes", 1, \
                        False)
            
            ster_align = die.rolld(100)    # sterotypical alignment %
            ster_class = die.rolld(100)    # stereotypical class %
                
            for i in range(len(pot_aligns)):
                if ster_align <= pot_aligns[i]:
                    self.p_alig_val[0] = pot_alig_nums[i][0]
                    self.p_alig_val[1] = pot_alig_nums[i][1]
                    
                    for j in range(len(class_nums)):
                        if ster_class <= class_nums[j]:
                            self.p_class = pot_classes[j]
                            break
                    break
        
        self.p_alignment = get_alig(self.p_alig_val)
            
    def smart_age(self):
        """
            Give character an appropriate age for given race
            Max age taken from 5th edition PHB, or D&D Beyond if not
            listed in PHB
        """
        
        r = die.rolld(100) # random percentage
        r_a_mod = random.randrange(86, 99) / 100 # age modifier
        
        # the following are ordered according to dnd_world
        maxa = [433, 845, 167, 98, 94, 522, 222, 80, 102] # max ages
        aa = [17, 17, 17, 17, 15, 20, 17, 16, 17] # adulthood ages
        r_a_check = [.74, .88, .85, .85, .70, .82, .88, .79, .82] # age check
        alter_chance = [89, 89, 89, 89, 85, 89, 89, 82, 89] # age alter chance
        
        for i in range(len(World.RACES.value)):
            if self.p_race == World.RACES.value[i]:
                age = die.rolld(maxa[i] - aa[i]) + aa[i]
                if age >= int(r_a_check[i] * maxa[i]) and r < alter_chance[i]:
                    age = int(age * r_a_mod)
                break
        
        return age
   
    def smart_wealth(self):
        'Make a somewhat logical attempt at calculating wealth'
        
        # these are arbitrary
        w_thresh = [100, 1150, 3700, 6800, 11000]
        w_brackets = [9.2, 50, 98.2, 99.6, 100]
        
        # ordered according to World
        w_mod = [1.08, 1.02, 1.01, 1.00, 1.02, 1.08, 1.02, .98, 1.03]
        
        p = round(random.uniform(0, 100), 2)
        rich_luck = random.uniform(0, 100)
        rl_mod = round(random.uniform(1.2, 2), 2)
        
        for i in range(len(w_brackets)):
            if p <= w_brackets[i]:
                if w_brackets[i] == w_brackets[0]:
                    self.p_net_worth = random.randint(1, w_thresh[i])
                    break
                else:
                    self.p_net_worth = random.randint(w_thresh[i-1], \
                        w_thresh[i])
                    if w_brackets[i] == w_brackets[-1] and rich_luck > 90:
                        self.p_net_worth = int(self.p_net_worth * rl_mod)
                    break
            
        for i in range(len(World.RACES.value)):
            if self.p_race == World.RACES.value[i]:
                self.p_net_worth = int(self.p_net_worth * w_mod[i])
                break
        
        # wealth descs not used for now
        self.p_wea_desc = ran_gen.get_wealth_desc(self.p_net_worth)
    
    def smart_stats(self):
        "Optimizes stats based on class based on 5th edition PHB"
        ph = [self.str, self.dex, self.con, self.wis, self.int, self.cha]
        ph.sort()
        ph.reverse()
        p = random.randint(1, 100)
        
        for perc, stats in World.ST_PERM.value[self.p_class].items():
            if p <= perc:
                for st_name, st_pos in stats.items():
                    setattr(self, st_name, ph[st_pos])
                break
            break
