import random
import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time
import gpt4free
from gpt4free import Provider
import requests
import json
from elevenlabs import generate, play, set_api_key
set_api_key("0cd37791f7efe35f081355930b026d9c")


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


def speak_text(inputtext):
    audio = generate(
        text=inputtext,
        voice="Bella",
        model="eleven_monolingual_v1"
    )
    play(audio)


def open_stream():
    speak_text("Opening Fedya's stream")
    webbrowser.open_new_tab("https://www.twitch.tv/pixelfedya")


def open_workout():
    speak_text("Opening sport page, get ready for a workout")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=8c86beb5a569443a889f8fb8303c399b")


def open_diary():
    speak_text("Opening diary")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=57cebf0ff83f400591039def63b8bd70")


def open_news():
    speak_text("Opening news")
    webbrowser.open_new_tab("https://news.google.com/home")


def open_cards():
    speak_text("Opening flashcards practice")
    webbrowser.open_new_tab("https://zorbi.app/decks")


def open_keyboard():
    speak_text("Opening Monkeytype")
    webbrowser.open_new_tab("https://monkeytype.com/")


def open_tasks():
    speak_text("Opening current due tasks")
    webbrowser.open_new_tab(
        "https://calendar.google.com/calendar")


def open_youtube():
    speak_text("Opening YouTube, time to take a break")
    webbrowser.open_new_tab(
        "https://www.youtube.com/")


def open_quick():
    speak_text("Opening quick notes")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openNote?id=bda1807b38f948508b9086779c92859a")


def open_food():
    speak_text("Opening food page, time to go grab something to eat")
    webbrowser.open_new_tab(
        "https://randomoutputs.com/random-recipe-generator?category=all")


def open_article():
    speak_text("Opening articles page")
    webbrowser.open_new_tab(
        "https://longform.org/random")


# ! YEAR ONE TERM TWO


def пн_фп():
    notes_фп()
    time.sleep(2)
    class_фп()


def пн_ооп_лк():
    notes_ооп()
    time.sleep(2)
    class_ооп()


def пн_ооп_лб():
    notes_ооп()
    time.sleep(2)
    class_ооп()


def пн_нп():
    notes_нп()
    time.sleep(2)
    class_нп_пр()


def чт_кдм():
    notes_кдм()
    time.sleep(2)
    class_кдм_пр()


def чт_фп():
    notes_фп()
    time.sleep(2)
    class_фп()


def чт_ss_чис():
    notes_сс()
    time.sleep(2)
    class_сс_лк()


def чт_фі_зна():
    notes_фі()
    time.sleep(2)
    class_фі()


def чт_вмма():
    notes_вмма()
    time.sleep(2)
    class_вмма_пр()


def ср_сс_чис():
    notes_сс()
    time.sleep(2)
    class_сс_пр()


def ср_фі_зна():
    notes_фі()
    time.sleep(2)
    class_фі()


def ср_нп_чис():
    notes_нп()
    time.sleep(2)
    class_нп_лк()


def ср_нп_зна():
    notes_нп()
    time.sleep(2)
    class_нп_пр()


def вт_ам():
    notes_ам()
    time.sleep(2)
    class_ам()


def вт_вмма_чис():
    notes_вмма()
    time.sleep(2)
    class_вмма_лк()


def вт_кдм_зна():
    notes_кдм()
    time.sleep(2)
    class_кдм_лк()


def notes_фп():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=891cbdf159bb4e7398f1985c91550c70"
    )


def notes_фі():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=7d47968a5ed649a6bc9aa1ef5fb8ac04"
    )


def notes_ооп():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=7866afa523874295bfbdd1cbbacd31cc"
    )


def notes_кдм():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=5b8b4cacfa6c4fc2bbfde021659e67a8"
    )


def notes_вмма():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=185cd0a5943c4ddaa830ce76e8c5baa1"
    )


def notes_ам():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=191f1bf2fd9b405cbf51c338e19e443c"
    )


def notes_нп():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=a9daf98f14bb4982abc1cb302fab2dd5"
    )


def notes_сс():
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=146a98fc3f0d4cb5855ed71c5d679313"
    )


def class_фп():
    speak_text("Starting Physical Education class")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09"
    )


def class_фі():
    speak_text("Starting Philosophy class")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20"
    )


def class_ооп():
    speak_text("Starting Object-Oriented Programming class")
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")


def class_кдм_пр():
    speak_text("Starting Computer Discrete Maths lab")
    webbrowser.open_new_tab("https://meet.google.com/hke-ztgv-wxg")


def class_кдм_лк():
    speak_text("Starting Computer Discrete Maths lecture")
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")


def class_вмма_пр():
    speak_text("Starting Calculus lab")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/3815612002?pwd=VW03dHdFQzk1Qnk4M0dlL2RMMlIxQT09")


def class_вмма_лк():
    speak_text("Starting Calculus lecture")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09")


def class_ам():
    speak_text("Starting English class")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/88030483350?pwd=YXFQYU9URVIwd1FRbkxqVFBxd2ZJdz09")


def class_нп_пр():
    speak_text("Starting Low Level Programming lab")
    pyperclip.copy("152334")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723"
    )


def class_нп_лк():
    speak_text("Starting Low Level Programming lecture")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/7594080934?pwd=RlBDYW9OMzNGeXkwQjBGQzNKNnF4QT09"
    )


def class_сс_лк():
    speak_text("Starting Soft Skills lecture")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/76026382394?pwd=wcmYLJnXS7RVbz7ZFu624OeGozRwgs"
    )


def class_сс_пр():
    speak_text("Starting Soft Skills lab")
    webbrowser.open_new_tab(
        "https://meet.google.com/sor-axaz-zxk"
    )
