import speech
import time
from generalCommands import search
from specificCommands import weather

def mainLoop():
    while True:
        phrase = speech.input("")

        if 'weather' && 'show' in phrase.split():
            weather()
