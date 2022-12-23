"""
for changing speech rate in pyttsx we have to use setProperty() fuction
engine.setProperty( "rate" , rate )
default is 200
"""

import pyttsx3 

engine = pyttsx3.init()


text = "changing speech rate in py ttsx3"

engine.setProperty("rate" , 100)
engine.say(text)
engine.save_to_file(text , "audio1.mp3")
engine.runAndWait()

engine.setProperty("rate" , 200)
engine.say(text)
engine.save_to_file(text , "audio2.mp3")
engine.runAndWait()

engine.setProperty("rate" , 300)
engine.say(text)
engine.save_to_file(text , "audio3.mp3")
engine.runAndWait()


