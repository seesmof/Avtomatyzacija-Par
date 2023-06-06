# TODO:

from library import *

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
time_one = "08:30"
time_two = "10:05"
time_three = "11:55"
time_four = "13:25"
this_time = "The time is " + str(current_hour) + ":" + \
    str(current_minute) + " " + " right now."
weather = f"Outside it is {get_weather()} degrees Celsius."
current_week = datetime.date.today().isocalendar()[1]
today = date.today()

speak_text("Greetings")
speak_text(this_time)
speak_text(weather)

this_week = ""
if current_week % 2 == 0:
    this_week = "Знаменник"
    speak_text("This week is a Denominator")
else:
    this_week = "Чисельник"
    speak_text("This week is a Numerator")

print("Сьогодні - ", today.strftime("%d.%m.%Y"),
      today.strftime("%A"), this_week)
t = time.localtime()
this = time.strftime("%b %dth %Y", t)
that = today.strftime("%A")
here_you_go = "Today is " + this + ". " + that
speak_text(here_you_go)
if today.strftime("%A") == "Monday" or today.strftime("%A") == "Tuesday" or today.strftime("%A") == "Wednesday" or today.strftime("%A") == "Thursday":
    speak_text("Today's classes:")
else:
    speak_text("There are no classes today")

if today.strftime("%A") == "Monday":
    speak_text("- Physical Education at " + time_one)
    speak_text("- OOP Lecture at " + time_two)
    speak_text("- OOP Lab at " + time_three)
    speak_text("- Low Level Programming Lab at " + time_four)
elif today.strftime("%A") == "Tuesday":
    speak_text("- English at " + time_two)
    if this_week == "Знаменник":
        speak_text("- Computer Discrete Maths Lecture at " + time_three)
    else:
        speak_text("- Calculus Lecture at " + time_three)
elif today.strftime("%A") == "Wednesday":
    if this_week == "Знаменник":
        speak_text("- Philosophy Practice at " + time_two)
        speak_text("- Low Level Programming Lab at " + time_three)
    else:
        speak_text("- Soft Skills Lab at " + time_two)
        speak_text("- Low Level Programming Lecture at " + time_three)
elif today.strftime("%A") == "Thursday":
    speak_text("- Computer Discrete Maths Lab at " + time_one)
    speak_text("- Physical Education at " + time_two)
    if this_week == "Знаменник":
        speak_text("- Philosophy Lecture at " + time_three)
    else:
        speak_text("- Soft Skills Lecture at " + time_three)
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
