# include necessary dependencies
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


def open_cards():
    webbrowser.open_new_tab("https://zorbi.app/decks")


def open_keyboard():
    webbrowser.open_new_tab("https://monkeytype.com/")


def open_tasks():
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/74d72bff0c9a4a328edaf1c6d41da14c?v=b78f3deaf02a4fc2a75dbcffbf478922")


def open_youtube():
    webbrowser.open_new_tab(
        "https://www.youtube.com/")


def open_quick():
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/bec5c26a16494d49a27aac4d3400bfd3")


def open_food():
    webbrowser.open_new_tab(
        "https://randomoutputs.com/random-food-generator")


def open_article():
    webbrowser.open_new_tab(
        "https://longform.org/random")


# define global variables for handling different class times
time_one = "08:30"
time_two = "10:05"
time_three = "11:55"
time_four = "13:25"

# define block for handling numberator or denominator weeks
current_week = datetime.date.today().isocalendar()[1]
this_week = ""
if current_week % 2 == 0:
    this_week = "Знаменник"
else:
    this_week = "Чисельник"

# define block for outputting today's day and classes
today = date.today()
print("\nВітаю!")
print("Сьогодні -", today.strftime("%d.%m.%Y"), today.strftime("%A"), this_week)
# output text depending on the day of the week. Keep in mind that there are no classes friday-sunday, so output the text only on weekdays
if today.strftime("%A") == "Monday" or today.strftime("%A") == "Tuesday" or today.strftime("%A") == "Wednesday" or today.strftime("%A") == "Thursday":
    print("\nСьогоднішні пари:")
else:
    print("\nСьогодні пар нема!\n")

# define block for each day of the week
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

# at the program startup run the following block
time.sleep(2)
open_diary()

# for weekends
schedule.every().day.at("07:00").do(open_diary)
schedule.every().day.at("07:30").do(open_keyboard)
schedule.every().sunday.at("08:00").do(open_tasks)
schedule.every().sunday.at("09:00").do(open_youtube)
schedule.every().sunday.at("09:30").do(open_diary)
schedule.every().sunday.at("10:00").do(open_quick)
schedule.every().sunday.at("11:30").do(open_youtube)
schedule.every().sunday.at("12:00").do(open_food)
schedule.every().sunday.at("13:00").do(open_tasks)
schedule.every().sunday.at("14:30").do(open_youtube)
schedule.every().sunday.at("15:00").do(open_diary)
schedule.every().sunday.at("14:00").do(open_quick)
schedule.every().day.at("17:00").do(open_youtube)
schedule.every().sunday.at("17:30").do(open_diary)
schedule.every().sunday.at("18:00").do(open_food)
schedule.every().sunday.at("19:00").do(open_tasks)
schedule.every().sunday.at("20:00").do(open_youtube)
schedule.every().sunday.at("20:30").do(open_diary)
schedule.every().sunday.at("21:00").do(open_article)
schedule.every().saturday.at("21:42").do(open_article)

schedule.every().saturday.at("08:00").do(open_tasks)
schedule.every().saturday.at("09:00").do(open_youtube)
schedule.every().saturday.at("09:30").do(open_diary)
schedule.every().saturday.at("10:00").do(open_quick)
schedule.every().saturday.at("11:30").do(open_youtube)
schedule.every().saturday.at("12:00").do(open_food)
schedule.every().saturday.at("13:00").do(open_tasks)
schedule.every().saturday.at("14:30").do(open_youtube)
schedule.every().saturday.at("15:00").do(open_diary)
schedule.every().saturday.at("14:00").do(open_quick)
schedule.every().saturday.at("17:30").do(open_diary)
schedule.every().saturday.at("18:00").do(open_food)
schedule.every().saturday.at("19:00").do(open_tasks)
schedule.every().saturday.at("20:00").do(open_youtube)
schedule.every().saturday.at("20:30").do(open_diary)
schedule.every().saturday.at("21:00").do(open_article)

schedule.every().friday.at("08:00").do(open_tasks)
schedule.every().friday.at("09:00").do(open_youtube)
schedule.every().friday.at("09:30").do(open_diary)
schedule.every().friday.at("10:00").do(open_quick)
schedule.every().friday.at("11:30").do(open_youtube)
schedule.every().friday.at("12:00").do(open_food)
schedule.every().friday.at("13:00").do(open_tasks)
schedule.every().friday.at("14:30").do(open_youtube)
schedule.every().friday.at("15:00").do(open_diary)
schedule.every().friday.at("14:00").do(open_quick)
schedule.every().friday.at("17:30").do(open_diary)
schedule.every().friday.at("18:00").do(open_food)
schedule.every().friday.at("19:00").do(open_tasks)
schedule.every().friday.at("20:00").do(open_youtube)
schedule.every().friday.at("20:30").do(open_diary)
schedule.every().friday.at("21:00").do(open_article)

# for weekdays
schedule.every().monday.at("08:00").do(open_tasks)
schedule.every().monday.at("11:25").do(open_food)
schedule.every().monday.at("14:45").do(open_food)
schedule.every().monday.at("15:00").do(open_tasks)
schedule.every().monday.at("17:30").do(open_diary)
schedule.every().monday.at("18:30").do(open_diary)
schedule.every().monday.at("19:00").do(open_food)
schedule.every().monday.at("20:00").do(open_tasks)
schedule.every().monday.at("21:00").do(open_youtube)
schedule.every().monday.at("21:30").do(open_diary)
schedule.every().monday.at("22:00").do(open_article)

schedule.every().tuesday.at("08:00").do(open_tasks)
schedule.every().tuesday.at("11:25").do(open_food)
schedule.every().tuesday.at("14:45").do(open_food)
schedule.every().tuesday.at("15:00").do(open_tasks)
schedule.every().tuesday.at("17:30").do(open_diary)
schedule.every().tuesday.at("18:30").do(open_diary)
schedule.every().tuesday.at("19:00").do(open_food)
schedule.every().tuesday.at("20:00").do(open_tasks)
schedule.every().tuesday.at("21:00").do(open_youtube)
schedule.every().tuesday.at("21:30").do(open_diary)
schedule.every().tuesday.at("22:00").do(open_article)

schedule.every().wednesday.at("08:00").do(open_tasks)
schedule.every().wednesday.at("11:25").do(open_food)
schedule.every().wednesday.at("14:45").do(open_food)
schedule.every().wednesday.at("15:00").do(open_tasks)
schedule.every().wednesday.at("17:30").do(open_diary)
schedule.every().wednesday.at("18:30").do(open_diary)
schedule.every().wednesday.at("19:00").do(open_food)
schedule.every().wednesday.at("20:00").do(open_tasks)
schedule.every().wednesday.at("21:00").do(open_youtube)
schedule.every().wednesday.at("21:30").do(open_diary)
schedule.every().wednesday.at("22:00").do(open_article)

schedule.every().thursday.at("08:00").do(open_tasks)
schedule.every().thursday.at("11:25").do(open_food)
schedule.every().thursday.at("14:45").do(open_food)
schedule.every().thursday.at("15:00").do(open_tasks)
schedule.every().thursday.at("17:30").do(open_diary)
schedule.every().thursday.at("18:30").do(open_diary)
schedule.every().thursday.at("19:00").do(open_food)
schedule.every().thursday.at("20:00").do(open_tasks)
schedule.every().thursday.at("21:00").do(open_youtube)
schedule.every().thursday.at("21:30").do(open_diary)
schedule.every().thursday.at("22:00").do(open_article)


def пн_фп():
    print("Заходимо на пару з Фізичної Підготовки\n")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-82987a7cc1784368b0ff097c38dc9ccb")


def пн_ооп_лк():
    print("Заходимо на лекцію з ООП\n")
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-f9b5c2d8f6b349cda8a26bd92fa004cf")


def пн_ооп_лб():
    print("Заходимо на лабу з ООП\n")
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-f9b5c2d8f6b349cda8a26bd92fa004cf")


def пн_нп():
    print("Заходимо на лабу з НП\n")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-501b28532fb54ad9845a77d2645a767e")


def чт_кдм():
    print("Заходимо на пару з КДМ\n")
    webbrowser.open_new_tab("https://meet.google.com/hke-ztgv-wxg")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-1e79743dd9664de9a22e2224578cc093")


def чт_фп():
    print("Заходимо на пару з Фізичної Підготовки\n")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-82987a7cc1784368b0ff097c38dc9ccb")


def чт_ss_чис():
    print("Заходимо на пару з SS\n")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/76026382394?pwd=wcmYLJnXS7RVbz7ZFu624OeGozRwgs")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-Soft-Skills-b9f6dedc39d64e00a5cdca5458d8e5b8")


def чт_фі_зна():
    print("Заходимо на пару з Філософії\n")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-9b2c923231fc42d18b7893386b62c6f3#6a529e1a80804ea1bca0206efa42acec")


def чт_вмма():
    print("Заходимо на пару з Вищої математики\n")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/3815612002?pwd=VW03dHdFQzk1Qnk4M0dlL2RMMlIxQT09")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-cebe33ea84194b75a5e906dea8b5a2fa")


def ср_сс_чис():
    print("Заходимо на пару з SS\n")
    webbrowser.open_new_tab(
        "https://meet.google.com/sor-axaz-zxk")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-Soft-Skills-b9f6dedc39d64e00a5cdca5458d8e5b8")


def ср_фі_зна():
    print("Заходимо на пару з Філософії\n")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-9b2c923231fc42d18b7893386b62c6f3#6a529e1a80804ea1bca0206efa42acec")


def ср_нп_чис():
    print("Заходимо на пару з НП\n")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/7594080934?pwd=RlBDYW9OMzNGeXkwQjBGQzNKNnF4QT09")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-501b28532fb54ad9845a77d2645a767e")


def ср_нп_зна():
    print("Заходимо на пару з НП\n")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-501b28532fb54ad9845a77d2645a767e")


def вт_ам():
    print("Заходимо на пару з АМ\n")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/88030483350?pwd=YXFQYU9URVIwd1FRbkxqVFBxd2ZJdz09")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-67f44d640e824de6a600b3543069d2fb")


def вт_вмма_чис():
    print("Заходимо на пару з Вищої математики\n")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-cebe33ea84194b75a5e906dea8b5a2fa")


def вт_кдм_зна():
    print("Заходимо на пару з КДМ\n")
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-1e79743dd9664de9a22e2224578cc093")


# Понеділок
schedule.every().monday.at("08:28").do(пн_фп)
schedule.every().monday.at("10:03").do(пн_ооп_лк)
schedule.every().monday.at("11:53").do(пн_ооп_лб)
schedule.every().monday.at("13:23").do(пн_нп)

# Вівторок
schedule.every().tuesday.at("10:03").do(вт_ам)
if current_week % 2 == 0:
    # Open the знаменник class link
    schedule.every().tuesday.at("11:53").do(вт_кдм_зна)
else:
    # Open the чисельник class link
    schedule.every().tuesday.at("11:53").do(вт_вмма_чис)

# Середа
if current_week % 2 == 0:
    # Open the знаменник class link
    schedule.every().wednesday.at("10:03").do(ср_фі_зна)
    schedule.every().wednesday.at("11:53").do(ср_нп_зна)
else:
    # Open the чисельник class link
    schedule.every().wednesday.at("10:03").do(ср_сс_чис)
    schedule.every().wednesday.at("11:53").do(ср_нп_чис)

# Четвер
schedule.every().thursday.at("08:28").do(чт_кдм)
schedule.every().thursday.at("10:03").do(чт_фп)
if current_week % 2 == 0:
    # Open the знаменник class link
    schedule.every().thursday.at("11:53").do(чт_фі_зна)
else:
    # Open the чисельник class link
    schedule.every().thursday.at("11:53").do(чт_ss_чис)
schedule.every().thursday.at("13:23").do(чт_вмма)

while True:
    schedule.run_pending()
    time.sleep(60)
