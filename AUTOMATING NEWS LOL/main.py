import requests
import pyttsx3
from time import sleep
from datetime import datetime

API_KEY = ""


engine = pyttsx3.init()

r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}")
json_text = r.json()

names = []
titles = []
descriptions = []
conents = []

voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name,voice.id)
# change the rate
engine.setProperty('rate', 220)

# change the volume
engine.setProperty('volume', 0.9)

#  Change the voice
engine.setProperty('voice', voices[4].id)


# Getting hold of the name
for i in range(len(json_text["articles"])):
    names.append(json_text["articles"][i]["source"]["name"])

# getting hold of the title
for i in range(len(json_text["articles"])):
    titles.append(json_text["articles"][i]["title"])

# getting the description

for i in range(len(json_text["articles"])):
    descriptions.append(json_text["articles"][i]["description"])

# getting the content

for i in range(len(json_text["articles"])):
    conents.append(json_text["articles"][i]["content"])



engine.say("Here is Today's News: ")
sleep(1)
for i in range(len(names)):
    engine.say(f"News from {names[i]}")
    engine.runAndWait()
    sleep(1)
    engine.say(f"Title: {titles[i]}")
    engine.runAndWait()
    sleep(1)
    engine.say(f"Description: {descriptions[i]}")
    engine.runAndWait()
    sleep(1)
    engine.say(f"Main content: {conents[i]}")
    engine.runAndWait()
    sleep(1)
    engine.say("going to the next News")
    sleep(1)

