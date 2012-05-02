#!/usr/bin/env python

# GAME

#####################
import pickle
import player # player class definitions
import cg2 # character generator script v2

import combat
from combat import *

from cg2 import *
from player import PC
#####################

############## CREDITS

title_msg = """
From the Hampshire College Press
a survival roleplaying game called

PEAK

Copyright Matthew Meneghini and Matthew Pink 2012
"""
print title_msg
######################

# THIS IS THE BACKGROUND STORY
msg ="""
The date is January 13, 2014.  
It is cold....very cold.

You wake up and head to the bathroom.  There, you see a face in the mirror.
Your face.
""" 

##
# LOADER
h_msg ="""
Letter  | Command
c       | Continue Game
l       | Load Game | COMING SOON
n       | New Game | COMING SOON
q       | Quit
h       | Help
r       | Credits
"""
print h_msg

done = False
while not done:
    tprompt = raw_input("input a command: ")
    if tprompt.lower() in ['l','load','save']:
        load_instance.loadGame()
        print load_instance.name
    elif tprompt.lower() in ['n','new','new game']:
        print msg
        charGen() # CHARACTER CREATION
        done = True
    elif tprompt.lower() in ['c','continue']:
        print "One of your neighbors attacks!  Time to fight!"
        fight()
    elif tprompt.lower() in ['r','credits']:
        print title_msg
    elif tprompt.lower() in ['q','quit']:
        print "goodbye!"
        done = True
    else:
        print h_msg

######################

"""
Loader script must do the following:  set the game to run 

"""
# IN-GAME MOVEMENT
# FROM NEW GAME
print "you are attacked by a wolf!  Time for battle!"

# FROM SAVED GAME

# COMBAT ENCOUNTER


#### AMBUSH!!!!
