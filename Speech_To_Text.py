# This is a speech recognition system created by Christopher Brown
# Program that helps users learn famous phrases or phrases they input.
# Feel free to add something to make it more fun.

# TODO: Add phrases for people
# TODO: Check if that phrase matches the selected phrase. Hide the phrase they select on the side.
# TODO: Create hint boxes that show the next word in the phrase.

import speech_recognition as sr
from tkinter import *


def speech_to_text():
    entry_phrase.delete(0, END)
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        global user_phrase
        user_phrase = r.recognize_google(audio)
        user_phrase = str(user_phrase)
        entry_phrase.delete(0, END)
        entry_phrase.insert(0, user_phrase.capitalize())
        # if "please" in user_phrase:
        #    print("You said the magic word!")
    except:
        print("Translation failed.")

    return


def say_something():
    label_say_something.config(text="Say something...")
    return

person = "user"
phrase_1 = ""
phrase_2 = ""
phrase_3 = ""
guessed_phrase = ""
# -------------------------------- START -----------------------------------------------------------

# Creates screen


root = Tk()
root.title("RePhrase")

# Label for main section
display_text = "Try a phrase"
label_say_something = Label(root, text=display_text)
label_say_something.grid(row=1, column=2, columnspan=2)

# Entry box for user input - Typing or audio.
entry_phrase = Entry(root, width=35, borderwidth=5)
entry_phrase.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
entry_phrase.insert(0, "Push the button to speak or type a phrase...")

# Button that enables microphone.
button_speak = Button(root, text="Speak", padx=60, pady=40, command=lambda:[say_something(), speech_to_text()])
button_speak.grid(row=3, column=2)

# Button Compare to user text
button_compare = Button(root, text="Compare", padx=60, pady=40, command=lambda:[compare()])
button_compare.grid(row=3, column=3)

# Label for Comparison text
label_comparison = Label(root, text="Insert a phrase to compare")
label_comparison.grid(row=0, column=4)

# Label for Choose a famous saying
label_comparison = Label(root, text="Choose a famous saying")
label_comparison.grid(row=0, column=0)

# Buttons for famous phrases
button_mlk = Button(root, text="Martin Luther King Jr.", padx=60, pady=40)
button_mlk.grid(row=1, column=0)

button_shakespeare = Button(root, text="William Shakespeare", padx=60, pady=40)
button_shakespeare.grid(row=2, column=0)

button_lincoln = Button(root, text="Abraham Lincoln", padx=60, pady=40)
button_lincoln.grid(row=3, column=0)

button_spongebob = Button(root, text="Spongebob Squarepants", padx=60, pady=40, command=lambda:[spongebob()])
button_spongebob.grid(row=4, column=0)

# Phrase to compare

def spongebob():
    phrase_1 = "I'm ready"
    phrase_2 = "F is for friends who do stuff together"
    phrase_3 = "The best time to wear a striped sweater is all the time"

    # buttons for spongebob sayings
    quote_1 = Button(root, text="1", padx=60, pady=40, command=lambda:[phrase_selection(phrase_1)])
    quote_1.grid(row=1, column=4)

    quote_1 = Button(root, text="2", padx=60, pady=40, command=lambda:[phrase_selection(phrase_2)])
    quote_1.grid(row=2, column=4)

    quote_1 = Button(root, text="3", padx=60, pady=40, command=lambda:[phrase_selection(phrase_3)])
    quote_1.grid(row=3, column=4)

    # labels for spongebob quotes
    label_1 = Label(root, text=phrase_1)
    label_1.grid(row=1, column=5)

    label_2 = Label(root, text=phrase_2)
    label_2.grid(row=2, column=5)

    label_3 = Label(root, text=phrase_3)
    label_3.grid(row=3, column=5)

    return


def phrase_selection(phrase):
    global selected_phrase
    selected_phrase = phrase
    guessed_phrase = "_ " * len(phrase)
    label_comparison_text = Label(root, text=guessed_phrase)
    label_comparison_text.grid(row=4, column=2, columnspan=2)
    label_comparison_text.update()

    return


def compare():
    if user_phrase == selected_phrase:
        label_outcome = Label(root, text="Correct!")
    else:
        label_outcome = Label(root, text="You suck at this...")

    label_outcome.grid(row=5, column=2, columnspan=2)

    return


root.mainloop()
