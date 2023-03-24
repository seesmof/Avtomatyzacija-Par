import schedule
import webbrowser
import pyperclip
import datetime


current_week = datetime.date.today().isocalendar()[1]


def пн_нп():
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")


current_week = datetime.date.today().isocalendar()[1]

schedule.every().day.at("18:43").do(пн_нп)

while True:
    schedule.run_pending()
