from library import *
from y2t1_class_names_shortcuts import *

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
today = date.today()
dayName = today.strftime("%A")
current_week = datetime.date.today().isocalendar()[1]
weather = f"Outside its {get_weather()} degrees"
globalTasks = []

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

sunsetTime = get_sunset()
schedule.every().day.at(sunsetTime).do(close_window)


def fetchAndReschedule():
    api = TodoistAPI("e3b0b2ed0642281f8f775fc954ef1567ea84537c")
    tasks = api.get_tasks()

    today = time.strftime("%Y-%m-%d")
    timeRegex = r"\d{2}:\d{2}"
    tasksForToday = [
        t for t in tasks if t.due is not None and t.due.date == today]
    for task in tasksForToday:
        dueTime = re.findall(timeRegex, task.due.string)
        globalTasks.append({
            "content": task.content,
            "due": dueTime[0] if dueTime else "any time"
        })

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
                    speak_text, f"Time to do: {translatedTask}")
        else:
            # if it has no due time then check for priorities and remind each certain time to just do it saying the task name
            priorityLevels = {1: 4, 2: 3, 3: 2, 4: 1}
            if task.priority in priorityLevels:
                schedule.every(priorityLevels[task.priority]).hours.do(
                    speak_text, f"Don't forget to do: {translatedTask}")
        if task not in globalTasks:
            globalTasks.append({
                "content": task.content,
                "due": dueTime[0] if dueTime else "any time"
            })


schedule.every().hour.do(fetchAndReschedule)
fetchAndReschedule()

while True:
    schedule.run_pending()
    time.sleep(3)
