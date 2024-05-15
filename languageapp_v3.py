"""
Title: language app
Author: Michelle Liu
Date: 13/05/24
Version: 3

"""

# -----------------
# Imports
# -----------------
import os
from guizero import App, Box, PushButton, Text
from random import shuffle

# -----------------
# Variables
# -----------------

# setting up path to images folder to give a list of images which are then shuffled
images_dir = "images/colours"
images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
shuffle(images)

# -----------------
# Functions
# -----------------

# function to link image with word


# function to set up one round
def setup_round():
    # assigning each picture widget with an image from 'images' list with pop() to avoid repetiton
    for picture in pictures:
        picture.image = images.pop()
    # assigning each button widget with text from list
    for button in buttons:
        button.text = buttons_random.pop()


# function to match words with images
def match_answers():
    for x in range(0, 8):
        if len(pictures) == len(buttons):
            text.value = "correct"
        else:
            text.value = "incorrect"


# function to set up timer

# -----------------
# App
# -----------------

#print(images)

app = App("language app")

# box for images
pictures_box = Box(app, layout="grid")
# box for buttons
buttons_box = Box(app, layout="grid")

pictures = []
# buttons list randomised
buttons = []
buttons_random = [
    "Rojo", "Naranja", "Amarillio", "Verde", "Azul", "Morado", "Rosa", "Negro",
    "Blanco"
]
shuffle(buttons_random)
print(buttons_random)

# for loop to create 9 picture and button widgets
for x in range(0, 3):
    for y in range(0, 3):
        picture = PushButton(pictures_box, grid=[x, y])
        pictures.append(picture)

        button = PushButton(buttons_box, grid=[x, y])
        buttons.append(button)

text = Text(app)
setup_round()
app.display()
