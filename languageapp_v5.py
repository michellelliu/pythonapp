"""
Title: language app
Author: Michelle Liu
Date: 20/05/24
Version: 5

"""

# -----------------
# Imports
# -----------------
import os
from guizero import App, Box, PushButton, Window
from random import shuffle

# -----------------
# Variables
# -----------------
# setting up path to images folder to give a list of images which are then shuffled
images_dir = "images/colours"
images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
shuffle(images)

square_width = 7
square_height = 4

lang_choice = "english"

# -----------------
# Functions
# -----------------


# function to link image with word
def choose_lang(language):
    lang_choice = language
    print(str(lang_choice) + " button was pressed")

    # opening text file in read mode
    file = open('textfiles/' + str(lang_choice) + '_colours.txt', "r")
    #print(file)
    data = file.read()
    file.close()
    #splitting text in file into a list and returning data
    return data.split("\n")
    

# function to set up one round
def setup_round():
    answers = choose_lang(lang_choice)
    print(answers)
    # assigning each picture widget with an image from 'images' list with pop() to avoid repetiton
    for picture in pictures:
        picture.image = images.pop()
    # assigning each button widget with text from list
    for button in buttons:
        choose_lang(lang_choice)
        button.text = answers.pop()


# -----------------
# App
# -----------------

#print(images)

app = App(title="language app")
# window for picking language of app
lang_window = Window(app, title="language")

# language buttons
english = PushButton(lang_window,
                     text="English",
                     command=lambda: choose_lang("english"))

spanish = PushButton(lang_window,
                     text="Spanish",
                     command=lambda: choose_lang("spanish"))

french = PushButton(lang_window,
                    text="French",
                    command=lambda: choose_lang("french"))

tereo = PushButton(lang_window,
                   text="Te Reo",
                   command=lambda: choose_lang("tereo"))

# box for images
pictures_box = Box(app, align="left", layout="grid")
# box for buttons
buttons_box = Box(app, align="right", layout="grid")

pictures = []
# buttons list randomised
buttons = []

# for loop to create 9 picture and button widgets
for x in range(0, 3):
    for y in range(0, 3):
        picture = PushButton(pictures_box, grid=[x, y])
        pictures.append(picture)

        button = PushButton(buttons_box,
                            grid=[x, y],
                            width=square_width,
                            height=square_height)
        buttons.append(button)
setup_round()
app.display()
