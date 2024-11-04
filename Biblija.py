from pprint import pprint
from run import todoist_api

target_project="2342885371"
day_number=67
parent_id=None

Bible_tasks=todoist_api.get_tasks()
check_tasks=[t for t in Bible_tasks if f'Day {day_number}' in t.content]

if not check_tasks:
    task_details={
        "content":"Day 67: Luke 24, Exodus 18, Proverbs 5",
        "due_string":"today",
        "project_id":target_project
    }
    new_task=todoist_api.add_task(
        content=task_details['content'],due_string=task_details['due_string'],project_id=task_details['project_id']
    )
    parent_id=new_task.id
else:
    parent_id=check_tasks[0].id

print(parent_id)