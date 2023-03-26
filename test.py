import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time


def open_stream():
    webbrowser.open_new_tab("https://www.twitch.tv/pixelfedya")


def open_workout():
    webbrowser.open_new_tab(
        "https://www.notion.so/f2b157d90c094729807a4c3d29801309")


def open_diary():
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/6be96ce35f2f4cf4bbfa18394672c30b?v=20fb27c8068e4797bb584d0e15db0956")


def open_news():
    webbrowser.open_new_tab("https://news.google.com/home")


time_one = "8:30"
time_two = "10:05"
time_three = "11:55"
time_four = "13:25"

current_week = datetime.date.today().isocalendar()[1]
this_week = ""
if current_week % 2 == 0:
    this_week = "Знаменник"
else:
    this_week = "Чисельник"

today = date.today()
print("\nВітаю!")
print("Сьогодні -", today.strftime("%d.%m.%Y"),
      today.strftime("%A"), this_week)
if today.strftime("%A") == "Monday" or today.strftime("%A") == "Tuesday" or today.strftime("%A") == "Wednesday" or today.strftime("%A") == "Thursday":
    print("\nСьогоднішні пари:")
else:
    print("\nСьогодні пар нема!\n")

if today.strftime("%A") == "Monday":
    print("- Фізична Підготовка -", time_one)
    print("- ООП Лекція -", time_two)
    print("- ООП Лаба -", time_three)
    print("- Низькорівневе Програмування Лаба -", time_four)
elif today.strftime("%A") == "Tuesday":
    print("- Англійська Мова -", time_two)
    if this_week == "Знаменник":
        print("- КДМ Лекція -", time_three)
    else:
        print("- Вища Математика Лекція -", time_three)
elif today.strftime("%A") == "Wednesday":
    if this_week == "Знаменник":
        print("- Філософія Семінар -", time_two)
        print("- Низькорівневе Програмування Лаба -", time_three)
    else:
        print("- Групова Динаміка Лаба -", time_two)
        print("- Низькорівневе Програмування Лекція -", time_three)
elif today.strftime("%A") == "Thursday":
    print("- Дискретна Математика Лаба -", time_one)
    print("- Фізична Підготовка -", time_two)
    if this_week == "Знаменник":
        print("- Філософія Лекція -", time_three)
    else:
        print("- Групова Динаміка Лекція -", time_three)
    print("- Вища Математика Лаба -", time_four)

time.sleep(6)
open_diary()
time.sleep(4)
open_news()

schedule.every().day.at("20:00").do(open_stream)
schedule.every().day.at("18:00").do(open_workout)
schedule.every().day.at("21:00").do(open_diary)


def пн_фп():
    webbrowser.open(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09")


def пн_ооп_лк():
    webbrowser.open("https://us02web.zoom.us/j/85793432609")


def пн_ооп_лб():
    webbrowser.open("https://us02web.zoom.us/j/85793432609")


def пн_нп():
    webbrowser.open(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")


def чт_кдм():
    webbrowser.open("https://meet.google.com/hke-ztgv-wxg")


def чт_фп():
    webbrowser.open(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09")


def чт_ss_чис():
    webbrowser.open(
        "https://us04web.zoom.us/j/76026382394?pwd=wcmYLJnXS7RVbz7ZFu624OeGozRwgs")


def чт_фі_зна():
    webbrowser.open(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20")


def чт_вмма():
    webbrowser.open(
        "https://us05web.zoom.us/j/3815612002?pwd=VW03dHdFQzk1Qnk4M0dlL2RMMlIxQT09")


def ср_сс_чис():
    webbrowser.open(
        "https://meet.google.com/sor-axaz-zxk")


def ср_фі_зна():
    webbrowser.open(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20")


def ср_нп_чис():
    webbrowser.open(
        "https://us04web.zoom.us/j/7594080934?pwd=RlBDYW9OMzNGeXkwQjBGQzNKNnF4QT09")


def ср_нп_зна():
    webbrowser.open(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")


def вт_ам():
    webbrowser.open(
        "https://us02web.zoom.us/j/88030483350?pwd=YXFQYU9URVIwd1FRbkxqVFBxd2ZJdz09")


def вт_вмма_чис():
    webbrowser.open(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09")


def вт_кдм_зна():
    webbrowser.open("https://meet.google.com/arg-syjc-vcz")


# Понеділок
schedule.every().monday.at("08:28").do(пн_фп)
schedule.every().monday.at("10:03").do(пн_ооп_лк)
schedule.every().monday.at("11:53").do(пн_ооп_лб)
schedule.every().monday.at("13:25").do(пн_нп)

# Вівторок
schedule.every().monday.at("10:03").do(вт_ам)
if current_week % 2 == 0:
    # Open the знаменник class link
    schedule.every().thursday.at("11:53").do(вт_кдм_зна)
else:
    # Open the чисельник class link
    schedule.every().thursday.at("11:53").do(вт_вмма_чис)

# Середа
if current_week % 2 == 0:
    # Open the знаменник class link
    schedule.every().thursday.at("10:03").do(ср_фі_зна)
    schedule.every().thursday.at("11:53").do(ср_нп_зна)
else:
    # Open the чисельник class link
    schedule.every().thursday.at("10:03").do(ср_сс_чис)
    schedule.every().thursday.at("11:53").do(ср_нп_чис)

# Четвер
schedule.every().thursday.at("08:28").do(чт_кдм)
schedule.every().thursday.at("10:03").do(чт_фп)
if current_week % 2 == 0:
    # Open the знаменник class link
    schedule.every().thursday.at("11:53").do(чт_фі_зна)
else:
    # Open the чисельник class link
    schedule.every().thursday.at("11:53").do(чт_ss_чис)
schedule.every().thursday.at("13:25").do(чт_вмма)

while True:
    schedule.run_pending()
