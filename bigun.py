class Zminni:
    import os

    POTOCHNA_TEKA = os.path.dirname(os.path.abspath(__file__))
    FAJL_TOKENU = os.path.join(POTOCHNA_TEKA, "kljuchi.txt")
    FAJL_POSYLANNJA = os.path.join(POTOCHNA_TEKA, "posylannja.json")


from todoist_api_python.api import TodoistAPI
from datetime import datetime
from time import sleep
import webbrowser
import pyperclip
import schedule
import json


def vidkryty_paru(danni_pary):
    nazva_pary, typ_pary, chas_pary, posylannja_pary, pin_pary = danni_pary.values()
    nazva_typu_pary = "praktyku" if typ_pary == "P" else "lekciju"

    print(f"Vidkryto {nazva_typu_pary} {nazva_pary} o {chas_pary}")
    webbrowser.open(posylannja_pary)
    pyperclip.copy(pin_pary)


def vantazhyty_pary():
    def prochytaty_kljuch():
        with open(Zminni.FAJL_TOKENU, "r", encoding="utf-8") as f:
            return f.read()

    try:
        object_api = TodoistAPI(prochytaty_kljuch())
        zavdannja = object_api.get_tasks()
    except Exception:
        print("Shchos' pishlo ne tak")
    spysok_par = [
        z
        # Beremo kozhnu paru
        for z in zavdannja
        # Ce shchob vono znajshlo pary
        if z.due
        # Na sjogodni
        and z.due.date == zaraz.strftime("%Y-%m-%d")
        # Jakshcho dovzhyna nazvy 4 symvoly
        and len(z.content) == 4
        # I jakshcho je probil u nazvi
        and " " in z.content
        # I jakshcho je L abo P u nazvi pary
        and ("L" or "P") in z.content
    ]
    return spysok_par


def schedule_classes(courses_info):
    for current_class in courses_info:
        class_time = current_class.due.string.split(" ")[-1]
        task_full_name = current_class.content
        class_type, class_name = task_full_name.split(" ")

        course_info = courses_info.get(class_name, {})
        if not course_info:
            continue
        uri = course_info[class_type]["uri"]
        pin = course_info[class_type].get("pin", "")

        class_hour, class_minute = class_time.split(":")
        class_minute = int(class_minute) - 3
        class_time = f"{class_hour}:{class_minute:02d}"

        schedule.every().day.at(class_time).do(
            vidkryty_paru,
            {
                "name": class_name,
                "type": class_type,
                "time": class_time,
                "uri": uri,
                "pin": pin,
            },
        )
        print(
            f"{class_name} {'Lecture' if class_type == 'L' else 'Practice'} at {class_time}"
        )


zaraz = datetime.now()
pary = vantazhyty_pary()
if not pary:
    print("Nema par")
    sleep(3)
    exit()

with open(Zminni.FAJL_POSYLANNJA, "r", encoding="utf-8") as f:
    danni_kursiv = json.load(f)
schedule_classes(danni_kursiv)

while 1:
    schedule.run_pending()
    sleep(3)
