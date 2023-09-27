import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wakeword = "you"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

import g4f
from g4f.Provider import (
    AItianhu,
    Acytoo,
    Aichat,
    Ails,
    Aivvm,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    ChatgptLogin,
    CodeLinkAva,
    DeepAi,
    H2o,
    HuggingChat,
    Opchatgpts,
    OpenAssistant,
    OpenaiChat,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Wewordle,
    Ylokh,
    You,
    Yqcloud,
)
providers=[
    AItianhu,
    Acytoo,
    Aichat,
    Ails,
    Aivvm,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    ChatgptLogin,
    CodeLinkAva,
    DeepAi,
    H2o,
    HuggingChat,
    Opchatgpts,
    OpenAssistant,
    OpenaiChat,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Wewordle,
    Ylokh,
    You,
    Yqcloud,
]
def generateWithAI(q):
    global providers
    for provider in providers[:]:
        try:
            return g4f.ChatCompletion.create(model=g4f.models.default,messages=[{"role":"user","content":q}],provider=provider)
        except Exception as e:
            providers.remove(provider)
    return None
def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if wakeword in query:
            query=query.replace(wakeword,"")
            response=generateWithAI(query)
            print(response)
            speak(response)
            

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

if __name__ == "__main__":
    main()