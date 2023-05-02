import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time


def open_stream():
    print("Відкриваю стрім PixelFedya\n")
    webbrowser.open_new_tab("https://www.twitch.tv/pixelfedya")


def open_workout():
    print("Відкриваю сторінку спорту\n")
    webbrowser.open_new_tab(
        "https://www.notion.so/f2b157d90c094729807a4c3d29801309")


def open_diary():
    print("Відкриваю щоденник\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=57cebf0ff83f400591039def63b8bd70")


def open_news():
    print("Відкриваю новини\n")
    webbrowser.open_new_tab("https://news.google.com/home")


def open_cards():
    print("Відкриваю практику карток\n")
    webbrowser.open_new_tab("https://zorbi.app/decks")


def open_keyboard():
    print("Відкриваю практику друку Monkeytype\n")
    webbrowser.open_new_tab("https://monkeytype.com/")


def open_tasks():
    print("Відкриваю сторінку з поточними завданнями\n")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/74d72bff0c9a4a328edaf1c6d41da14c?v=b78f3deaf02a4fc2a75dbcffbf478922")


def open_youtube():
    print("Відкриваю YouTube, починаємо відпочинок\n")
    webbrowser.open_new_tab(
        "https://www.youtube.com/")


def open_quick():
    print("Відкриваю швидкі нотатки для персональних проєктів\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openNote?id=bda1807b38f948508b9086779c92859a")


def open_food():
    print("Відкриваю сторінки з їжею. Пора піти шось похавати\n")
    webbrowser.open_new_tab(
        "https://randomoutputs.com/random-food-generator")


def open_article():
    print("Відкриваю сторінку з випадковими статтями на вечір\n")
    webbrowser.open_new_tab(
        "https://longform.org/random")


# CLASSES FUNCTIONS


def notes_фп():
    print("Заходимо на пару з Фізичної Підготовки\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=891cbdf159bb4e7398f1985c91550c70"
    )


def class_фп():
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09"
    )


def notes_фі():
    print("Заходимо на пару з Філософії\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=7d47968a5ed649a6bc9aa1ef5fb8ac04"
    )


def class_фі():
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20"
    )


def notes_ооп():
    print("Заходимо на пару з Об'єктно-Орієнтованого Програмування\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=7866afa523874295bfbdd1cbbacd31cc"
    )


def class_ооп():
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")


def notes_кдм():
    print("Заходимо на пару з Комп'ютерної Дискретної Математики\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=5b8b4cacfa6c4fc2bbfde021659e67a8"
    )


def class_кдм_пр():
    webbrowser.open_new_tab("https://meet.google.com/hke-ztgv-wxg")


def class_кдм_лк():
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")


def notes_вмма():
    print("Заходимо на пару з Вищої Математики та Математичного Аналізу\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=185cd0a5943c4ddaa830ce76e8c5baa1"
    )


def class_вмма_пр():
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/3815612002?pwd=VW03dHdFQzk1Qnk4M0dlL2RMMlIxQT09")


def class_вмма_лк():
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09")


def notes_ам():
    print("Заходимо на пару з Англійської Мови\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=191f1bf2fd9b405cbf51c338e19e443c"
    )


def class_ам():
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/88030483350?pwd=YXFQYU9URVIwd1FRbkxqVFBxd2ZJdz09")


def notes_нп():
    print("Заходимо на пару з Архітектури Комп'ютера та Низькорівневого Програмування\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=a9daf98f14bb4982abc1cb302fab2dd5"
    )


def class_нп_пр():
    pyperclip.copy("152334")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723"
    )


def class_нп_лк():
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/7594080934?pwd=RlBDYW9OMzNGeXkwQjBGQzNKNnF4QT09"
    )


def notes_сс():
    print("Заходимо на пару з Soft Skills, Групової Динаміки та Комунікацій\n")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=146a98fc3f0d4cb5855ed71c5d679313"
    )


def class_сс_лк():
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/76026382394?pwd=wcmYLJnXS7RVbz7ZFu624OeGozRwgs"
    )


def class_сс_пр():
    webbrowser.open_new_tab(
        "https://meet.google.com/sor-axaz-zxk"
    )


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
print("\nВітаю!")
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
schedule.every().sunday.at("16:00").do(open_quick)
schedule.every().day.at("17:00").do(open_youtube)
schedule.every().sunday.at("17:30").do(open_diary)
schedule.every().sunday.at("18:00").do(open_food)
schedule.every().sunday.at("19:00").do(open_tasks)
schedule.every().sunday.at("20:00").do(open_youtube)
schedule.every().sunday.at("20:30").do(open_diary)
schedule.every().sunday.at("21:00").do(open_article)

schedule.every().saturday.at("08:00").do(open_tasks)
schedule.every().saturday.at("09:00").do(open_youtube)
schedule.every().saturday.at("09:30").do(open_diary)
schedule.every().saturday.at("10:00").do(open_quick)
schedule.every().saturday.at("11:30").do(open_youtube)
schedule.every().saturday.at("12:00").do(open_food)
schedule.every().saturday.at("13:00").do(open_tasks)
schedule.every().saturday.at("14:30").do(open_youtube)
schedule.every().saturday.at("15:00").do(open_diary)
schedule.every().saturday.at("16:00").do(open_quick)
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
schedule.every().friday.at("16:00").do(open_quick)
schedule.every().friday.at("17:30").do(open_diary)
schedule.every().friday.at("18:00").do(open_food)
schedule.every().friday.at("19:00").do(open_tasks)
schedule.every().friday.at("20:00").do(open_youtube)
schedule.every().friday.at("20:30").do(open_diary)
schedule.every().friday.at("21:00").do(open_article)

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
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09")
    webbrowser.open_new_tab(
        "joplin://x-callback-url/openFolder?id=891cbdf159bb4e7398f1985c91550c70")


def пн_ооп_лк():
    time.sleep(8)
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-f9b5c2d8f6b349cda8a26bd92fa004cf")


def пн_ооп_лб():
    time.sleep(8)
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-f9b5c2d8f6b349cda8a26bd92fa004cf")


def пн_нп():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-501b28532fb54ad9845a77d2645a767e")


def чт_кдм():
    time.sleep(8)
    webbrowser.open_new_tab("https://meet.google.com/hke-ztgv-wxg")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-1e79743dd9664de9a22e2224578cc093")


def чт_фп():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-82987a7cc1784368b0ff097c38dc9ccb")


def чт_ss_чис():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/76026382394?pwd=wcmYLJnXS7RVbz7ZFu624OeGozRwgs")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-Soft-Skills-b9f6dedc39d64e00a5cdca5458d8e5b8")


def чт_фі_зна():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-9b2c923231fc42d18b7893386b62c6f3#6a529e1a80804ea1bca0206efa42acec")


def чт_вмма():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/3815612002?pwd=VW03dHdFQzk1Qnk4M0dlL2RMMlIxQT09")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-cebe33ea84194b75a5e906dea8b5a2fa")


def ср_сс_чис():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://meet.google.com/sor-axaz-zxk")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-Soft-Skills-b9f6dedc39d64e00a5cdca5458d8e5b8")


def ср_фі_зна():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-9b2c923231fc42d18b7893386b62c6f3#6a529e1a80804ea1bca0206efa42acec")


def ср_нп_чис():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/7594080934?pwd=RlBDYW9OMzNGeXkwQjBGQzNKNnF4QT09")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-501b28532fb54ad9845a77d2645a767e")


def ср_нп_зна():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-501b28532fb54ad9845a77d2645a767e")


def вт_ам():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/88030483350?pwd=YXFQYU9URVIwd1FRbkxqVFBxd2ZJdz09")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-67f44d640e824de6a600b3543069d2fb")


def вт_вмма_чис():
    time.sleep(8)
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-cebe33ea84194b75a5e906dea8b5a2fa")


def вт_кдм_зна():
    time.sleep(8)
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")
    webbrowser.open_new_tab(
        "https://www.notion.so/seesmof/1-2-1e79743dd9664de9a22e2224578cc093")


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
