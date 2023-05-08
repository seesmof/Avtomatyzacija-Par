import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time
from library import *


time_one = "08:30"
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
print("\nЗ поверненням!")
print("Сьогодні -", today.strftime("%d.%m.%Y"), today.strftime("%A"), this_week)
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
print("")

time.sleep(2)
open_diary()


schedule.every().day.at("07:00").do(open_food)
schedule.every().day.at("07:30").do(open_diary)
schedule.every().day.at("11:25").do(open_food)
schedule.every().day.at("14:45").do(open_food)
schedule.every().day.at("16:00").do(open_tasks)
schedule.every().day.at("18:00").do(open_workout)
schedule.every().day.at("18:45").do(open_diary)
schedule.every().day.at("19:00").do(open_food)
schedule.every().day.at("19:15").do(open_tasks)
schedule.every().day.at("21:30").do(open_diary)
schedule.every().day.at("22:00").do(open_article)


# SECTION CLASSES AUTOMATION

schedule.every().monday.at("08:28").do(пн_фп)
schedule.every().monday.at("10:03").do(пн_ооп_лк)
schedule.every().monday.at("11:53").do(пн_ооп_лб)
schedule.every().monday.at("13:23").do(пн_нп)

schedule.every().tuesday.at("10:03").do(вт_ам)
if current_week % 2 == 0:
    schedule.every().tuesday.at("11:53").do(вт_кдм_зна)
else:
    schedule.every().tuesday.at("11:53").do(вт_вмма_чис)

if current_week % 2 == 0:
    schedule.every().wednesday.at("10:03").do(ср_фі_зна)
    schedule.every().wednesday.at("11:53").do(ср_нп_зна)
else:
    schedule.every().wednesday.at("10:03").do(ср_сс_чис)
    schedule.every().wednesday.at("11:53").do(ср_нп_чис)

schedule.every().thursday.at("08:28").do(чт_кдм)
schedule.every().thursday.at("10:03").do(чт_фп)
if current_week % 2 == 0:
    schedule.every().thursday.at("11:53").do(чт_фі_зна)
else:
    schedule.every().thursday.at("11:53").do(чт_ss_чис)
schedule.every().thursday.at("13:23").do(чт_вмма)

while True:
    schedule.run_pending()
    time.sleep(10)
