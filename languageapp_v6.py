"""
Title: language app
Author: Michelle Liu
Date: 22/05/24
Version: 6
language butttons in language window print which button waas pressed 
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
lang_choice = ""

# setting up path to images folder to give a list of images which are then shuffled
images_dir = "images/colours"
images_list = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
shuffle(images_list)

# path to text files
text_files_dir = "text_files/colours"
files_list = [
    os.path.join(text_files_dir, f) for f in os.listdir(text_files_dir)
]
#print(files_list)
square_width = 7
square_height = 4

# -----------------
# Functions
# -----------------


#function to choose which language the questions are going to be
def choose_lang(language):
    global word_list
    lang_choice = language
    print(str(lang_choice) + " button was pressed")

    file_path = ""
    # path for each language file
    if lang_choice == "english":
        file_path = files_list[0]
        #print(file_path)
    if lang_choice == "spanish":
        file_path = files_list[1]
    if lang_choice == "french":
        file_path = files_list[2]
    if lang_choice == "tereo":
        file_path = files_list[3]
    #read files
    # https://www.youtube.com/watch?v=FwBsPcFCO-0
    with open(file_path) as file:
        words = file.read()
        word_list = words.split("\n")
        #print(word_list)


# function to set up one round
def setup_round():
    # assigning each picture widget with an image from 'images' list with pop() to avoid repetiton
    for picture in pictures:
        picture.image = images_list.pop()
    # assigning each button widget with text from list


# for button in buttons:
#    button.text = word_list.pop()

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

# for loop to create picture and button widgets
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
