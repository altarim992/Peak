#!/usr/bin/env python

# THIS IS v2.0 OF THE WEAPONS FILE

import bfield
from bfield import *

import player
from player import PC

import cg2
from cg2 import Loader,loadThings

import pickle

loadchr = open("save/pc/default.creature", "r+")
pc = pickle.load(loadchr)

# FEED DAMAGE TO bfield
def feedDmg(p_dmg,m_dmg,s_dmg):
    pct.phys += p_dmg
    pct.mental += m_dmg
    pct.speed += s_dmg
    
    

def sweep():
    p_dmg = pc.physical * 0.2 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = pc.physical * 0.4
    missBar = 95 + pc.physical
    tgt = "you used sweep"
    feedDmg(p_dmg,m_dmg,s_dmg)
    print tgt
    
def stab():
    p_dmg = pc.physical * 0.5 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = 0
    missBar = 85 + pc.mental
    tgt = "physical"
    feedDmg(p_dmg,m_dmg,s_dmg)

def swipe():
    p_dmg = pc.physical * 0.1 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = pc.mental * 0.3
    missBar = 80 + pc.mental
    tgt = "physical"
    feedDmg(p_dmg,m_dmg,s_dmg)

def spray():
    p_dmg = 0 # having trouble accessing from PC
    m_dmg = pc.mental * 0.4
    s_dmg = pc.mental * 0.3
    missBar = 75 + pc.physical
    tgt = "maced!"
    feedDmg(p_dmg,m_dmg,s_dmg)
    
def stun():
    p_dmg = pc.physical * 0.1 # having trouble accessing from PC
    m_dmg = pc.physical * 0.3
    s_dmg = pc.physical * 0.2
    missBar = 85 + pc.physical
    tgt = "you used stun!"
    feedDmg(p_dmg,m_dmg,s_dmg)
    print tgt

def jet():
    p_dmg = pc.mental * 0.1 # improved version of spray
    m_dmg = pc.mental * 0.5
    s_dmg = pc.mental * 0.4
    missBar = 70 + pc.mental
    tgt = "power maced!"
    feedDmg(p_dmg,m_dmg,s_dmg)
"""
def explode():
    p_dmg = pc.physical * 1.5 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = 0
    missBar = 85 + pc.physical
    tgt = "physical"
    feedDmg(p_dmg,m_dmg,s_dmg)
"""
def whack():
    p_dmg = pc.physical * 0.3 # whacked with a stick!
    m_dmg = 0
    s_dmg = 1
    missBar = 90 + pc.physical
    tgt = "whacked!"
    feedDmg(p_dmg,m_dmg,s_dmg)
    
def roundhouse():
    p_dmg = pc.physical * 0.2 # punched with fists
    m_dmg = pc.mental * 0.1
    s_dmg = 0
    missBar = 80 + pc.mental
    tgt = "slugged!"
    feedDmg(p_dmg,m_dmg,s_dmg)

def bShot():
    p_dmg = pc.mental * 0.7 # body shot
    m_dmg = 0
    s_dmg = 0
    missBar = 70 + pc.mental
    tgt = "shot!"
    feedDmg(p_dmg,m_dmg,s_dmg)
    
def hShot():
    p_dmg = pc.mental * 1.2 # Dad, would you put Mum on the phone...
    m_dmg = 0
    s_dmg = 0
    missBar = 60 + pc.mental
    tgt = "sniped"
    feedDmg(p_dmg,m_dmg,s_dmg)

def club():
    p_dmg = pc.physical * 0.4 # no dancing here, but it is skeevy.
    m_dmg = pc.physical * 0.4
    s_dmg = 0
    missBar = 85 + pc.physical
    tgt = "brained"
    feedDmg(p_dmg,m_dmg,s_dmg)

def iSlash():
    p_dmg = pc.physical * 0.3 + pc.mental * 0.3 # the new slash, with 20% more slash
    m_dmg = 0
    s_dmg = 0
    missBar = 90
    tgt = "visiously slashed"
    feedDmg(p_dmg,m_dmg,s_dmg)

def cSlash():
    p_dmg = pc.physical * 0.4 + pc.mental * 0.4 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = 0
    missBar = 95
    tgt = "savagely slashed"
    feedDmg(p_dmg,m_dmg,s_dmg)

def pin():
    p_dmg = 0 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = pc.physical * 0.6
    missBar = 75 + pc.physical
    tgt = "pinned"
    feedDmg(p_dmg,m_dmg,s_dmg)
    
def dismember():
    p_dmg = 3 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = 5
    missBar = 80 + pc.physical
    tgt = "crippled"
    feedDmg(p_dmg,m_dmg,s_dmg)

def hammer():
    p_dmg = pc.physical * 0.8 # having trouble accessing from PC
    m_dmg = pc.physical * 0.1
    s_dmg = pc.physical * 0.1
    missBar = 85 + pc.physical
    tgt = "smashed"
    feedDmg(p_dmg,m_dmg,s_dmg)
    
def test():
    p_dmg = 1
    m_dmg = 0
    s_dmg = 0
    feedDmg(p_dmg,m_dmg,s_dmg)

def hack():
    p_dmg = pc.physical * 0.5 # having trouble accessing from PC
    m_dmg = 0
    s_dmg = 0
    missBar = 85 + pc.physical
    tgt = "you used hack!"
    feedDmg(p_dmg,m_dmg,s_dmg)
    print tgt

def slash(): # trusty, trusty slash
    p_dmg = pc.physical * 0.2 + pc.mental * 0.2
    m_dmg = 0
    s_dmg = 1
    missBar = 50 + pc.physical + pc.mental
    tgt = "you used slash!"
    feedDmg(p_dmg,m_dmg,s_dmg)
    print tgt
    
def bludgeon():
    p_dmg = pc.physical * 0.3 # having trouble accessing from PC
    m_dmg = pc.physical * 0.3
    s_dmg = pc.physical * 0.1
    missBar = 85 + pc.physical
    tgt = "bludgeoned"
    feedDmg(p_dmg,m_dmg,s_dmg)



##############################
# (C) MATTHEW MENEGHINI 2012 #
##############################
