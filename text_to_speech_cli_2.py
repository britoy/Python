""" 
    Name: text_to_speech_cli_.py
    Author: Ygor Brito
    Created:
    Purpose: Render text into speech
    This Library has many modeules with whcic you can try changing
    the voice, volume, and speed rate of the audio.
    https://pypi.org/project/pyttsx3/
    https://pyttsx3.readthedoccs.io/en/latest
    """ 
    

    #pip install pytssx3
    
import pyttsx3

# init function creates an egine
#instance/object for speech synthesis

engine = pyttsx3.init()

#Set properties before you add thing to say
engine.setProperty('rate', 150)     #Speed word per minute
engine.setProperty('volume', 0.9)   #Volume 0.0-1.0

# Queue up things to say
# There will be a short break between each one
# When Spoken, like a pause between sentences
engine.say("You've got mail")
engine.say("You can queue  up multiple items")

#Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech ocnversion has completed
