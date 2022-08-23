from typing import Text
from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = "en"
text=input("Enter text to convert to speech")

sp = gTTS(text,lang=language,slow=False)

sp.save(audio)
playsound(audio)


