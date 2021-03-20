from gtts import gTTS 
import os
file = open("draft.txt", "r").read().replace("\n", " ")
speech = gTTS(text = str(file), slow = False)
speech.save('global.mp3')
os.system('start global.mp3')
