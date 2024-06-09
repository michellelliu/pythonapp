"""
Title: language app
Author: Michelle Liu
Date: 06/06/24
Version: 11
- added score counter 
"""
# https://www.youtube.com/watch?v=FwBsPcFCO-0
#https://tkinter.com/build-a-spanish-language-flashcard-app-python-tkinter-gui-tutorial-168/
# -----------------
# Imports
# -----------------
import os
from guizero import App, Box, PushButton, Window, Text, TextBox
import random
from random import randint

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
with open(files_list[0]) as file:
    data = file.read()
    colour_list = data.split("\n")
    #print(colour_list)

# list of feedback for when user presses the check button
feedback_correct = [
    "you are a " + lang_choice + "wiz!", "woohoo! you're on a roll",
    "well done :)", "well done!", "you know your stuff ;)"
]
feedback_incorrect = [
    "better luck next time!", "we should revise this one :)",
    "keep practicing!"
]

score = 0


# -----------------
# Functions
# -----------------
#function to choose which language the questions are going to be
def choose_lang(language):
    global word_list
    lang_window.hide()
    lang_choice = language
    #print(str(lang_choice) + " button was pressed")

    file_path = ""
    # path for each language file
    if lang_choice == "english":
        file_path = "text_files/colours/english_colours.txt"
        app.title = "English language app"

        #print(file_path)
    if lang_choice == "spanish":
        file_path = "text_files/colours/spanish_colours.txt"
        app.title = "Espanol language app"

    if lang_choice == "french":
        file_path = "text_files/colours/french_colours.txt"
        app.title = "language Francais app"
        app.bg = "#92ADD0"  # powder blue
        check.bg = "#335192"  #YInMn bue
        hint.bg = "#FBF8F3"
        #check.bg = "#E63945"  # red (pantone)
        next.bg = "#FBF8F3"
        user_answer.bg = "#E3DBDD"  #platinum

    if lang_choice == "tereo":
        file_path = "text_files/colours/tereo_colours.txt"
        app.title = "Te Reo language app"

    #read files

    with open(file_path) as file:
        words = file.read()
        word_list = words.split("\n")


# function to clear board and get a new word/ go to the next question
def new_word():
    #clear screen for new question
    user_answer.value = ""
    text.value = ""

    #if user_answer.value == "":
    # print("please enter an answer")
    # get len of word list
    word_count = len(word_list)
    # create random selection
    global random_word
    random_word = randint(0, word_count - 1)

    #create a set of questions and answers by zipping the word and colour list
    qanda = zip(word_list, colour_list)
    global set
    set = list(qanda)
    #print(set)
    question.value = "What colour is ..."
    term.value = set[random_word][1].upper()
    term.bg = set[random_word][1].lower()

    #change the text white if the background colour is black
    if term.bg == "black":
        term.text_color = "white"
    else:
        term.text_color = "black"


# this function checks the user answer against the correct answer and increases the score when answer is correct
def check_answer():
    # print error message if user doesn't enter an answer
    if user_answer.value == "":
        text.value = "please enter a valid answer"
    else:
        # compare user input with answer
        if user_answer.value.lower() == set[random_word][0].lower():
            # CORRECT - pick a random feedback in correct feedback list
            random_correct = random.choice(feedback_correct)
            text.value = "correct!\n" + random_correct
            score.value = int(score.value) + 1
        else:
            #  INCORRECT- pick a random feedback in incorrect feedback list
            random_incorrect = random.choice(feedback_incorrect)
            text.value = "incorrect\n" + random_incorrect


# -----------------
# App
# -----------------

# main app window
app = App(title="language app", width=400)

#https://www.youtube.com/watch?v=ZqHFn7_6RUA
top_box = Box(app, align="top", width="fill")
score_text = Text(top_box, align="left", text="score: ")
score = Text(top_box, text="0", align="left")

question = Text(app, text="press arrow to start", size=20)
term = Text(app, text=word, size=30)
user_answer = TextBox(app, width=15)

bottom_box = Box(app, align="bottom", width="fill")

hint = PushButton(bottom_box,
                  text="hint",
                  image="images/lightbulb.gif",
                  align="left")
next = PushButton(bottom_box,
                  text="next",
                  command=new_word,
                  image="images/arrow.gif",
                  align="right")

check = PushButton(bottom_box, text="check", command=check_answer, width=14)
check.text_size = 14
text = Text(app, text="")

# -----------------
# Language Window
# -----------------
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
