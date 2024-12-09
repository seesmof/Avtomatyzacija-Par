import os
import json
import time
import schedule
import datetime
import obsws_python as obs
from todoist_api_python.api import TodoistAPI

todoist_key = "e3b0b2ed0642281f8f775fc954ef1567ea84537c"
todoist_api = TodoistAPI(todoist_key)
root=os.path.dirname(os.path.abspath(__file__))
try:
    recorder = obs.ReqClient(host='localhost', port=4455, password='Fu2Xfs5vMePGSIkR', timeout=3)
except:
    obs_path=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk"
    os.startfile(obs_path)
    recorder = obs.ReqClient(host='localhost', port=4455, password='Fu2Xfs5vMePGSIkR', timeout=3)

def copy_text(text: str):
    command = f'echo {text.strip()}| clip'
    os.system(command)

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
    with open(os.path.join(root, "data.json"),encoding="utf-8",mode='r') as f:
        return json.load(f)

def get_full_class_type(short_class_type: str):
    return 'Lekcija' if short_class_type == 'L' else 'Praktyka'

def reschedule_classes():
    os.system('cls')
    schedule.clear()
    schedule_classes()

def open_class(class_data: tuple):
    class_type, class_name = class_data
    classes_data = load_classes_data()[class_name][class_type]
    class_link, class_pin = classes_data.get("uri"), classes_data.get("pin")

    os.system(f'start "" {class_link}')
    copy_text(class_pin) if class_pin else None
    try:
        recorder.start_record()
    except:
        recorder.stop_record()
        recorder.start_record()

    def get_time(m):
        '''
        Get time after m minutes
        '''
        return (datetime.datetime.now() + datetime.timedelta(minutes=m)).strftime('%H:%M')

    t=get_time(80)
    schedule.every().day.at(t).do(recorder.stop_record)
    recording_file_name=f'{time.strftime("%Y%m%d")}-{class_name}-{get_full_class_type(class_type)}'
    print(recording_file_name)
    copy_text(recording_file_name)
    schedule.every().day.at(t).do(reschedule_classes)

def schedule_classes():
    classes_list = form_classes_list()
    # Check if classes list is empty
    if not classes_list:
        exit()

    for class_data in classes_list:
        class_type, class_name = class_data.content.split()
        class_time = class_data.due.string.split()[-1]
        print(f"{get_full_class_type(class_type)} {class_name} o {class_time}")
        schedule.every().day.at(class_time).do(open_class, (class_type, class_name))

def main():
    reschedule_classes()
    while 1:
        schedule.run_pending()
        time.sleep(40)

if __name__ == "__main__":
    main()
