"""
Title: language app
Author: Michelle Liu
Date: 06/05/24
Version: 1
"""

# -----------------
# Imports
# -----------------
import os
from guizero import App
from random import shuffle

# -----------------
# Variables
# -----------------

# setting up path to images folder to give a list of images which are then shuffled
images_dir = "images"
images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
shuffle(images)

# -----------------
# Functions
# -----------------

# function to link image with word

# function to set up one round

# function to match words with images

# function to set up timer

# -----------------
# App
# -----------------

print(images)

app = App("language app")

# box for images

# box for buttons

app.display()
