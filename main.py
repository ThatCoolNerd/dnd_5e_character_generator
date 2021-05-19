#!/usr/bin/python

# imports
from textwrap import wrap
from dnd_char import character
from dnd_world import World
from time import sleep

# functions
def clear(): print('\033[H\033[J', end="")
def beautify(s): print(f"\n\n{s}\n\n")
def alert(s): beautify(f"       {s}")
def req_input(): return int(input())

def menu():
    "Display menu options"
    print(" 1| Generate New Logical Character")
    print(" 2| Generate New Random Character")
    print(" 3| Generate Character Of Certain Race")
    print("-----------------------------------")
    print(" 8| Save Character To File")
    print(" 9| Print Stats of Current Character")
    print("-1| Exit Program")
    print("-----------------------------------")
    
def display_races():
    "Display races in D&D"
    r_ph = "\n\n"
    for i in range(len(World.RACES.value)):
        r_ph += f"   {i+1}| {World.RACES.value[i]}\n"
    print(f"{r_ph}\n")
    
def display_classes():
    "Display classes in D&D"
    c_ph = "\n\n"
    for i in range(len(World.CLASSES.value)):
        c_ph += f"   {i+1}| {World.CLASSES.value[i]}\n"
    print(f"{c_ph}\n")

def prompt(s):
    print(s, end="")
    return req_input()
    
def save_char(c, char_made, has_saved):
    "Save character to text file"
    
    if char_made == False:
        alert("ERROR: Generate character before saving.")
    elif has_saved == True:
        alert("ERROR: Character has already been saved.")
        return True
    else: 
        file_name = f"{c.p_race} {c.p_class} - {c.p_name}.txt"
        savepath  = "./characters/" + file_name
        current   = "./current_character.txt"
        files     = [savepath, current]
        
        for a_file in files:
            file = open(a_file, 'w')
            file.write(print_desc(c))
            file.close()
        
        alert(f"'{file_name}' saved in characters folder")
        
        return True
    
def make_log_character(*r):
    "Generate character based on 5e PHB logic"
    new = character()
    if len(r) > 0: new.logical_stereotype(r[0])
    else: new.logical_stereotype()
    new.smart_stats()
    new.smart_wealth()
    new.smart_gear()
    
    print("- - - - GENERATED LOGICAL CHARACTER - - - -".center(80, ' '))
    print(f"{print_desc(new)}\n")
    
    return new

def make_ran_character():
    "Generate character randomly"
    new = character()
    print("- - - - GENERATED RANDOM CHARACTER - - - -".center(80, ' '))
    print(f"{print_desc(new)}\n")
    return new

def format_desc(c):
    "Extra formatting for descriptions"
    stats = [c.str, c.dex, c.con, c.wis, c.int, c.cha]
    form = []
    ind = "                       "
    
    for stat in stats:
        if stat < 10:
            form.append(str(stat).rjust(2, ' '))
        else:
            form.append(stat)
            
    res = f" {ind}|     STR {form[0]}     WIS {form[3]}     |" \
          f"\n {ind}|     DEX {form[1]}     INT {form[4]}     |" \
          f"\n {ind}|     CON {form[2]}     CHA {form[5]}     |"
    
    if c.p_race == "Elf": grammar = "an"
    else: grammar = "a"
    
    if "Dart" in c.p_weapon:
        weapon = "a handful of darts"
    else: weapon = "a " + c.p_weapon
      
    return [res, weapon, grammar]

def print_desc(c):
    "Display a brief, cleanly-formatted description of generated character"
    formatted = format_desc(c)
    stats = formatted[0]
    weapon = formatted[1]
    return_list = []
    char_id = f"This person is {formatted[2]} {c.p_race} {c.p_class} " \
        f"whose name is {c.p_name}."
    desc = f"{c.p_fname} is {c.p_alignment}, {c.p_age} years old, and " \
        "has a net worth of {:,d} GP.".format(c.p_net_worth)
    breaker = "".center(80, '-')
    appearance = f"{c.p_fname} is wearing {c.p_clothing}, and {c.p_wea_desc}"
    armed = f"{c.p_fname} is wielding {weapon}."
    
    desc_dict = {
        "   Description: ": desc,
        "   Appearance : ": appearance,
        "   Wielding   : ": armed
    }
    
    return_list.append("\n\n\n" + char_id.center(80, ' '))
    return_list.append(f"{breaker}\n{stats}\n{breaker}\n")
    for key, val in desc_dict.items():
        wrapped = wrap(f"{key}{val}", 77)
        return_list.append(wrapped[0])
        if len(wrapped) > 0:
            for i in range(len(wrapped)-1):
                return_list.append("".ljust(len(key), ' ') + wrapped[i+1])
        return_list[-1] += "\n"
    
    return_string = ""
    for line in return_list:
        return_string += (line + "\n")
    return(return_string)

# body
clear()
cont = 1
has_saved = False
char_made = False
debug_count = 500
curr = character()

while cont >= 0:
    cont = prompt("Enter a number (0 for menu): ")
    clear()
    
    if cont == 1:
        "Make logical char, display stats, and reset saved stat"
        curr = make_log_character()
        has_saved = False
        char_made = True
        
    elif cont == 2: 
        "Make random char, display stats, and reset saved stat"
        curr = make_ran_character()
        has_saved = False
        char_made = True
        
    elif cont == 3: 
        "Make char with a given race"
        display_races()
        selected_race = prompt("Choose a race: ")
        if selected_race == 0:
            clear()
            pass
        else:
            clear()
            curr = make_log_character(World.RACES.value[selected_race-1])
        
    elif cont == 8: 
        "Display errors w/ saving"
        has_saved = save_char(curr, char_made, has_saved)
        
    elif cont == 9:
        "Print stats if character has been generated"
        if char_made == False:
            alert("ERROR: Generate character before attempting to view their stats.")
        else:
            print(f"{print_desc(curr)}\n")
            
    elif cont == 111:
        for i in range(debug_count):
            print(f"DEBUG MODE (LOG) ({i} of {debug_count})".center(80, '-'))
            curr = make_log_character()
            sleep(.01)
            clear()
        has_saved = False
        char_made = True
        alert("CHAR GEN SUCCESSFUL - NO BUGS")
            
    elif cont == 222:
        for i in range(debug_count):
            print(f"DEBUG MODE (RAN) ({i} of {debug_count})".center(80, '-'))
            curr = make_ran_character()
            sleep(.01)
            clear()
        has_saved = False
        char_made = True
        alert("CHAR GEN SUCCESSFUL - NO BUGS")
        
    elif cont == 0:
        menu()

clear()
