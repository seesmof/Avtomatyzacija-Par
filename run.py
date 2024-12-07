import os
import time
import schedule
import pyperclip
from dataclasses import dataclass
from collections import deque
from todoist_api_python.api import TodoistAPI

todoist_key = "e3b0b2ed0642281f8f775fc954ef1567ea84537c"
todoist_api = TodoistAPI(todoist_key)
root=os.path.dirname(os.path.abspath(__file__))

@dataclass
class Meeting:
    link: str
    code: str = ""
    lecture: bool = True

def copy_text(text: str):
    command = f'echo {text.strip()}| clip'
    os.system(command)

q=deque()
'''
add classes to google calendar, schedule them to repeat accordingly 
    those classes should be added to todoist 
read them from todoist, check if a task name is 4 letters, contains a space and either and L or a P letter at the front
add links data and read it 
'''

def check_task_name(task_name: str):
    '''
    Check if todoist task name is a meeting name

    Check if task name is 4 letters long 
        AND has a space in it 
        AND starts with an L (for Lecture) or a P (for Practice)
    '''
    return len(task_name)==4 and ' ' in task_name and (task_name.startswith('P') or task_name.startswith('L'))

def get_meetings():
    return [
        t for t in todoist_api.get_tasks()
        if t.due
        and t.due.date == time.strftime("%Y-%m-%d")
        and check_task_name(t.content)
    ]

print(get_meetings())

def open_class(class_data: tuple):
    class_type, class_name = class_data
    classes_data = load_classes_data()[class_name][class_type]
    class_link, class_pin = classes_data.get("uri"), classes_data.get("pin")
    # Open class link in browser
    os.system(f'start "" {class_link}')
    # Copy class password if any
    pyperclip.copy(class_pin) if class_pin else None

def schedule_classes():
    classes_list = get_meetings()
    # Check if classes list is empty
    if not classes_list:
        exit()

    for class_data in classes_list:
        class_type, class_name = class_data.content.split()
        class_time = class_data.due.string.split()[-1]
        full_class_type = "Lekcija" if class_type == "L" else "Praktyka"
        print(f"{full_class_type} {class_name} o {class_time}")
        schedule.every().day.at(class_time).do(open_class, (class_type, class_name))

def main():
    schedule_classes()
    schedule.every(3).hours.do(schedule_classes)
    while 1:
        schedule.run_pending()
        time.sleep(40)
