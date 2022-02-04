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

#pass text to say methof
engine.say('Hello, How may I help you?')
    
# run and Wait method processes the voice
engine.runAndWait()