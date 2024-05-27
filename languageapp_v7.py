"""
Title: language app
Author: Michelle Liu
Date: 25/05/24
Version: 7
"""

# -----------------
# Imports
# -----------------
import os
from guizero import App, Box, PushButton, Window, Text, TextBox, Picture

# -----------------
# Variables
# -----------------
lang_choice = ""
word_list = []
word = ""
# setting up path to images folder to give a list of images which are then shuffled
images_dir = "images/colours"
images_list = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
# path to text files
text_files_dir = "text_files/colours"
files_list = [
    os.path.join(text_files_dir, f) for f in os.listdir(text_files_dir)
]

# -----------------
# Functions
# -----------------


#function to choose which language the questions are going to be
def choose_lang(language):
    global word_list
    lang_window.hide()
    lang_choice = language
    print(str(lang_choice) + " button was pressed")

    file_path = ""
    # path for each language file
    if lang_choice == "english":
        file_path = files_list[0]
        #print(file_path)
    if lang_choice == "spanish":
        file_path = files_list[2]
    if lang_choice == "french":
        file_path = files_list[1]
    if lang_choice == "tereo":
        file_path = files_list[3]
    #read files
    # https://www.youtube.com/watch?v=FwBsPcFCO-0
    with open(file_path) as file:
        words = file.read()
        word_list = words.split("\n")


def new_word():
    #print(word_list)

    if word_list:
        #pop from word_list, return popped list value to question text
        global word
        word = str(word_list.pop())
        question.value = "What colour is " + word + "?"
        picture.image = images_list.pop()
        print(word)
    else:
        print("The words list is empty.")


def new_image():
    question_colour_dict = {
        "red": "#FF0000",
        "orange": "#FFA500",
        "yellow": "#FFFF00",
        "green": "#00FF00",
        "blue": "#0000FF",
        "purple": "	#A020F0",
        "pink": "#FFC0CB",
        "black": "#000000",
        "white": "#FFFFFF"
    }


def check_answer():
    answer = word.lower()
    print(answer)

    if user_answer.value == answer:
        print("correct!")
    else:
        print("incorrect")


# -----------------
# App
# -----------------

# main app window
app = App(title="language app", bg="white")

#https://www.youtube.com/watch?v=ZqHFn7_6RUA
picture = Picture(app, image="images/colours/white.gif")
question = Text(app, text="press next to start", size=20)

check = PushButton(app, text="check", command="check_answer")

bottom_bar = Box(app, layout="grid")
hint = PushButton(bottom_bar, text="hint", grid=[0, 0])
user_answer = TextBox(bottom_bar, grid=[1, 0], width=15)
next = PushButton(bottom_bar, text="next", grid=[2, 0], command=new_word)

text = Text(app, text="")

# box for images
question_box = Box(app, align="left")
# box for buttons
buttons_box = Box(app, align="right", layout="grid")

#question_image =
# window for picking language of app
lang_window = Window(app, title="language", bg="white")

lang_box = Box(lang_window, layout="grid")

#english box
eng_box = Box(lang_box, grid=[0, 0])
english = PushButton(eng_box,
                     image="images/language/english.gif",
                     command=lambda: choose_lang("english"),
                     align="top")

english_label = Text(eng_box, text="English", align="bottom")

#spanish box
spa_box = Box(lang_box, grid=[1, 0])
spanish = PushButton(spa_box,
                     image="images/language/spanish.gif",
                     command=lambda: choose_lang("spanish"),
                     align="top")
spanish_label = Text(spa_box, text="Spanish", align="bottom")

#french box
fre_box = Box(lang_box, grid=[0, 1])
french = PushButton(fre_box,
                    text="French",
                    image="images/language/french.gif",
                    command=lambda: choose_lang("french"),
                    align="top")
french_label = Text(fre_box, text="French", align="bottom")

# maori box
reo_box = Box(lang_box, grid=[1, 1])
tereo = PushButton(reo_box,
                   text="Te Reo",
                   image="images/language/maori.gif",
                   command=lambda: choose_lang("tereo"),
                   align="top")
tereo_label = Text(reo_box, text="Te Reo", align="bottom")
app.display()
