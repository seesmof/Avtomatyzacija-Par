from library import *

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
time_one = "08:30"
time_two = "10:05"
time_three = "11:55"
time_four = "13:25"
weather = f"Outside its {get_weather()} degrees"
current_week = datetime.date.today().isocalendar()[1]
today = date.today()
dayName = today.strftime("%A")

if dayName == "Sunday":
    schedule.every().day.at("21:35").do(close_window)


while True:
    schedule.run_pending()
    time.sleep(3)
