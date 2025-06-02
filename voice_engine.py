import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   #voice id 0 for male


def speak(audio):
    engine.say(audio)
    engine.runAndWait()