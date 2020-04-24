import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('My name is Oriana. I am here to destroy the world. Altough i am newborn and i have not the strenght i need yet')
engine.runAndWait()
engine.stop()
