import os
import time
import playsound
from gtts import gTTS
import speech_recognition as sr 

def speak(text):
    tts=gTTS(text=text,lang='eng')
    filename="sound.mp3"
    tts.save(filename)
    playsound.playsound(filename)
speak("welcome to learn with dhayalan")