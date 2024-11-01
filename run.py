import os
import json
import time
import schedule
import pyperclip
from todoist_api_python.api import TodoistAPI

def form_classes_list(): 
    return [
        t for t in TodoistAPI("e3b0b2ed0642281f8f775fc954ef1567ea84537c").get_tasks() 
        if t.due 
        and t.due.date==time.strftime("%Y-%m-%d") 
        and len(t.content)==4 
        and " " in t.content 
        and ("P" in t.content or "L" in t.content)
    ]

def get_preponed_time(class_time:str): 
    hours,minutes=class_time.split(":")
    hours,minutes=int(hours),int(minutes)-3
    return f"{hours}:{minutes:02d}"

def load_classes_data():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.json"),encoding="utf-8") as f:
        return json.load(f)

def open_class(class_data:tuple):
    class_type, class_name = class_data
    classes_data = load_classes_data()[class_name][class_type]
    class_link, class_pin = classes_data.get("uri"), classes_data.get("pin")
    # Open class link in browser
    os.system(f"start \"\" {class_link}")
    # Copy class password if any
    pyperclip.copy(class_pin) if class_pin else None

def schedule_classes():
    classes_list = form_classes_list()
    # Check if classes list is empty 
    if not classes_list: 
        exit()

    for class_data in classes_list:
        class_type, class_name = class_data.content.split()
        class_time = class_data.due.string.split()[-1]
        full_class_type = 'Lekcija' if class_type=='L' else 'Praktyka'
        print(f"{full_class_type} {class_name} o {class_time}")
        preponed_time=get_preponed_time(class_time)
        schedule.every().day.at(preponed_time).do(open_class, (class_type,class_name))

schedule_classes()
schedule.every(3).hours.do(schedule_classes)
while 1:
    schedule.run_pending()
    time.sleep(40)