#!/usr/bin/python

# imports
from dnd_char import character

# functions
def beautify(s): print(f"\n\n{s}\n\n")
def alert(s): beautify("      " + s)

def menu():
    "Display menu options"
    
    print(" 1| Generate New Logical Character")
    print(" 2| Generate New Random Character")
    print("-----------------------------------")
    print(" 8| Save Character To File")
    print(" 9| Print Stats of Current Character")
    print("-1| Exit Program")
    print("-----------------------------------")

def req_input():
    "Request an int for input"
    
    print("Enter a number (0 for menu): ", end = "")
    ina = int(input())
    return ina
    
def save_char(c):
    "Save character to text file"
    
    file_name = f"{c.p_race} {c.p_class} - {c.p_name}.txt"
    savepath  = "./characters/" + file_name
    current   = "./current_character.txt"
    files     = [savepath, current]
    
    for a_file in files:
        file = open(a_file, 'w')
        file.write(print_desc(c))
        file.close()
    
    alert(f"'{file_name}' saved in characters folder")
    
def make_log_character():
    "Generate character based on 5e PHB logic"
    
    new = character()
    new.logical_stereotype()
    new.smart_stats()
    new.smart_wealth()
    return new

def make_ran_character():
    "Generate character randomly"
    
    new = character()
    return new

def format_desc(c):
    stats = [c.str, c.dex, c.con, c.wis, c.int, c.cha]
    form = []
    ind = "                      "
    
    for stat in stats:
        if stat < 10:
            form.append(str(stat).rjust(2, ' '))
        else:
            form.append(stat)
            
    res = f"\n {ind}|     STR {form[0]}     WIS {form[3]}     |" \
          f"\n {ind}|     DEX {form[1]}     INT {form[4]}     |" \
          f"\n {ind}|     CON {form[2]}     CHA {form[5]}     |"
    
    if c.p_race == "Elf": grammar = "an"
    else: grammar = "a"
      
    return [grammar, res]

def print_desc(c):
    "Display a brief, cleanly-formatted description of generated character"
    
    #format description with proper grammar
    formatted = format_desc(c)
    stats = formatted[1]
    char_id = f"This person is {formatted[0]} {c.p_race} {c.p_class} " \
              f"whose name is {c.p_name}."
    desc = f"\n{c.p_fname} is {c.p_alignment}, is {c.p_age} years old, and " \
           f"has a net worth of {c.p_net_worth} GP."
    breaker = "- - - - - - - - - - - - - - - - - -" + \
              " - - - - - - - - - - - - - - - - - - - - - -"
    result = f"{char_id}{desc}\n{breaker}{stats}\n{breaker}"
           
    return result
# body

cont  = 0
has_saved = False
char_made = False
curr  = character()

print("\n")
menu()

while cont >= 0:
    cont = req_input()
    
    if cont == 1:
        "Make logical char, display stats, and reset saved stat"
        curr = make_log_character()
        beautify(print_desc(curr))
        has_saved = False
        char_made = True
        
    elif cont == 2: 
        "Make random char, display stats, and reset saved stat"
        curr = make_ran_character()
        beautify(print_desc(curr))
        has_saved = False
        char_made = True
        
    elif cont == 8: 
        "Display errors w/ saving"
        if char_made == False:
            alert("ERROR: Generate character before saving.")
        elif has_saved == True:
            alert("ERROR: Character has already been saved.")
        else: 
            has_saved = True
            save_char(curr)
        
    elif cont == 9:
        "Print stats if character has been generated"
        if char_made == False:
            alert("ERROR: Generate character before attempting to view their stats.")
        else:
            beautify(print_desc(curr))
            
    elif cont == 0:
        menu()

print("\n")
