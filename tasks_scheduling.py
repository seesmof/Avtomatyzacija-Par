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

clear_downloads_folder()
print("Don't forget to make a daily donate.")
news()
mail()

weekNominationStatus = ""
if current_week % 2 == 0:
    weekNominationStatus = "Знаменник"
    print("This week is a Denominator.")
else:
    weekNominationStatus = "Чисельник"
    print("This week is a Numerator.")

if dayName != "Saturday" or dayName != "Sunday":
    print("Today's classes:")
else:
    print("No classes today!")

if dayName == "Monday":
    print(f"{ASD} Lecture at {classThreeTime}")
    schedule.every().day.at(classThreeTime).do(ASD_lecture)
    if weekNominationStatus == "Чисельник":
        print(f"{TY} Practice at {classFourTime}")
        schedule.every().day.at(classFourTime).do(TY_practice)
        print(f"{SP} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime).do(SP_lecture)
    else:
        print(f"{SP} Lab at {classFourTime}")
        schedule.every().day.at(classFourTime).do(SP_practice)
elif dayName == "Tuesday":
    print(f"{WEB} Lab at {classOneTime}")
    schedule.every().day.at(classOneTime).do(WEB_practice)
    print(f"{ASD} Lab at {classTwoTime}")
    schedule.every().day.at(classTwoTime).do(ASD_practice)
    print(f"{OPI} Lab at {classFiveTime}")
    schedule.every().day.at(classFiveTime).do(OPI_practice)
    if weekNominationStatus == "Знаменник":
        print(f"{OPI} Practice at {classSixTime}")
        schedule.every().day.at(classSixTime).do(OPI_practice)
elif dayName == "Wednesday":
    print(f"{WEB} Lecture at {classTwoTime}")
    schedule.every().day.at(classTwoTime).do(WEB_lecture)
    if weekNominationStatus == "Чисельник":
        print(f"{TY} Lecture at {classOneTime}")
        schedule.every().day.at(classOneTime).do(TY_lecture)
elif dayName == "Thursday":
    if weekNominationStatus == "Чисельник":
        print(f"{IY} Practice at {classFiveTime}")
        schedule.every().day.at(classFiveTime).do(IY_practice)
    else:
        print(f"{OPI} Lecture at {classTwoTime}")
        schedule.every().day.at(classTwoTime).do(OPI_lecture)
        print(f"{IY} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime).do(IY_lecture)
elif dayName == "Friday":
    if weekNominationStatus == "Чисельник":
        print(f"{VM} Lecture at {classTwoTime}")
        schedule.every().day.at(classTwoTime).do(VM_lecture)
        print(f"{VM} Practice at {classThreeTime}")
        schedule.every().day.at(classThreeTime).do(VM_practice)


sunsetTime = get_sunset()
schedule.every().day.at(sunsetTime).do(close_window)

while True:
    schedule.run_pending()
    time.sleep(3)
