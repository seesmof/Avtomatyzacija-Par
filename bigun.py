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


def zaplanuvaty_pary():
    def vidkryty_paru(danni_pary):
        nazva_pary, typ_pary, chas_pary, posylannja_pary, pin_pary = danni_pary
        nazva_typu_pary = "praktyku" if typ_pary == "P" else "lekciju"

        print(f"Vidkryto {nazva_typu_pary} {nazva_pary} o {chas_pary}")
        webbrowser.open(posylannja_pary)
        pyperclip.copy(pin_pary)

    for para in pary:
        chas_pary = para.due.string.split(" ")[-1]
        nazva_pary = para.content
        typ_pary, nazva_kursu = nazva_pary.split(" ")

        danni_kursu = danni_kursiv.get(nazva_kursu, {})
        if not danni_kursu:
            continue
        uri = danni_kursu[typ_pary]["uri"]
        pin = danni_kursu[typ_pary].get("pin", "")

        hodyna, hvylyna = chas_pary.split(":")
        hvylyna = int(hvylyna) - 3
        zavchas_pary = f"{hodyna}:{hvylyna:02d}"

        schedule.every().day.at(zavchas_pary).do(
            vidkryty_paru,
            (nazva_kursu, typ_pary, chas_pary, uri, pin),
        )
        print(
            f"{'Lekcija' if typ_pary == 'L' else 'Prakrtyka'} {nazva_kursu} o {chas_pary}"
        )


zaraz = datetime.now()
pary = vantazhyty_pary()
if not pary:
    print("Nema par")
    sleep(3)
    exit()

with open(Zminni.FAJL_POSYLANNJA, "r", encoding="utf-8") as f:
    danni_kursiv = json.load(f)
zaplanuvaty_pary()

while 1:
    schedule.run_pending()
    sleep(40)
