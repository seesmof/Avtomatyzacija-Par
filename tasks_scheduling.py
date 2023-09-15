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
time.sleep(1)
news()
time.sleep(1)
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


def fetchAndReschedule():
    api = TodoistAPI("e3b0b2ed0642281f8f775fc954ef1567ea84537c")
    today = time.strftime("%Y-%m-%d")
    tasks = api.get_tasks()
    timeRegex = r"\d{2}:\d{2}"
    tasksForToday = [
        t for t in tasks if t.due is not None and t.due.date == today]
    classContents = {
        "ПР. ": {
            "Алгоритми та Структури Даних": ASD_practice,
            "Спортивне Програмування": SP_practice,
            "Вебтехнології та Вебдизайн": WEB_practice,
            "Основи Програмної Інженерії": OPI_practice,
            "Історія України": IY_practice,
            "Теорія Ймовірності": TY_practice,
            "Спеціальні Розділи Вищої Математики": VM_practice
        },
        "ЛК. ": {
            "Алгоритми та Структури Даних": ASD_lecture,
            "Спортивне Програмування": SP_lecture,
            "Вебтехнології та Вебдизайн": WEB_lecture,
            "Основи Програмної Інженерії": OPI_lecture,
            "Історія України": IY_lecture,
            "Теорія Ймовірності": TY_lecture,
            "Спеціальні Розділи Вищої Математики": VM_lecture
        }
    }

    for task in tasksForToday:
        dueTime = re.findall(timeRegex, task.due.string)
        translatedTask = GoogleTranslator(
            source='ukrainian', target='english').translate(task.content)
        if dueTime:
            # check for each class time first and then if its not a class, just schedule it for the due time
            if task.content.startswith("ПР. ") or task.content.startswith("ЛБ. "):
                if "Алгоритми та Структури Даних" in task.content:
                    schedule.every().day.at(dueTime[0]).do(ASD_lecture)
                elif "Спортивне Програмування" in task.content:
                    schedule.every().day.at(dueTime[0]).do(SP_lecture)
                elif "Вебтехнології та Вебдизайн" in task.content:
                    schedule.every().day.at(dueTime[0]).do(WEB_lecture)
                elif "Основи Програмної Інженерії" in task.content:
                    schedule.every().day.at(dueTime[0]).do(OPI_lecture)
                elif "Історія України" in task.content:
                    schedule.every().day.at(dueTime[0]).do(IY_lecture)
                elif "Теорія Ймовірності" in task.content:
                    schedule.every().day.at(dueTime[0]).do(TY_lecture)
                elif "Спеціальні Розділи Вищої Математики" in task.content:
                    schedule.every().day.at(dueTime[0]).do(VM_lecture)
            elif task.content.startswith("ЛК. "):
                if "Алгоритми та Структури Даних" in task.content:
                    schedule.every().day.at(dueTime[0]).do(ASD_practice)
                elif "Спортивне Програмування" in task.content:
                    schedule.every().day.at(dueTime[0]).do(SP_practice)
                elif "Вебтехнології та Вебдизайн" in task.content:
                    schedule.every().day.at(dueTime[0]).do(WEB_practice)
                elif "Основи Програмної Інженерії" in task.content:
                    schedule.every().day.at(dueTime[0]).do(OPI_practice)
                elif "Історія України" in task.content:
                    schedule.every().day.at(dueTime[0]).do(IY_practice)
                elif "Теорія Ймовірності" in task.content:
                    schedule.every().day.at(dueTime[0]).do(TY_practice)
                elif "Спеціальні Розділи Вищої Математики" in task.content:
                    schedule.every().day.at(dueTime[0]).do(VM_practice)
            else:
                schedule.every().day.at(dueTime[0]).do(
                    speak_text, f"Time to do: {GoogleTranslator(source='ukrainian', target='english').translate(task.content)}")
        else:
            # if it has no due time then check for priorities and remind each certain time to just do it saying the task name
            priorityLevels = {1: 4, 2: 3, 3: 2, 4: 1}
            if task.priority in priorityLevels:
                schedule.every(priorityLevels[task.priority]).hours.do(
                    speak_text, f"Don't forget to do: {GoogleTranslator(source='ukrainian', target='english').translate(task.content)}")


schedule.every().hour.do(fetchAndReschedule)

while True:
    schedule.run_pending()
    time.sleep(3)
