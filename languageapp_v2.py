"""
Title: language app
Author: Michelle Liu
Date: 13/05/24
Version: 2
"""

# -----------------
# Imports
# -----------------
import os
from guizero import App, Box, Picture, PushButton
from random import shuffle, choice

#from guizero import system_config
#print(system_config.supported_image_types)

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
    for picture in pictures:
        picture.image = images.pop()
        
# function to match words with images

# function to set up timer

# -----------------
# App
# -----------------

print(images)

app = App("language app")

# box for images
pictures_box = Box(app, layout="grid", border=True)
# box for buttons
buttons_box = Box(app, layout="grid")

# picture widgets
pictures = []
buttons = [
    "Rojo", "Naranja", "Amarillio", "Verde", "Azul", "Morado", "Rosa", "Negro",
    "Blanco"
]

random_answer = choice(buttons)

for x in range(0, 3):
    for y in range(0, 2):
        picture = Picture(pictures_box, grid=[x, y])
        pictures.append(picture)

        # button widgets
        #button = PushButton(buttons_box, grid=[x, y])
        #buttons.append(random_answer)

button = PushButton(buttons_box, grid=[0, 0], text=random_answer)
button = PushButton(buttons_box, grid=[0, 1], text=random_answer)
button = PushButton(buttons_box, grid=[1, 0], text=random_answer)
button = PushButton(buttons_box, grid=[1, 1], text=random_answer)

setup_round()
app.display()
