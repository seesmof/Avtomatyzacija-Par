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

print("Greetings")
print("Today is " + today.strftime("%d.%m.%Y"))
print(weather)

this_week = ""
if current_week % 2 == 0:
    this_week = "Знаменник"
    print("This week is a Denominator!")
else:
    this_week = "Чисельник"
    print("This week is a Numerator!")

print("Сьогодні ", today.strftime("%d.%m.%Y"),
      today.strftime("%A"), this_week)
t = time.localtime()
if today.strftime("%A") == "Monday" or today.strftime("%A") == "Tuesday" or today.strftime("%A") == "Wednesday" or today.strftime("%A") == "Thursday":
    print("Today's classes:")
else:
    print("No classes today!")

if today.strftime("%A") == "Monday":
    print("PE at " + time_one)
    print("OOP Lecture at " + time_two)
    print("OOP Lab at " + time_three)
    print("ASM Lab at " + time_four)
elif today.strftime("%A") == "Tuesday":
    print("English at " + time_two)
    if this_week == "Знаменник":
        print("Discrete Maths Lecture at " + time_three)
    else:
        print("Calculus Lecture at " + time_three)
elif today.strftime("%A") == "Wednesday":
    if this_week == "Знаменник":
        print("Philosophy Practice at " + time_two)
        print("ASM Lab at " + time_three)
    else:
        print("SS Lab at " + time_two)
        print("ASM Lecture at " + time_three)
elif today.strftime("%A") == "Thursday":
    print("Discrete Maths Lab at " + time_one)
    print("PE at " + time_two)
    if this_week == "Знаменник":
        print("Philosophy Lecture at " + time_three)
    else:
        print("SS Lecture at " + time_three)
    print("Calculus Lab at " + time_four)
print("")

time.sleep(2)
open_diary()

schedule.every().day.at("05:40").do(open_workout)

schedule.every().day.at("06:20").do(open_food)
schedule.every().day.at("11:25").do(open_food)
schedule.every().day.at("18:00").do(open_food)

schedule.every().day.at("07:00").do(open_github)
schedule.every().day.at("15:30").do(open_github)

schedule.every().day.at("14:50").do(open_shopping)
schedule.every().day.at("19:00").do(open_tasks)
schedule.every().day.at("21:50").do(take_nap)


# ! CLASSES AUTOMATION
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
    time.sleep(3)
