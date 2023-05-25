import schedule
import webbrowser
import pyperclip
import time
from library import *
import random

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
am_or_pm = ""

this_time = "The time is " + str(current_hour) + ":" + \
    str(current_minute) + " " + " right now."

speak_text("Greetings")
speak_text(this_time)
weather = f"Outside it is {get_weather()} degrees Celsius."
speak_text(weather)

time_one = "08:30"
time_two = "10:05"
time_three = "11:55"
time_four = "13:25"

current_week = datetime.date.today().isocalendar()[1]
this_week = ""
if current_week % 2 == 0:
    this_week = "Знаменник"
    speak_text("This week is a Denominator")
else:
    this_week = "Чисельник"
    speak_text("This week is a Numerator")

today = date.today()
print("\nЗ поверненням!")
print("Сьогодні - ", today.strftime("%d.%m.%Y"),
      today.strftime("%A"), this_week)
t = time.localtime()
this = time.strftime("%b %dth %Y", t)
that = today.strftime("%A")
here_you_go = "Today is " + this + ". " + that
speak_text(here_you_go)
if today.strftime("%A") == "Monday" or today.strftime("%A") == "Tuesday" or today.strftime("%A") == "Wednesday" or today.strftime("%A") == "Thursday":
    print("\nСьогоднішні пари:")
    speak_text("Today's classes:")
else:
    print("\nСьогодні пар нема!\n")
    speak_text("There are no classes today")

if today.strftime("%A") == "Monday":
    print("- Фізична Підготовка at " + time_one)
    print("- ООП Лекція at " + time_two)
    print("- ООП Лаба at " + time_three)
    print("- Низькорівневе Програмування Лаба at " + time_four)
    speak_text("- Physical Education at " + time_one)
    speak_text("- OOP Lecture at " + time_two)
    speak_text("- OOP Lab at " + time_three)
    speak_text("- Low Level Programming Lab at " + time_four)
elif today.strftime("%A") == "Tuesday":
    print("- Англійська Мова at " + time_two)
    speak_text("- English at " + time_two)
    if this_week == "Знаменник":
        print("- КДМ Лекція at " + time_three)
        speak_text("- Computer Discrete Maths Lecture at " + time_three)
    else:
        print("- Вища Математика Лекція at " + time_three)
        speak_text("- Calculus Lecture at " + time_three)
elif today.strftime("%A") == "Wednesday":
    if this_week == "Знаменник":
        print("- Філософія Семінар at " + time_two)
        speak_text("- Philosophy Practice at " + time_two)
        print("- Низькорівневе Програмування Лаба at " + time_three)
        speak_text("- Low Level Programming Lab at " + time_three)
    else:
        print("- Групова Динаміка Лаба at " + time_two)
        speak_text("- Soft Skills Lab at " + time_two)
        print("- Низькорівневе Програмування Лекція at " + time_three)
        speak_text("- Low Level Programming Lecture at " + time_three)
elif today.strftime("%A") == "Thursday":
    print("- Дискретна Математика Лаба at " + time_one)
    speak_text("- Computer Discrete Maths Lab at " + time_one)
    print("- Фізична Підготовка at " + time_two)
    speak_text("- Physical Education at " + time_two)
    if this_week == "Знаменник":
        print("- Філософія Лекція at " + time_three)
        speak_text("- Philosophy Lecture at " + time_three)
    else:
        print("- Групова Динаміка Лекція at " + time_three)
        speak_text("- Soft Skills Lecture at " + time_three)
    print("- Вища Математика Лаба at " + time_four)
    speak_text("- Calculus Lab at " + time_four)
print("")

time.sleep(2)
open_diary()


schedule.every().day.at("07:00").do(open_food)
schedule.every().day.at("11:25").do(open_food)
schedule.every().day.at("14:45").do(open_food)
schedule.every().day.at("18:00").do(open_workout)
schedule.every().day.at("18:45").do(open_food)

# SECTION CLASSES AUTOMATION

schedule.every().monday.at("08:28").do(пн_фп)
schedule.every().monday.at("10:03").do(пн_ооп_лк)
schedule.every().monday.at("11:53").do(пн_ооп_лб)
schedule.every().monday.at("13:23").do(пн_нп)

schedule.every().tuesday.at("10:03").do(вт_ам)
if current_week % 2 == 0:
    schedule.every().tuesday.at("11:53").do(вт_кдм_зна)
else:
    schedule.every().tuesday.at("11:53").do(вт_вмма_чис)

if current_week % 2 == 0:
    schedule.every().wednesday.at("10:03").do(ср_фі_зна)
    schedule.every().wednesday.at("11:53").do(ср_нп_зна)
else:
    schedule.every().wednesday.at("10:03").do(ср_сс_чис)
    schedule.every().wednesday.at("11:53").do(ср_нп_чис)

schedule.every().thursday.at("08:28").do(чт_кдм)
schedule.every().thursday.at("10:03").do(чт_фп)
if current_week % 2 == 0:
    schedule.every().thursday.at("11:53").do(чт_фі_зна)
else:
    schedule.every().thursday.at("11:53").do(чт_ss_чис)
schedule.every().thursday.at("13:23").do(чт_вмма)

while True:
    schedule.run_pending()
    time.sleep(3)
