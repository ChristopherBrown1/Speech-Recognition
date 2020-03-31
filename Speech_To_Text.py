# This is a speech recognition system created by Christopher Brown
# Feel free to add something to make it more fun.

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    text = str(text)
    print("You said, \n", text.capitalize())
    if "please" in text:
        print("You said the magic word!")
except:
    print("Translation failed.")
