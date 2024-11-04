from pprint import pprint
from run import todoist_api

target_project="2342885371"
day_number=67
parent_id=None

Bible_tasks=todoist_api.get_tasks()
check_tasks=[t for t in Bible_tasks if f'Day {day_number}' in t.content]

class Task:
    def __init__(
        self,
        content:str,
        due:str=None,
        project_id:int=target_project,
        parent_id:int=None
    ):
        self.content=content
        self.due=due
        self.project_id=project_id
        self.parent_id=parent_id

if not check_tasks:
    details=Task("Day 67","today")
    new_task=todoist_api.add_task(
        content=details.content,due_string=details.due,project_id=details.project_id
    )
    parent_id=new_task.id
else:
    parent_id=check_tasks[0].id

day_details="Luke 24, Exodus 18, Proverbs 5".split(", ")
print(parent_id)