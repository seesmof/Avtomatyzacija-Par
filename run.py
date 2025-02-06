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

def make_paras_data():
    # target_file_path=os.path.join(root_folder_path,'data.md')
    target_file_path=os.path.join(r"E:\Notatnyk\Університет\20250130174547 32 Інформація про курси - посилання на заняття, список завдань та викладачів з дисциплін.md")
    with open(target_file_path,encoding="utf-8",mode='r') as f:
        lines=f.readlines()
    data: list[ParaData] = list()
    for l in lines:
        p=ParaData(*l[2:].strip().split(' - '))
        data.append(p)
    return data

paras_data=make_paras_data()


def copy_text(text: str):
    command = f'echo {text.strip()}| clip'
    os.system(command)


def get_scheduled_paras():
    return [
        t for t in todoist_api.get_tasks()
        if t.due
        and t.due.date == time.strftime("%Y-%m-%d")
        and len(t.content) == 4
        and " " in t.content
        and ("P" in t.content or "L" in t.content)
    ]


def reschedule_paras():
    os.system('cls')
    schedule.clear()
    schedule_paras()


def close_para(para_abbr: str = "L OS"):
    recorder.stop_record()
    kind,name=para_abbr.split(' ')
    file_name=f'{time.strftime("%Y%m%d")}_{name}-{lib.get_full_para_kind(kind)}'
    copy_text(file_name)


def open_para(para_abbr: str = "L OS"):
    this_class_data=[d for d in paras_data if d.name==para_abbr][0]

    os.system(f'start "" {this_class_data.link}')
    copy_text(this_class_data.code) if this_class_data.code else None
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

def schedule_paras():
    scheduled_paras = get_scheduled_paras()
    if not scheduled_paras:
        exit()

    for para_data in scheduled_paras:
        para_kind, para_name = para_data.content.split(' ')
        para_scheduled_time = para_data.due.string.split()[-1]
        print(f"{lib.get_full_para_kind(para_kind)} {para_name} o {para_scheduled_time}")
        schedule.every().day.at(para_scheduled_time).do(open_para, f'{para_kind} {para_name}')

def main():
    reschedule_paras()
    while 1:
        schedule.run_pending()
        time.sleep(40)

if __name__ == "__main__":
    main()