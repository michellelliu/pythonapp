"""
Title: language app
Author: Michelle Liu
Date: 16/05/24
Version: 5
this version is just the questions and answers
"""

pictures = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]
buttons = [
    "Rojo", "Naranja", "Amarillio", "Verde", "Azul", "Morado", "Rosa", "Negro",
    "Blanco"
]
# question and answer dictionary
questions = [{
    "question": "red",
    "answer": "Rojo"
}, {
    "question": "orange",
    "answer": "Naranja"
}, {
    "question": "yellow",
    "answer": "Amarillio"
}, {
    "question": "green",
    "answer": "Verde"
}, {
    "question": "blue",
    "answer": "Azul"
}, {
    "question": "purple",
    "answer": "Morado"
}, {
    "question": "pink",
    "answer": "Rosa"
}, {
    "question": "black",
    "answer": "Negro"
}, {
    "question": "white",
    "answer": "Blanco"
}]

for question in questions:
    question_text = question.get("question")
    print(question_text)
