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

speak_text(random.choice(informal_greetings))
speak_text("Today is", dayName)
speak_text(weather)
this_week = ""
if current_week % 2 == 0:
    this_week = "Знаменник"
    speak_text("This week is a Denominator!")
else:
    this_week = "Чисельник"
    speak_text("This week is a Numerator!")

# TODO: Fill in the new classes from year two term one here

''' OLD CLASSES BELOW, USE AS TEMPLATE 
if dayName == "Monday" or dayName == "Tuesday" or dayName == "Wednesday" or dayName == "Thursday":
    speak_text("Today's classes:")
else:
    speak_text("No classes today!")

if dayName == "Monday":
    speak_text("PE at " + time_one)
    speak_text("OOP Lecture at " + time_two)
    speak_text("OOP Lab at " + time_three)
    speak_text("ASM Lab at " + time_four)
elif dayName == "Tuesday":
    speak_text("English at " + time_two)
    if this_week == "Знаменник":
        speak_text("Discrete Maths Lecture at " + time_three)
    else:
        speak_text("Calculus Lecture at " + time_three)
elif dayName == "Wednesday":
    if this_week == "Знаменник":
        speak_text("Philosophy Practice at " + time_two)
        speak_text("ASM Lab at " + time_three)
    else:
        speak_text("SS Lab at " + time_two)
        speak_text("ASM Lecture at " + time_three)
elif dayName == "Thursday":
    speak_text("Discrete Maths Lab at " + time_one)
    speak_text("PE at " + time_two)
    if this_week == "Знаменник":
        speak_text("Philosophy Lecture at " + time_three)
    else:
        speak_text("SS Lecture at " + time_three)
    speak_text("Calculus Lab at " + time_four)
'''

clear_downloads_folder()
time.sleep(1)
speak_text("Don't forget to make a daily donate.")
news()
time.sleep(3)
mail()

schedule.every().day.at("15:00").do(shopping)
if dayName == "Tuesday" or dayName == "Thursday" or dayName == "Saturday":
    schedule.every().day.at("18:00").do(workout, CARDIO_WORKOUT_LINK)
else:
    schedule.every().day.at("18:00").do(workout)
schedule.every().day.at("20:00").do(close_window)
schedule.every().day.at("21:30").do(sleep)

while True:
    schedule.run_pending()
    time.sleep(3)
