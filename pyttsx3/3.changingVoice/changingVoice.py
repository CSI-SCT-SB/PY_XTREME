""""
this code shows how to change the voice in pytts3 
engine.getProperty("voices") returns a list of voices installed in windows 
engine.setProperty("voice" , voices[ 1].id) sets the second voice in list as the voice
"""

import pyttsx3 

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice" , voices[1].id )

text = "demonstration of changing the voice in py ttsx3"

engine.say(text)

engine.save_to_file(text , "audio.mp3")

engine.runAndWait()
