"""
save_to_file( text , file_path ) saves the audio to a audiofile 
"""


import pyttsx3 

engine = pyttsx3.init()

text = "hello how are you"

engine.say(text)

engine.save_to_file(text , "audio.mp3") 

engine.runAndWait()
