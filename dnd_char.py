#!/usr/bin/python

##imports
import random
import ran_gen
import die
import dnd_world

##functions
def stat_gen() : 
    "Roll 4d6, drop the lowest, return total sum"
    
    rolls = [die.rolld(6), die.rolld(6), die.rolld(6), die.rolld(6)]
    rolls.remove(min(rolls))
            
    return sum(rolls)

def get_alig(alig_list) :
    '''
        First   [0] is lawful, neutral, chaotic
        Second  [1] is good, neutral, evil
    '''
    
    alignment = ""
    if alig_list[0] == 1 : 
        alignment = alignment + "Lawful"
    elif alig_list[0] == 2 : 
        alignment = alignment + "Neutral"
    else : 
        alignment = alignment + "Chaotic"
        
    if alig_list[1] == 1 : 
        alignment = alignment + " Good"
    elif alig_list[1] == 2 : 
        alignment = alignment + " Neutral"
    else : 
        alignment = alignment + " Evil"
        
    if alig_list[0] == 2 and alig_list[1] == 2 :
        alignment = "True Neutral"

    return alignment

def get_wealth_desc(w) : 
        "Return a random description of the character's appearance (GP based)"
        
        if w <= 100 :
            txt = open("wealth_descs/s_poor.txt", "r")
        elif w <= 1250 :
            txt = open("wealth_descs/poor.txt", "r")
        elif w <= 5800 :
            txt = open("wealth_descs/moderate.txt", "r")
        elif w <= 12500 :
            txt = open("wealth_descs/wealthy.txt", "r")
        elif w > 12500 :
            txt = open("wealth_descs/s_wealthy.txt", "r")
            
        pot_descs = txt.read().split(",   ")
        txt.close()
        
        return random.choice(pot_descs)
##body
class character :
    
    def __init__(self) :
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
        self.p_wea_desc  = get_wealth_desc(self.p_net_worth)
        
        #stats
        self.str = stat_gen()
        self.dex = stat_gen()
        self.con = stat_gen()
        self.wis = stat_gen()
        self.int = stat_gen()
        self.cha = stat_gen()
        
    def logical_stereotype(self) :
        '''
            Helps normalize stereotypical alignment and class based 
            on race according to the 5th edition PHB
        '''
        
        pot_aligns = []     # potential alignment %s
        pot_alig_nums = []  # alig nums based off of pot_aligns
        class_nums = []     # class % per race
        pot_classes = []    # potential classes
        
        ster_align = die.rolld(100)    # sterotypical alignment %
        ster_class = die.rolld(100)    # stereotypical class %
    
        if self.p_race == "Dwarf" :
            pot_aligns = [98]
            pot_alig_nums = [[1, 1]]
            class_nums = [48, 96]
            pot_classes = ["Fighter", "Barbarian"]
                            
        elif self.p_race == "Elf" :
            pot_aligns = [88]
            pot_alig_nums = [[3, 1]]
            class_nums = [32, 48, 68, 80, 96]
            pot_classes = ["Ranger", "Sorcerer", "Cleric", "Wizard", "Rogue"]
            
        elif self.p_race == "Halfling" :
            pot_aligns = [97]
            pot_alig_nums = [[1, 1]]
            class_nums = [25, 48, 82, 92]
            pot_classes = ["Bard", "Rogue", "Cleric", "Monk"]
        
        elif self.p_race == "Dragonborn" :
            pot_aligns = [30, 60, 78, 96]
            pot_alig_nums = [[1, 1], [3, 1], [1, 3], [3, 3]]
            class_nums = [18, 32, 48, 58, 72, 88]
            pot_classes = ["Wizard", "Fighter", "Sorcerer", "Warlock", \
                           "Paladin", "Rogue"]
                
        elif self.p_race == "Gnome" :
            pot_aligns = [86, 98]
            pot_alig_nums = [[1, 1], [3, 1]]
            class_nums = [18, 42, 48, 58, 76, 88]
            pot_classes = ["Wizard", "Bard", "Sorcerer", "Warlock", \
                           "Paladin", "Rogue"]
                    
        elif self.p_race == "Half-Elf" : #numbers might need adjusting
            pot_aligns = [35, 70, 96]
            pot_alig_nums = [[1, 1], [2, 3], [3, 3]]
            class_nums = [22, 32, 48, 58, 72, 88]
            pot_classes = ["Wizard", "Fighter", "Sorcerer", "Warlock", \
                           "Paladin", "Rogue"]
                    
        elif self.p_race == "Half-Orc" : #numbers might need adjusting
            pot_aligns = [95]
            pot_alig_nums = [[3, 2]]
            class_nums = [40, 80, 90, 100]
            pot_classes = ["Barbarian", "Fighter", "Monk", "Paladin"]
                    
        elif self.p_race == "Tiefling" : #numbers might need adjusting
            pot_aligns = [85]
            pot_alig_nums = [[3, 3]]
            class_nums = [22, 32, 48, 58, 72, 88]
            pot_classes = ["Wizard", "Ranger", "Sorcerer", "Warlock", \
                           "Paladin", "Rogue"]
            
        for i in range(len(pot_aligns)) :
            if ster_align <= pot_aligns[i] :
                self.p_alig_val[0] = pot_alig_nums[i][0]
                self.p_alig_val[1] = pot_alig_nums[i][1]
                
                for j in range(len(class_nums)) :
                    if ster_class <= class_nums[j] :
                        self.p_class = pot_classes[j]
                        break
                break
        
        self.p_alignment = get_alig(self.p_alig_val)
            
    def smart_age(self) :
        '''
            Give character an appropriate age for given race
            Max age taken from 5th edition PHB, or D&D Beyond if not
            listed in PHB
        '''
        
        r = die.rolld(100) # random percentage
        r_a_mod = random.randrange(86, 99) / 100 # age modifier
        
        # the following are ordered according to dnd_world
        maxa = [433, 845, 167, 98, 94, 522, 222, 80, 102] # max ages
        aa = [17, 17, 17, 17, 15, 20, 17, 16, 17] # adulthood ages
        r_a_check = [.74, .88, .85, .85, .70, .82, .88, .79, .82] # age check
        alter_chance = [89, 89, 89, 89, 85, 89, 89, 82, 89] # age alter chance
        
        for i in range(len(dnd_world.races)) :
            if self.p_race == dnd_world.races[i] :
                age = die.rolld(maxa[i] - aa[i]) + aa[i]
                if age >= int(r_a_check[i] * maxa[i]) and r < alter_chance[i] :
                    age = int(age * r_a_mod)
                break
        
        return (age)
   
    def smart_wealth(self) :
        'Make a somewhat logical attempt at calculating wealth'
        
        th_s_poor = 100
        th_poor = 1250 - th_s_poor
        th_mod = 5800 - th_poor
        th_wea = 12500 - th_mod
        th_s_wea = 15000 - th_wea
        p = round(random.uniform(0, 100), 2)
        
        # ordered according to dnd_world
        w_mod = [1.08, 1.02, 1.01, 1.00, 1.02, 1.08, 1.02, .98, 1.03]
        
        rand = random.random()
        
        if p <= 9.2 :
            self.p_net_worth = int(rand * 100)
        elif p > 9.2 and p <= 50 :
            self.p_net_worth = int(rand * random.randrange(1, th_poor)) + 100
        elif p > 50 and p <= 98.2 :
            self.p_net_worth = int(rand * random.randrange(1, th_mod)) + 1250
        elif p > 98.2 and p <= 99.6 :
            self.p_net_worth = int(rand * random.randrange(1, th_wea)) + 5800
        elif p > 99.6 :
            self.p_net_worth = int(rand * random.randrange(1, th_s_wea)) + 9200
            
        for i in range(len(dnd_world.races)) :
            if self.p_race == dnd_world.races[i] :
                self.p_net_worth = int(self.p_net_worth * w_mod[i])
                break
                
        # wealth descs not used for now
        self.p_wea_desc = get_wealth_desc(self.p_net_worth)
    
    def smart_stats(self) :
        "Optimizes stats based on class based on 5th edition PHB"
        ph = [self.str, self.dex, self.con, self.wis, self.int, self.cha]
        ph.sort()
        ph.reverse()
        p = die.rolld(100)
        
        if self.p_class == "Barbarian" :
            if p <=50 :
                self.str = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.cha = ph[3]
                self.int = ph[4]
                self.wis = ph[5]
            else :
                self.str = ph[0]
                self.con = ph[1]
                self.cha = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.wis = ph[5]
            
        elif self.p_class == "Bard" :
            self.cha = ph[0]
            self.dex = ph[1]
            self.wis = ph[2]
            self.con = ph[3]
            self.int = ph[4]
            self.str = ph[5]
            
        elif self.p_class == "Cleric" :
            if p <= 50 :
                self.wis = ph[0]
                self.str = ph[1]
                self.con = ph[2]
                self.dex = ph[3]
                self.cha = ph[4]
                self.int = ph[5]
            else :
                self.wis = ph[0]
                self.con = ph[1]
                self.str = ph[2]
                self.dex = ph[3]
                self.cha = ph[4]
                self.int = ph[5]
            
        elif self.p_class == "Druid" :
            self.wis = ph[0]
            self.con = ph[1]
            self.dex = ph[2]
            self.cha = ph[3]
            self.int = ph[4]
            self.str = ph[5]
            
        elif self.p_class == "Fighter" :
            if p <= 46 :
                self.str = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.cha = ph[4]
                self.int = ph[5]
            elif p > 46 and p <= 92 :
                self.dex = ph[0]
                self.con = ph[1]
                self.wis = ph[2]
                self.cha = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else :
                self.int = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.str = ph[4]
                self.cha = ph[5]
                
            
        elif self.p_class == "Monk" :
            self.dex = ph[0]
            self.wis = ph[1]
            self.con = ph[2]
            self.cha = ph[3]
            self.int = ph[4]
            self.str = ph[5]
            
        elif self.p_class == "Paladin" :
            if p <= 50 : 
                self.str = ph[0]
                self.cha = ph[1]
                self.wis = ph[2]
                self.dex = ph[3]
                self.con = ph[4]
                self.int = ph[5]
            else :
                self.str = ph[0]
                self.cha = ph[1]
                self.con = ph[2]
                self.dex = ph[3]
                self.wis = ph[4]
                self.int = ph[5]
            
        elif self.p_class == "Ranger" :
            if p <= 92 :
                self.dex = ph[0]
                self.wis = ph[1]
                self.con = ph[2]
                self.str = ph[3]
                self.int = ph[4]
                self.cha = ph[5]
            else :
                self.str = ph[0]
                self.wis = ph[1]
                self.con = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.cha = ph[5]
            
        elif self.p_class == "Rogue" :
            if p <= 50 :
                self.dex = ph[0]
                self.cha = ph[1]
                self.con = ph[2]
                self.wis = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else :
                self.dex = ph[0]
                self.int = ph[1]
                self.con = ph[2]
                self.wis = ph[3]
                self.cha = ph[4]
                self.str = ph[5]
            
        elif self.p_class == "Sorcerer" :
            if p <= 50 :
                self.cha = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else :
                self.cha = ph[0]
                self.con = ph[1]
                self.wis = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            
        elif self.p_class == "Wizard" :
            if p <= 50 :
                self.int = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.str = ph[4]
                self.cha = ph[5]
            elif p > 50 and p <= 66 :
                self.int = ph[0]
                self.dex = ph[1]
                self.con = ph[2]
                self.wis = ph[3]
                self.str = ph[4]
                self.cha = ph[5]
            else :
                self.int = ph[0]
                self.dex = ph[1]
                self.wis = ph[2]
                self.con = ph[3]
                self.str = ph[4]
                self.cha = ph[5]
                
        elif self.p_class == "Warlock" :
            if p <= 50 :
                self.cha = ph[0]
                self.con = ph[1]
                self.dex = ph[2]
                self.wis = ph[3]
                self.int = ph[4]
                self.str = ph[5]
            else :
                self.cha = ph[0]
                self.con = ph[1]
                self.wis = ph[2]
                self.dex = ph[3]
                self.int = ph[4]
                self.str = ph[5]
