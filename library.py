from suntime import Sun, SunTimeException
import shutil
import threading
import pyttsx4
import sys
import os
import random
import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time
import requests
import re
import json
import ctypes
import wmi
from todoist_api_python.api import TodoistAPI
from deep_translator import GoogleTranslator

engine = pyttsx4.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

CARDIO_WORKOUT_LINK = "https://youtu.be/ylxSQ_5WbMQ?t=50"
informal_greetings = [
    "Greetings",
    "Hey there",
    "Hello!",
    "Hiya",
    "Hey!",
    "What's up?",
    "Yo!",
    "Hi!",
    "Hey!",
    "Howdy",
    "Hiya!",
    "Hey, how's it going?",
    "Hi there",
    "Yo, what's crackin'?",
    "Hey you!",
    "Sup?",
    "Hi hi!",
    "Hey buddy",
]
short_meal_wishes = [
    "Enjoy your meal!",
    "Bon appétit!",
    "Happy eating!",
    "Tasty bites ahead!",
    "Delight in dining!",
    "Savor every bite!",
    "Have a great feast!",
    "Flavorful moments!",
    "Dig in and enjoy!",
]


def get_sunset():
    latitude = 47.838800
    longitude = 35.139567
    timezone = datetime.datetime.now()

    sun = Sun(latitude, longitude)

    try:
        sunset_time = sun.get_local_sunset_time(timezone)
        return sunset_time.strftime("%H:%M")
    except SunTimeException as e:
        print("Error:", e)


def get_weather():
    city = "Zaporizhzhia"
    api_key = "acf1d8082e6dccbf5b9a72dd3c1f9cf8"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = json.loads(response.text)

    return int(data["main"]["temp"])


def speak_text(*args):
    input_text = " ".join(args)
    print(f"\n{input_text}\n")
    engine.say(input_text)
    engine.runAndWait()


def clear_downloads_folder():
    downloads_folder = os.path.expanduser("~/Downloads")

    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

    speak_text("Clearing downloads folder.")


def close_window():
    speak_text("Close the window.")


def mail():
    speak_text("Opening mail.")
    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")


def tasks():
    speak_text("Opening tasks.")
    webbrowser.open_new_tab("https://habitica.com/")


def workout(
    page="joplin://x-callback-url/openFolder?id=7bc59968dcc94a5f8705ae8e07511e6e",
):
    motivational_phrases = [
        "You've got this!",
        "Push harder, you're stronger than you think.",
        "Make every rep count!",
        "Sweat now, shine later.",
        "Challenge accepted!",
        "Embrace the grind.",
        "Today's effort, tomorrow's results.",
        "Crush your goals!",
        "Keep going, you're making progress.",
        "No pain, no gain!",
        "Be unstoppable.",
        "You're a fighter!",
        "Prove yourself right.",
        "Focus on progress, not perfection.",
        "Believe in yourself!",
        "Stay determined.",
        "Train insane or remain the same.",
        "Don't quit, you're almost there.",
        "Stronger with every session.",
        "You are your only limit.",
    ]
    speak_text(f"Opening workout. {random.choice(motivational_phrases)}")
    webbrowser.open_new_tab(page)


def diary():
    speak_text("Opening diary.")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openNote?id=43f449a2e8f7494199b59758f917e64f"
    )


def news():
    speak_text("Opening news.")
    webbrowser.open_new_tab(
        "https://www.inoreader.com/feed/https%3A%2F%2Ft.me%2Fnovinach"
    )


def food():
    speak_text(f"Opening food page. {random.choice(short_meal_wishes)}")
    webbrowser.open_new_tab(
        "https://randomoutputs.com/random-recipe-generator?category=all"
    )


def shopping():
    speak_text("Opening groceries page.")
    webbrowser.open_new_tab(
        "obsidian://open?vault=obsidian-main-vault&file=shop%2F200%20Shopping%20Main%20Hub"
    )


def sleep():
    speak_text("Good night, bro.")
    ctypes.windll.user32.LockWorkStation()


def letterbox():
    speak_text("Opening watchlist.")
    webbrowser.open_new_tab("https://letterboxd.com/seesmof/watchlist/by/shuffle/")
