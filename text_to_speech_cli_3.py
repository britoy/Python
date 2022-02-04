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
engine = pyttsx3.init()



""" VOICE PROPERTIES CONSTANTS """
RATE = 150
VOLUME = .7
VOICE = 1

"""SET VOICE RATE"""
engine.setProperty('rate', RATE)

"""SET VOLUME"""
engine.setProperty('volume', VOLUME)

"""SET VOICE"""
# Retireves all availablr voices from your system.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[VOICE].id)

#run engine to show set properties
engine.runAndWait()

"""GET PROPERTIES"""
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
