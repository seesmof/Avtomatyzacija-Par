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
            dueTime = re.findall(timeRegex, task.due.string)[0]
            print(dueTime)
            print(task.content)


fetchAndReschedule()

# date format example from task object below
# due=Due(date='2023-09-16', is_recurring=False, string='2023-09-16 20:00', datetime='2023-09-16T17:00:00Z', timezone='Europe/Kiev')

# full task object below
# Task(assignee_id=None, assigner_id=None, comment_count=0, is_completed=False, content='competitive programming group meeting', created_at='2023-09-14T13:52:27.303016Z', creator_id='45513878', description='Субота, 16 вересня · 20:00 – 21:00\n\nПосилання на відеодзвінок: [https://meet.google.com/snw-mzxn-mgs](https://meet.google.com/snw-mzxn-mgs)', due=Due(date='2023-09-16', is_recurring=False, string='2023-09-16 20:00', datetime='2023-09-16T17:00:00Z', timezone='Europe/Kiev'), id='7228425330', labels=[], order=18, parent_id=None, priority=1, project_id='2318870175', section_id=None, url='https://todoist.com/showTask?id=7228425330', sync_id=None)
