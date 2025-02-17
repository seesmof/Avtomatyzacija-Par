from todoist_api_python.api import TodoistAPI
import obsws_python as obs
import datetime
import schedule
import time
import os

import lib
from lib.data import ParaData

todoist_api = TodoistAPI(lib.todoist_key)
try:
    recorder = obs.ReqClient(host='localhost', port=4455, password='Fu2Xfs5vMePGSIkR', timeout=3)
except:
    obs_path=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk"
    os.startfile(obs_path)
    recorder = obs.ReqClient(host='localhost', port=4455, password='Fu2Xfs5vMePGSIkR', timeout=3)

def reschedule_paras():
    os.system('cls')
    schedule.clear()
    schedule_paras()

def schedule_paras():
    scheduled_paras = get_scheduled_paras()
    if not scheduled_paras:
        exit()

    def get_earlier_time(time: str):
        BEFORE_MINTES=3

        hour,minute=time.split(':')
        return f'{hour}:{int(minute)-BEFORE_MINTES:0>2}'

    for para_data in scheduled_paras:
        para_kind, para_name = para_data.content.split(' ')
        para_kind, para_name = para_kind.upper(), para_name.upper()
        para_scheduled_time = para_data.due.string.split()[-1]
        print(f"{lib.get_full_para_kind(para_kind)} {para_name} o {para_scheduled_time}")
        earlier_time=get_earlier_time(para_scheduled_time)
        schedule.every().day.at(earlier_time).do(open_para, f'{para_kind} {para_name}')

def get_scheduled_paras():
    return [
        task for task in todoist_api.get_tasks()
        if task.due
        and task.due.date == time.strftime("%Y-%m-%d")
        and len(task.content) == 4
        and " " in task.content
        and ("P" in task.content.upper() or "L" in task.content.upper())
    ]

def open_para(para_abbr: str = "L IV"):
    this_class_data=[d for d in make_paras_data() if d.name==para_abbr][0]

    os.system(f'start "" {this_class_data.link}')
    lib.copy_text(this_class_data.code) if this_class_data.code else None
    try:
        recorder.start_record()
    except:
        recorder.stop_record()
        recorder.start_record()

    def get_time(m):
        return (datetime.datetime.now() + datetime.timedelta(minutes=m)).strftime('%H:%M')

    t=get_time(80)
    schedule.every().day.at(t).do(close_para,para_abbr)
    schedule.every().day.at(t).do(reschedule_paras)

def move_recording_to_its_folder(para_abbr: str = "L IV"):
    def get_latest_file():
        recordings_folder_path=os.path.join(lib.recordings_folder)
        file_paths=[os.path.join(recordings_folder_path,file_name) for file_name in os.listdir(recordings_folder_path) if '.' in file_name]
        latest_file=max(file_paths, key=os.path.getmtime)
        return latest_file

    kind,name=para_abbr.split(' ')

    latest_file_path=get_latest_file()
    file_name=latest_file_path.split('\\')[-1]
    moved_file_path=os.path.join(lib.recordings_folder,name,kind,file_name)
    os.replace(latest_file_path,moved_file_path)

def close_para(para_abbr: str = "L IV"):
    try:
        recorder.stop_record()
        time.sleep(10)
    except: pass
    move_recording_to_its_folder(para_abbr)

def make_paras_data():
    target_file_path=os.path.join(r"E:\Notatnyk\Університет\20250130174547 32 Інформація про курси - посилання на заняття, список завдань та викладачів з дисциплін.md")
    paras: list[ParaData] = list()

    with open(target_file_path,encoding="utf-8",mode='r') as f:
        lines=f.readlines()

    for line in lines:
        clean_line=line[2:].strip()
        para=ParaData(*clean_line.split(' - '))
        paras.append(para)

    return paras

def main():
    reschedule_paras()
    while 1:
        schedule.run_pending()
        time.sleep(40)

if __name__ == "__main__":
    main()
