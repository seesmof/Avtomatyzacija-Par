import pyperclip
from todoist_api_python.api import TodoistAPI
import time
import schedule
import os 

def fetch_classes(): return [t for t in TodoistAPI("").get_tasks() if t.due and t.due.date==time.strftime("%Y-%m-%d") and len(t.content)==4 and " " in t.content and ("P" in t.content or "L" in t.content)]

def get_preponed_time(class_time:str): return f"{class_time.split(":")[0]}:{int(class_time.split(":")[-1])-3}"

def open_class(class_data):
    class_type,class_name,class_time=class_data
    d=get_classes_data()[class_name][class_type]
    class_link,class_pin=d.get("uri"),d.get("pin")
    os.system(f"start \"\" {class_link}")
    pyperclip.copy(class_pin) if class_pin else None

def get_classes_data():
    import json
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.json"),encoding="utf-8") as f:
        return json.load(f)

def schedule_classes(classes):
    for t in classes:
        class_type,class_name=t.content.split()
        class_time=t.due.string.split()[-1]
        
        preponed_time=get_preponed_time(class_time)
        schedule.every().day.do(open_class,(class_type,class_name,preponed_time))

""" 
while 1:
    schedule.run_pending()
    time.sleep(40)
"""

open_class(("L","PP","16:42"))