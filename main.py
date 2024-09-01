from todoist_api_python.api import TodoistAPI
from datetime import datetime
from time import sleep
import webbrowser
import pyperclip
import schedule
import json
import os

current_dir: str = os.path.dirname(os.path.abspath(__file__))
target_project_id = "2318959463"
now = datetime.now()


def open_class(data):
    class_name, class_type, class_time, class_uri, class_pin = data.values()
    class_type_string = "Practice" if class_type == "P" else "Lecture"

    print(f"Opening {class_name} {class_type_string} on {class_time}")
    webbrowser.open(class_uri)

    note_name=f"{now.strftime("%d-%m-%Y")}_{class_name}-{class_type_string}"
    pyperclip.copy(note_name)

    if class_pin:
        pyperclip.copy(class_pin)


def read_api_key():
    with open(os.path.join(current_dir, "keys.txt"), "r", encoding="utf-8") as f:
        return f.read()


api = TodoistAPI(read_api_key())
tasks = api.get_tasks()
classes = [
    task
    for task in tasks
    if task.due
    and task.due.date == now.strftime("%Y-%m-%d")
    and task.project_id == target_project_id
]

if not classes:
    print("No classes today")
    exit()

with open(os.path.join(current_dir, "info.json"), "r", encoding="utf-8") as f:
    courses_info = json.load(f)

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

while 1:
    schedule.run_pending()
    sleep(3)
