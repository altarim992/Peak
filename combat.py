#!/usr/bin/env python

# python modules
import os
from os.path import abspath, dirname
import pickle
import random
import pygame
from pygame.locals import *

# game modules
import player
from player import PC
import cg2
from cg2 import load_instance
from cg2 import loadThings
import enemies
from enemies import NPC
import w2
from w2 import *
import bfield
from bfield import *

ROOT_DIR = dirname(abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "combat")

baddie = NPC("Paul Renier",19,14,12,"alive") # loader for enemy.  Long-term, this will be defined by an outside loader function

loadThings() # opens and loads relevant save file

#####################################
# FIGHTING SHELL
#####################################

fl1 = """
this is the fighting shell
h   | help
l   | list weapons
a   | attack
q   | quit
"""

fl2 = """
Available Attacks:
-------------------
1   | Hack  | basic attack
2   | Sweep | lowers speed
3   | Slash | moderate attack
4   | Stun  | lowers mental
"""

def fight():    # this is the fight menu
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    colorkey = (255,255,255)
    background = pygame.image.load(os.path.join(DATA_DIR, "shed.png")).convert()
    pc_img = pygame.image.load(os.path.join(DATA_DIR, "player.png")).convert()
    pc_img.set_colorkey(colorkey)
    enemy_img = pygame.image.load(os.path.join(DATA_DIR, "wolf2.png")).convert()
    enemy_img.set_colorkey(colorkey)
    menu = pygame.Rect((450,375), (350,325))
    textbox = pygame.Rect((0,375), (450,325))
    menufont = pygame.font.Font(None, 36)
    statusfont = pygame.font.Font(None, 24)
    statustext = statusfont.render("Your turn. What will you do?", True, (0,0,0))
    mainmenu = [menufont.render("1. Attack", True, (0,0,0)),
                menufont.render("2. List Weapons", True, (0,0,0)),
                menufont.render("3. Help", True, (0,0,0)),
                menufont.render("4. Quit", True, (0,0,0))
                ]
    atkmenu = [menufont.render("1. Hack", True, (0,0,0)),
                menufont.render("2. Sweep", True, (0,0,0)),
                menufont.render("3. Slash", True, (0,0,0)),
                menufont.render("4. Stun", True, (0,0,0))
                ]
    listmenu = menufont.render("1. Return", True, (0,0,0))
    fps = 30
    clock = pygame.time.Clock()

    #fight loop
    global fighting
    fighting = True
    turn = 1
    while fighting:
        screen.fill((255,255,255))
        screen.blit(background, screen.get_rect())
        screen.blit(pc_img, screen.get_rect())
        screen.blit(enemy_img, (500,125))

        #Status Text
        screen.fill((255,255,255), textbox)
        screen.blit(statustext, (25,400))

        #Menu Text
        x = 500
        y = 400
        screen.fill((255,255,255), menu)
        for option in range(4):
            menutext = mainmenu[:]
            screen.blit(menutext[option], (x,y))
            y = y + 50

        pygame.display.flip()
        clock.tick(fps)
        pct.refresh() # wipe the damage qeues clear
        nct.refresh()
        infoGraphic() # display stats
        checkWin2() # checks to see if fight is over
        for event in pygame.event.get():
            if event.type == QUIT:
                fighting = False
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                fighting = False
                pygame.quit()

############################
#Attack
############################
            elif event.type == KEYDOWN and event.key == K_1:
                atkphase = True
                while atkphase:
                    screen.fill((255,255,255), textbox)
                    screen.fill((255,255,255), menu)
                    menutext = atkmenu[:]
                    statustext = statusfont.render("What attack?", True, (0,0,0))
                    y = 400
                    for atk in range(4):
                        screen.blit(menutext[atk], (x,y))
                        y = y + 50
                    screen.blit(statustext, (25,400))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            atkphase = False
                            fighting = False
                            pygame.quit()
                        elif event.type == KEYDOWN and event.key == K_ESCAPE:
                            atkphase = False
                            fighting = False
                            pygame.quit()
                        elif event.type == KEYDOWN and event.key == K_1:
                            hack()
                            atkphase = False
                        elif event.type == KEYDOWN and event.key == K_2:
                            sweep()
                            atkphase = False
                        elif event.type == KEYDOWN and event.key == K_3:
                            slash()
                            atkphase = False
                        elif event.type == KEYDOWN and event.key == K_4:
                            stun()
                            atkphase = False
########################
#End attack
########################
#List weapons
########################
            elif event.type == KEYDOWN and event.key == K_2:
                listphase = True
                while listphase:
                    screen.fill((255,255,255), textbox)
                    screen.fill((255,255,255), menu)
                    menutext = listmenu
                    statustext = statusfont.render("You have an axe.", True, (0,0,0))
                    screen.blit(menutext, (500,400))
                    screen.blit(statustext, (25, 400))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            listphase = False
                            fighting = False
                            pygame.quit()
                        elif event.type == KEYDOWN and event.key == K_ESCAPE:
                            listphase = False
                            fighting = False
                            pygame.quit()
                        elif event.type == KEYDOWN and event.key == K_1:
                            listphase = False
#####################
#End list weapons
#####################
#Help
#####################
            elif event.type == KEYDOWN and event.key == K_3:
                helpphase = True
                while helpphase:
                    screen.fill((255,255,255), textbox)
                    screen.fill((255,255,255), menu)
                    menutext = listmenu
                    statustext = statusfont.render("Nothing here yet =/", True, (0,0,0))
                    screen.blit(menutext, (500,400))
                    screen.blit(statustext, (25, 400))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            helpphase = False
                            fighting = False
                            pygame.quit()
                        elif event.type == KEYDOWN and event.key == K_1:
                            helpphase = False
######################
#End help
######################
#Quit
######################
            elif event.type == KEYDOWN and event.key == K_4:
                fighting = False
                pygame.quit()
######################
#End quit
######################
        hurtBad() # deals damage to the bad guy
        turn += 1
        checkWin2() # checks to see if the fight is over
        flipCoin() # decides which attack enemy will use
        hurtMe() # deals damage to player character

                        
'''
        fshell = raw_input("Your turn - Fight> ")
        fshell = str(fshell)
# in the end, this will include a loader function for known attacks.  At the moment, it will simply have hardcoded attacks
        if fshell.lower() in ['h','help']:
            print fl1
        elif fshell.lower() in ['l','list']:
            print "you have an axe"
            print "your enemy has a rifle"
            print fl2
        elif fshell.lower() in ['q', 'quit','b','back']:
            fighting = False
        elif fshell.lower() in ['a']:
            atk_cmd = raw_input("Your turn - Fight - Attack> ")
            atk_cmd = int(atk_cmd)
            if atk_cmd == 1:
                hack()
            elif atk_cmd == 2:
                sweep()
            elif atk_cmd == 3:
                slash()
            elif atk_cmd == 4:
                stun()
            else:
                print fl2
        else:
             print fl1
'''


######################################
# FIGHT LOOP END
######################################

def checkWin2(): # checkWin 2
    global fighting
    baddie.checkSelf(baddie.physical,baddie.mental,baddie.spd)
    if baddie.status.lower() in ['dead']:
        fighting = False
        screen.fill((255,255,255), textbox)
        statustext = statusfont.render("You killed the enemy!", True, (0,0,0))
        screen.blit(statustext, (25,400))
        pygame.display.flip()
    elif baddie.status.lower() in ['faint']:
        fighting = False
        screen.fill((255,255,255), textbox)
        statustext = statusfont.render("You knocked out your enemy!", True, (0,0,0))
        screen.blit(statustext, (25,400))
        pygame.display.flip()
    elif baddie.status.lower() in ['tko']:
        fighting = False
        screen.fill((255,255,255), textbox)
        statustext = statusfont.render("You've incapacitated your enemy!", True, (0,0,0))
        screen.blit(statustext, (25,400))
        pygame.display.flip()

    pc.chkStatus(pc.physical,pc.mental,pc.spd)
    if pc.status.lower() in ['dead']:
        fighting = False
        screen.fill((255,255,255), textbox)
        statustext = statusfont.render("You died!", True, (0,0,0))
        screen.blit(statustext, (25,400))
        pygame.display.flip()
    elif pc.status.lower() in ['faint']:
        fighting = False
        screen.fill((255,255,255), textbox)
        statustext = statusfont.render("You fainted!", True, (0,0,0))
        screen.blit(statustext, (25,400))
        pygame.display.flip()
    elif pc.status.lower() in ['tko']:
        fighting = False
        screen.fill((255,255,255), textbox)
        statustext = statusfont.render("You're incapacitated and cannot defend yourself!", True, (0,0,0))
        screen.blit(statustext, (25,400))
        pygame.display.flip()

    return fighting

def infoGraphic():
    screen.fill((255,255,255), textbox)
    info = [
            statusfont.render("Your health: "+str(pc.physical), True, (0,0,0)),
            statusfont.render("Your mental: "+str(pc.mental), True, (0,0,0)),
            statusfont.render("Your speed: "+str(pc.spd), True, (0,0,0)),
            statusfont.render("Enemy health: "+str(baddie.physical), True, (0,0,0)),
            statusfont.render("Enemy mental: "+str(baddie.mental), True, (0,0,0)),
            statusfont.render("Enemy speed: "+str(baddie.spd), True, (0,0,0))
            ]
    x = 500
    y = 400
    for item in range(len(info)):
        screen.blit(info[item], (x,y))
        y = y + 25
    pygame.display.flip()
        
def hurtMe(): # this function transfers the damage from 'nct' to you, and invokes the nct.refresh() function
    pc.physical -= nct.phys
    pc.mental -= nct.mental
    pc.spd -= nct.speed

def hurtBad(): # this function transfers the damage from 'pct' to CURRENT_ENEMY
    baddie.physical -= pct.phys
    baddie.mental -= pct.mental
    baddie.spd -= pct.speed

############################################
# IMPORTANT COMBAT FUNCTIONS END
############################################

##############################
# ENEMY ATTACKS
##############################


def darkDmg(p_dmg,m_dmg,s_dmg): # needed until enemies have native attack functions
    nct.phys += p_dmg
    nct.mental += m_dmg
    nct.speed += s_dmg

def flipCoin():
    choice = random.randint(1,3)
    if choice == 1:
        ebShot()
    elif choice == 2:
        ehShot()
    else:
        eclub()

def ebShot(): # modified good guy attack function
    p_dmg = baddie.mental * 0.7 # body shot
    m_dmg = 0
    s_dmg = 0
    missBar = 70 + baddie.mental
    tgt = "you were shot with a rifle!"
    print tgt
    darkDmg(p_dmg,m_dmg,s_dmg)
    
def ehShot():
    p_dmg = baddie.mental * 1.2 
    m_dmg = 0
    s_dmg = 0
    missBar = 60 + baddie.mental
    tgt = "you were sniped with a rifle!"
    print tgt
    darkDmg(p_dmg,m_dmg,s_dmg)

def eclub():
    p_dmg = baddie.physical * 0.4 
    m_dmg = baddie.physical * 0.4
    s_dmg = 0
    missBar = 85 + baddie.physical
    tgt = "you got brained with a club!"
    print tgt
    darkDmg(p_dmg,m_dmg,s_dmg)
