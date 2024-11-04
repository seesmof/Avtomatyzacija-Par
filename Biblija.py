from pprint import pprint
from run import todoist_api

all_tasks=todoist_api.get_tasks()

class Task:
    def __init__(
        self,
        content:str,
        due:str=None,
        parent_id:int=None,
        project_id:str=str(2342885371)
    ):
        self.content=content
        self.due=due
        self.project_id=project_id
        self.parent_id=parent_id

def safely_add_task(
    task_name:str,
    task_details:Task,
    search_tasks:list=all_tasks
):
    check_for_task=[t for t in search_tasks if task_name in t.content]
    if not check_for_task:
        target_task=todoist_api.add_task(
            content=task_details.content,
            due_string=task_details.due,
            project_id=task_details.project_id,
            parent_id=task_details.parent_id
        )
    else:
        target_task=check_for_task[0]
    return target_task

day_number=67
day_task=safely_add_task(f'Day {day_number}',Task("Day 67","today"))
parent_id=day_task.id

day_details="Luke 24, Exodus 18, Proverbs 5".split(", ")
for sub_task in day_details:
    print(sub_task)
    new_sub_task=safely_add_task(sub_task,Task(sub_task,parent_id=parent_id))
    print(new_sub_task.id)