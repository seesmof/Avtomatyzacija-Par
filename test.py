import re
import time
import datetime
from todoist_api_python.api import TodoistAPI


def fetchAndReschedule():
    api = TodoistAPI("e3b0b2ed0642281f8f775fc954ef1567ea84537c")
    today = time.strftime("%Y-%m-%d")
    tasks = api.get_tasks()
    timeRegex = r"\d{2}:\d{2}"
    tasks = [t for t in tasks if t.due is not None and t.due.date == today]

    for task in tasks:
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

# full format. above is just the properties we really need

# Task(assignee_id=None, assigner_id=None, comment_count=0, is_completed=False, content='ПР. Спеціальні Розділи Вищої Математики', created_at='2023-09-03T18:16:36.019003Z', creator_id='45513878', description='', due=Due(date='2023-09-15', is_recurring=True, string='every other fri at 11:55', datetime='2023-09-15T08:55:00Z', timezone='Europe/Kiev'), id='7194004149', labels=['GCal'], order=11, parent_id=None, priority=1, project_id='2318959463', section_id=None, url='https://todoist.com/showTask?id=7194004149', sync_id=None)
