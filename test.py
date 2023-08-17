from library import *

schedule.every().day.at("19:12").do(workout, CARDIO_WORKOUT_LINK)

while True:
    schedule.run_pending()
    time.sleep(3)
