import pyttsx3

def output(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
