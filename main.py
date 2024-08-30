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


def open_class(uri, pin):
    print(f"Opening {uri}")
    webbrowser.open(uri)
    if pin:
        pyperclip.copy(pin)


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
    class_name = current_class.content

    class_type, course_name = class_name.split(" ")

    course_info = courses_info[course_name]
    uri = course_info[class_type]["uri"]
    pin = course_info[class_type].get("pin", "")

    schedule.every().day.at(class_time).do(open_class, uri, pin)
    print(
        f"{course_name} {'Lecture' if class_type == 'L' else 'Practice'} at {class_time}"
    )

while 1:
    schedule.run_pending()
    sleep(3)
