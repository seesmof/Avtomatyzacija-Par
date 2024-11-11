import os
import json
import time
import schedule
import pyperclip

from const import todoist_api

def form_classes_list():
    return [
        t for t in todoist_api.get_tasks()
        if t.due
        and t.due.date == time.strftime("%Y-%m-%d")
        and len(t.content) == 4
        and " " in t.content
        and ("P" in t.content or "L" in t.content)
    ]

def load_classes_data():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"),
        encoding="utf-8",
        mode='r'
    ) as f:
        return json.load(f)

def open_class(class_data: tuple):
    class_type, class_name = class_data
    classes_data = load_classes_data()[class_name][class_type]
    class_link, class_pin = classes_data.get("uri"), classes_data.get("pin")
    # Open class link in browser
    os.system(f'start "" {class_link}')
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
        full_class_type = "Lekcija" if class_type == "L" else "Praktyka"
        print(f"{full_class_type} {class_name} o {class_time}")
        schedule.every().day.at(f'{class_time.split(':')[0]}:{int(class_time.split(':')[1])-3}').do(open_class, (class_type, class_name))

if __name__ == "__main__":
    schedule_classes()
    schedule.every(3).hours.do(schedule_classes)
    while 1:
        schedule.run_pending()
        time.sleep(40)