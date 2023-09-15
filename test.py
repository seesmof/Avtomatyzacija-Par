import re
import time
import datetime
from todoist_api_python.api import TodoistAPI


def fetchAndReschedule():
    api = TodoistAPI("e3b0b2ed0642281f8f775fc954ef1567ea84537c")
    today = time.strftime("%Y-%m-%d")
    tasks = api.get_tasks()
    timeRegex = r"\d{2}:\d{2}"

    for task in tasks:
        if task.due is not None and task.due.date == today:
            dueTime = re.findall(timeRegex, task.due.string)
            print(
                f"\n{task.content} at {dueTime[0] if dueTime else 'any time'}\n")


fetchAndReschedule()

# tasks examples

# Task(
#     is_completed=False,
#     content='ЛК. Спеціальні Розділи Вищої Математики',
#     description='',
#     due=Due(date='2023-09-15', string='every other fri at 10:05'),
#     priority=1
# )

# Task(
#     is_completed=False,
#     content='test priority 1',
#     description='',
#     due=Due(date='2023-09-15', string='15 Sep'),
#     priority=4
# )
