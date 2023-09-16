from library import *
from y2t1_class_names_shortcuts import *

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
today = date.today()
dayName = today.strftime("%A")
current_week = datetime.date.today().isocalendar()[1]
weather = f"Outside its {get_weather()} degrees"

classOneTime = "08:30"
classTwoTime = "10:05"
classThreeTime = "11:55"
classFourTime = "13:25"
classFiveTime = "14:55"
classSixTime = "16:45"

speak_text(random.choice(informal_greetings))
speak_text("Today is", dayName)
speak_text(weather)
time.sleep(1)
clear_downloads_folder()
speak_text("Don't forget to make a daily donate.")
time.sleep(2)
news()
time.sleep(4)
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
    speak_text(f"{ASD} Lecture at {classThreeTime}")
    schedule.every().day.at(classThreeTime).do(ASD_lecture)
    if weekNominationStatus == "Чисельник":
        speak_text(f"{TY} Practice at {classFourTime}")
        schedule.every().day.at(classFourTime).do(TY_practice)
        speak_text(f"{SP} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime).do(SP_lecture)
    else:
        speak_text(f"{SP} Lab at {classFourTime}")
        schedule.every().day.at(classFourTime).do(SP_practice)
elif dayName == "Tuesday":
    speak_text(f"{WEB} Lab at {classOneTime}")
    schedule.every().day.at(classOneTime).do(WEB_practice)
    speak_text(f"{ASD} Lab at {classTwoTime}")
    schedule.every().day.at(classTwoTime).do(ASD_practice)
    speak_text(f"{OPI} Lab at {classFiveTime}")
    schedule.every().day.at(classFiveTime).do(OPI_practice)
    if weekNominationStatus == "Знаменник":
        speak_text(f"{OPI} Practice at {classSixTime}")
        schedule.every().day.at(classSixTime).do(OPI_practice)
elif dayName == "Wednesday":
    speak_text(f"{WEB} Lecture at {classTwoTime}")
    schedule.every().day.at(classTwoTime).do(WEB_lecture)
    if weekNominationStatus == "Чисельник":
        speak_text(f"{TY} Lecture at {classOneTime}")
        schedule.every().day.at(classOneTime).do(TY_lecture)
elif dayName == "Thursday":
    if weekNominationStatus == "Чисельник":
        speak_text(f"{IY} Practice at {classFiveTime}")
        schedule.every().day.at(classFiveTime).do(IY_practice)
    else:
        speak_text(f"{OPI} Lecture at {classTwoTime}")
        schedule.every().day.at(classTwoTime).do(OPI_lecture)
        speak_text(f"{IY} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime).do(IY_lecture)
elif dayName == "Friday":
    if weekNominationStatus == "Чисельник":
        speak_text(f"{VM} Lecture at {classTwoTime}")
        schedule.every().day.at(classTwoTime).do(VM_lecture)
        speak_text(f"{VM} Practice at {classThreeTime}")
        schedule.every().day.at(classThreeTime).do(VM_practice)


sunsetTime = get_sunset()
schedule.every().day.at(sunsetTime).do(close_window)

while True:
    schedule.run_pending()
    time.sleep(3)
