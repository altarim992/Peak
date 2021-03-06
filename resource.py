import os
from os.path import abspath, dirname

import pygame

ROOT_DIR = dirname(abspath(__file__)) # sets the root directory as the current one
DATA_DIR = os.path.join(ROOT_DIR, "assets")

SFX_DIR = os.path.join(DATA_DIR, "sfx")
MUSIC_DIR = os.path.join(DATA_DIR, "music")
MINIMG_DIR = os.path.join(DATA_DIR, "mini")
IMG_DIR = os.path.join(DATA_DIR, "assets/images")

