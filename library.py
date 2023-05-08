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
        "joplin://x-callback-url/openFolder?id=8c86beb5a569443a889f8fb8303c399b")


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
        "https://calendar.google.com/calendar")


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


# SCHEDULE FUNCTIONS


def пн_фп():
    notes_фп()
    time.sleep(2)
    class_фп()


def пн_ооп_лк():
    notes_ооп()
    time.sleep(2)
    class_ооп()


def пн_ооп_лб():
    notes_ооп()
    time.sleep(2)
    class_ооп()


def пн_нп():
    notes_нп()
    time.sleep(2)
    class_нп_пр()


def чт_кдм():
    notes_кдм()
    time.sleep(2)
    class_кдм_пр()


def чт_фп():
    notes_фп()
    time.sleep(2)
    class_фп()


def чт_ss_чис():
    notes_сс()
    time.sleep(2)
    class_сс_лк()


def чт_фі_зна():
    notes_фі()
    time.sleep(2)
    class_фі()


def чт_вмма():
    notes_вмма()
    time.sleep(2)
    class_вмма_пр()


def ср_сс_чис():
    notes_сс()
    time.sleep(2)
    class_сс_пр()


def ср_фі_зна():
    notes_фі()
    time.sleep(2)
    class_фі()


def ср_нп_чис():
    notes_нп()
    time.sleep(2)
    class_нп_лк()


def ср_нп_зна():
    notes_нп()
    time.sleep(2)
    class_нп_пр()


def вт_ам():
    notes_ам()
    time.sleep(2)
    class_ам()


def вт_вмма_чис():
    notes_вмма()
    time.sleep(2)
    class_вмма_лк()


def вт_кдм_зна():
    notes_кдм()
    time.sleep(2)
    class_кдм_лк()
