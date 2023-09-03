from library import *
from y2t1_class_names_shortcuts import *

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
today = date.today()
dayName = today.strftime("%A")
current_week = datetime.date.today().isocalendar()[1]

classOneTime = "08:30"
classTwoTime = "10:05"
classThreeTime = "11:55"
classFourTime = "13:25"
classFiveTime = "14:55"
classSixTime = "16:45"

weather = f"Outside its {get_weather()} degrees"

speak_text(random.choice(informal_greetings))
speak_text("Today is", dayName)
speak_text(weather)
clear_downloads_folder()
time.sleep(1)
speak_text("Don't forget to make a daily donate.")
news()
time.sleep(3)
mail()

weekNominationStatus = ""
if current_week % 2 == 0:
    weekNominationStatus = "Знаменник"
    speak_text("This week is a Denominator.")
else:
    weekNominationStatus = "Чисельник"
    speak_text("This week is a Numerator.")

if dayName != "Saturday" or dayName != "Sunday":
    speak_text("Today's classes:")
else:
    speak_text("No classes today!")

if dayName == "Monday":
    speak_text(f"{AtaSD} Lecture at {classThreeTime}")
    schedule.every().day.at(classThreeTime - 3).do(AtaSD_lecture)
    if weekNominationStatus == "Чисельник":
        speak_text(f"{TY} Practice at {classFourTime}")
        schedule.every().day.at(classFourTime - 3).do(TY_practice)
        speak_text(f"{SP} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime - 3).do(SP_lecture)
    else:
        speak_text(f"{SP} Lab at {classFourTime}")
        schedule.every().day.at(classFourTime - 3).do(SP_practice)
elif dayName == "Tuesday":
    speak_text(f"{Web} Lab at {classOneTime}")
    schedule.every().day.at(classOneTime - 3).do(Web_practice)
    speak_text(f"{AtaSD} Lab at {classTwoTime}")
    schedule.every().day.at(classTwoTime - 3).do(AtaSD_practice)
    speak_text(f"{OPI} Lab at {classFourTime}")
    schedule.every().day.at(classFourTime - 3).do(OPI_practice)
    if weekNominationStatus == "Знаменник":
        speak_text(f"{OPI} Practice at {classSixTime}")
        schedule.every().day.at(classSixTime - 3).do(OPI_practice)
elif dayName == "Wednesday":
    print("Wednesday")
elif dayName == "Thursday":
    print("Thursday")
elif dayName == "Friday":
    print("Friday")


sunsetTime = get_sunset()
schedule.every().day.at(sunsetTime).do(close_window)

while True:
    schedule.run_pending()
    time.sleep(3)
