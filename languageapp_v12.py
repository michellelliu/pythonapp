"""
Title: language app
Author: Michelle Liu
Date: 11/06/24
Version: 12
let user change the topic
"""
# https://www.youtube.com/watch?v=FwBsPcFCO-0
#https://tkinter.com/build-a-spanish-language-flashcard-app-python-tkinter-gui-tutorial-168/
# -----------------
# Imports
# -----------------
import os
from guizero import App, Box, PushButton, Window, Text, TextBox, Combo, Slider
import random
from random import randint

# -----------------
# Variables
# -----------------
#initialize variables
lang_choice = ""
word_list = []
word = ""
topic = "numbers"
score = 0
hint_limit = 3
revision_number = 10
# setting up path to images folder to give a list of images which are then shuffled
images_dir = "images/colours"
#images_list = [os.path.join(images_dir, f) for f in #os.listdir(images_dir)]

# list of feedback for when user presses the check button
feedback_correct = [
    "you are a " + lang_choice + "wiz!", "woohoo! you're on a roll",
    "well done :)", "well done!", "you know your stuff!"
]
feedback_incorrect = [
    "better luck next time!", "we should revise this one :)",
    "keep practicing!"
]


# -----------------
# Functions
# -----------------
#function to choose which language the questions are going to be
def choose_lang(language):
    global word_list
    #hide the language choices in lang_window
    lang_box.hide()
    # show the slider to choose the number of questions and change instructions text
    app_settings.show()
    instructions.value = "Choose a topic to learn:"

    lang_choice = language
    #print(str(lang_choice) + " button was pressed")

    file_path = ""
    # path for each language file
    if lang_choice == "english":
        file_path = "text_files/" + str(set_choice.value)+ "/english_" + str(set_choice.value) + ".txt"
        app.title = "English language app"

    if lang_choice == "spanish":
        file_path = "text_files/" + str(set_choice.value) + "/spanish_" + str(set_choice.value) + ".txt"
        app.title = "Espanol language app"

    if lang_choice == "french":
        file_path = "text_files/" + str(set_choice.value)+ "/french_" + str(set_choice.value) + ".txt"
        #customize app to french choice
        app.title = "language Francais app"
        app.bg = "#92ADD0"  # powder blue
        check.bg = "#335192"  #YInMn bue
        hint.bg = "#FBF8F3"
        #check.bg = "#E63945"  # red (pantone)
        next.bg = "#FBF8F3"
        user_answer.bg = "#E3DBDD"  #platinum

    if lang_choice == "tereo":
        file_path = "text_files/" + str(set_choice.value)+ "/tereo_" + str(set_choice.value) + ".txt"
        app.title = "Te Reo language app"

    #read files
    with open(file_path) as file:
        words = file.read()
        word_list = words.split("\n")


# function to clear board and get a new word/ go to the next question


def new_word():
    global revision_number
    # check if answer is correct and add to score
    check_answer()

    #clear screen for new question
    user_answer.value = ""
    text.value = ""
    # get len of word list
    word_count = len(word_list)
    # create random selection
    global random_word
    random_word = randint(0, word_count - 1)

    #create a set of questions and answers by zipping the word and colour list ( index 0 = answer , index 1 = question (in english))
    qanda = zip(word_list, question_list)
    global set
    set = list(qanda)
    #print(set)

    #change the question
    question.value = "What is ..."
    term.value = set[random_word][1].upper()
    #if set choice is 'colours' change the bg of the question to that colour
    if set_choice.value == "colours":
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
        text.align = "left"
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


# function that reveals hint to user
def hint():
    global set
    global hint_limit
    if hint_limit >= 1:
        text.value = set[random_word][0]
        hint_limit = hint_limit - 1
        hints_left.value = "hints left: " + str(hint_limit)
    else:
        text.value = "you have run out of hints"


def change_settings():
    global question_list
    #read chosen language text file
    file = open(
        "text_files/" + set_choice.value + "/english_" + set_choice.value +
        ".txt", "r")
    data = file.read()
    # make list with the english words (these will be used for the question)
    question_list = data.split("\n")
    # hide the language/settings window
    lang_window.hide()
    # start asking user questions
    new_word()


# -----------------
# App
# -----------------

# main app window
app = App(title="language app", width=400)

#https://www.youtube.com/watch?v=ZqHFn7_6RUA
top_box = Box(app, align="top", width="fill")
score_text = Text(top_box, align="left", text="score: ")
score = Text(top_box, text="0", align="left")
hints_left = Text(top_box,
                  text="hints left: " + str(hint_limit),
                  align="right")

question = Text(app, text="", size=20)
term = Text(app, text=word, size=30)
user_answer = TextBox(app, width=15)

bottom_box = Box(app, align="bottom", width="fill")

hint = PushButton(bottom_box,
                  text="hint",
                  image="images/lightbulb.gif",
                  align="left",
                  command=hint)

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
lang_window = Window(app, title="language settings", bg="white")

instructions = Text(lang_window,
                    text="please select a language to revise:",
                    size=15)

##---language options---##
lang_box = Box(lang_window, layout="grid", visible=True)
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

##--other game choice--##
app_settings = Box(lang_window, visible=False)
app_settings.bg = "white"

set_choice = Combo(app_settings, options=["colours", "numbers", "fruits"])

instructions2 = Text(app_settings,
                     text="select number of questions to revise:",
                     size=15)
revision_number = Slider(app_settings, start=5, end=20)

start = PushButton(app_settings,
                   text="Start",
                   align="right",
                   command=change_settings)
# -----------------
# End Window
# -----------------
end_window = Window(app, title="final score", bg="white", visible=False)

app.display()
