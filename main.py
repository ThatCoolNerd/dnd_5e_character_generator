#!/usr/bin/python

##imports
from dnd_char import character
from dnd_char import stat_gen

import die

##functions
def menu() :
    "Display menu options"
    
    print(" 1| Generate New Logical Character")
    print(" 2| Generate New Random Character")
    print("-----------------------------------")
    print(" 8| Save Character To File")
    print(" 9| Print Stats of Current Character")
    print("-1| Exit Program")
    print("-----------------------------------")

def req_input() :
    "Get an int for input"
    
    print("Enter a number (0 for menu): ", end = "")
    ina = int(input())
    return ina
    
def beautify(s) :
    "Easier to read text formatting"
    
    print()
    print()
    print(s)
    print()
    print()
    
def alert(s) : beautify("      " + s)

def save_char(c) :
    "Save character to text file"
    
    file_name = c.p_race + " " + c.p_class + " - " + c.p_name + ".txt"
    savepath  = "./characters/" + file_name
    current   = "./current_character.txt"
    
    file = open(savepath, 'w')
    file.write(print_desc(c))
    file.close()
    
    file = open(current, 'w')
    file.write(print_desc(c))
    file.close()
    
    alert("'" + file_name + "' saved in characters folder")
    
def make_log_character() :
    "Generate character based on 5e PHB logic"
    
    new = character()
    new.logical_stereotype()
    new.smart_stats()
    new.smart_wealth()
    return new

def make_ran_character() :
    "Generate character randomly"
    
    new = character()
    return new

def print_desc(c) :
    "Display a brief, cleanly-formatted description of generated character"
    
    #format description with proper grammar
    if c.p_race == "Elf" :
        char_id   = "This person is an " + c.p_race + " " + \
            c.p_class + " whose name is " + c.p_name + "."
    else :
        char_id   = "This person is a " + c.p_race + " " + \
            c.p_class + " whose name is " + c.p_name + "."
    
    desc = "\n" + c.p_fname + " is " + c.p_alignment + ", is " + \
        str(c.p_age) + " years old, and has a net worth of " + \
        str(c.p_net_worth) + " GP."
          
    #wea = c.p_fname + " " + c.p_wea_desc
    #wealth descriptions have been removed from this version
    
    breaker = "- - - - - - - - - - - - - - - - - -" + \
              " - - - - - - - - - - - - - - - - - - - - - -"
    ind = "                      "
    
    #convert stats to text & format appropriately
    stre = str(c.str)
    dex  = str(c.dex)
    con  = str(c.con)
    wis  = str(c.wis)
    int  = str(c.int)
    cha  = str(c.cha)
    
    if c.str < 10 :
        stre = " " + stre
    
    if c.dex < 10 :
        dex = " " + dex
        
    if c.con < 10 :
        con = " " + con
        
    if c.wis < 10 :
        wis = " " + wis
        
    if c.int < 10 :
        int = " " + int
        
    if c.cha < 10 :
        cha = " " + cha
        
    stats = "\n"+  ind + "|     STR " + stre + "     WIS " + wis + "     |\n"+\
            ind + "|     DEX " + dex  + "     INT " + int + "     |\n"+\
            ind + "|     CON " + con  + "     CHA " + cha + "     |"
    
    #return (char_id + "\n" + desc + "\n" + breaker + stats + \
           #"\n" + breaker + wea)
    #wealth descriptions have been removed from this version
           
    return (char_id + desc + "\n" + breaker + stats + \
        "\n" + breaker)
##body

cont  = 0
count = 0
has_saved = False
curr  = character()

print()
print()
menu()

while cont >= 0 :
    cont = req_input()
    
    if cont == 1 :
        "Make logical char, display stats, and reset saved stat"
        curr = make_log_character()
        beautify(print_desc(curr))
        has_saved = False
        count += 1
        
    elif cont == 2 : 
        "Make random char, display stats, and reset saved stat"
        curr = make_ran_character()
        beautify(print_desc(curr))
        has_saved = False
        count += 1
        
    elif cont == 8 : 
        "Display errors w/ saving"
        if count == 0 :
            alert("ERROR: Generate character before saving.")
        elif has_saved == True :
            alert("ERROR: Character has already been saved.")
        else: 
            has_saved = True
            save_char(curr)
        
    elif cont == 9 :
        "Print stats if character has been generated"
        if count == 0 :
            alert("ERROR: Generate character before attempting to view their stats.")
        else :
            beautify(print_desc(curr))
            
    elif cont == 0 :
        menu()

print()
print()
