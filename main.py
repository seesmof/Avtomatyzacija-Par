from todoist_api_python.api import TodoistAPI
from datetime import datetime
from time import sleep
import webbrowser
import pyperclip
import schedule
import json

from const import Const as c

def open_class(class_data):
    class_name, class_type, class_time, class_uri, class_pin = class_data.values()
    class_type_string = "Practice" if class_type == "P" else "Lecture"

    print(f"Opening {class_name} {class_type_string} on {class_time}")
    webbrowser.open(class_uri)

    note_name=f"{now.strftime("%d-%m-%Y")}_{class_name}-{class_type_string}"
    pyperclip.copy(f"{class_pin}\n{note_name}")

def fetch_classes():
    def read_api_key():
        with open(c.KEYS_PATH, "r", encoding="utf-8") as f:
            return f.read()

    api_handler = TodoistAPI(read_api_key())
    due_tasks = api_handler.get_tasks()
    classes_list = [
        task
        for task in due_tasks
        if task.due
        and task.due.date == now.strftime("%Y-%m-%d")
        and task.project_id == c.TARGET_PROJECT_ID
    ]
    return classes_list

def schedule_classes(courses_info):
    for current_class in classes:
        class_time = current_class.due.string.split(" ")[-1]
        task_full_name = current_class.content
        class_type, class_name = task_full_name.split(" ")

        course_info = courses_info[class_name]
        uri = course_info[class_type]["uri"]
        pin = course_info[class_type].get("pin", "")

        class_info = {
            "name": class_name,
            "type": class_type,
            "time": class_time,
            "uri": uri,
            "pin": pin,
        }

        class_hour, class_minute = class_time.split(":")
        class_minute = int(class_minute)-3
        class_time = f"{class_hour}:{class_minute:02d}"

        schedule.every().day.at(class_time).do(open_class, class_info)
        print(
            f"{class_name} {'Lecture' if class_type == 'L' else 'Practice'} at {class_time}"
        )


now = datetime.now()
classes=fetch_classes()
if not classes:
    print("No classes today")
    sleep(3)
    exit()

with open(c.INFO_PATH, "r", encoding="utf-8") as f:
    courses_info = json.load(f)
schedule_classes(courses_info)

while 1:
    schedule.run_pending()
    sleep(3)
