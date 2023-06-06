from year1term2 import *
import random
import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time
import gpt4free
from gpt4free import Provider
import pyttsx3
import requests
import json
engine = pyttsx3.init()


def get_weather():
    city = "Zaporizhzhia"
    api_key = "acf1d8082e6dccbf5b9a72dd3c1f9cf8"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = json.loads(response.text)

    return int(data['main']['temp'])


def generate_response(input_prompt):
    response = gpt4free.Completion.create(Provider.You, prompt=input_prompt)
    return response


def speak_text(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def open_stream():
    speak_text("Opening Fedya's stream\n")
    webbrowser.open_new_tab("https://www.twitch.tv/pixelfedya")


def open_workout():
    speak_text("Opening sport page, get ready for a workout\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=8c86beb5a569443a889f8fb8303c399b")


def open_diary():
    speak_text("Opening diary\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=57cebf0ff83f400591039def63b8bd70")


def open_news():
    speak_text("Opening news\n")
    webbrowser.open_new_tab("https://news.google.com/home")


def open_cards():
    speak_text("Opening flashcards practice\n")
    webbrowser.open_new_tab("https://zorbi.app/decks")


def open_keyboard():
    speak_text("Opening Monkeytype\n")
    webbrowser.open_new_tab("https://monkeytype.com/")


def open_tasks():
    speak_text("Opening current due tasks\n")
    webbrowser.open_new_tab(
        "https://calendar.google.com/calendar")


def open_youtube():
    speak_text("Opening YouTube, time to take a break\n")
    webbrowser.open_new_tab(
        "https://www.youtube.com/")


def open_quick():
    speak_text("Opening quick notes\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openNote?id=bda1807b38f948508b9086779c92859a")


def open_food():
    speak_text("Opening food page, time to go grab something to eat\n")
    webbrowser.open_new_tab(
        "https://randomoutputs.com/random-recipe-generator?category=all")


def open_article():
    speak_text("Opening articles page\n")
    webbrowser.open_new_tab(
        "https://longform.org/random")
