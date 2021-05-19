# dnd_5e_character_generator
A tool for generating 5th edition Dungeons & Dragons characters

# 18 May 2021
##### New
- Shield functionality

##### Changed
- Armor generation now utilizes configs
- Made a cleaner format for displaying the description of the character to the user

##### Planned
- More realistic descriptions of wealth
- Differentiate between one-hand and two-hand weapons
  - For shielded weapons (you can't use shields if you have both of your hands occupied)

# 9 May 2021
##### New
- Added option to logically make a character based on race 
  - No need to make potentially dozens of characters to get a character with the race you wanted

##### Changed
- Screen clearing utilizes escape characters instead of importing an entire library to do so
- Deepcopy used for armor generation to prevent possible edge-case scenarios resulting in segfaults

##### Planned
- ~~Change armor generation to use configs~~
- ~~Make a cleaner format for displaying the description of the character to the user~~
- More realistic descriptions of wealth
- ~~Implement shield functionality that was added recently~~

# 14 Apr. 2021
Gear generation has been added. For ease of legibility, screen clearing has been added. Basic boundary-testing has been added. The enum CL_GEAR_STER in dnd_world.py will probably be moved to using configs in the future.

I haven't yet incorporated the addition of shields. The underlying code is in dnd_world.py, but hasn't yet been added. All other gear generation is working fine, but could probably be improved in some way.

# 9 Apr. 2021
Now that most of the initial code has been cleaned up and organized, gear generation and descriptions are planned, but there is no set time. Again, this is just a project for when I'm bored and feel like learning new things :D

##### R.I.P. DMX

# 15 Mar. 2021
In the future I might fix/add a system for adding descriptions based on wealth and clothing/armor/gear worn.

It should be noted that this was my foray into python programming and was my quarantine project for a week or so in the summer of last year. It's probably very sloppy. I'm just looking for constructive feedback, be it negative or positive.
