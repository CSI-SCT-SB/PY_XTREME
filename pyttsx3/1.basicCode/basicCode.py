

import pyttsx3 

engine = pyttsx3.init()  #initializing pyttsx3 
text = "hello how are you" #text to say

engine.say(text)  
engine.runAndWait()
