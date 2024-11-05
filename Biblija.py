import os
import time
from const import *

all_tasks=todoist_api.get_tasks()

class Task:
    def __init__(
        self,
        content: str,
        due: str = None,
        parent: int = None,
        project: str = str(2342885371),
    ):
        self.content = content
        self.due = due
        self.project_id = project
        self.parent_id = parent

def safely_add_task(
    task_name: str,
    task_details: Task,
    search_tasks: list = all_tasks
):
    check_for_task = [t for t in search_tasks if task_name in t.content]
    if not check_for_task:
        target_task = todoist_api.add_task(
            content=task_details.content,
            due_string=task_details.due,
            project_id=task_details.project_id,
            parent_id=task_details.parent_id,
        )
    else:
        target_task = check_for_task[0]
    return target_task

def form_reading_link(Book:int,chapter:int): 
    return f"https://ebible.org/study/?w1=bible&t1=local%3Aukr1871&v1={tiny_abbreviations[Book]}{chapter}"

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"readings_cache.txt")) as f:
    target_day=int(f.read())

subtask_details=[]
for list_index in range(10):
    Book_number,chapter_number=0,0
    Books_data=Book_lists[list_index]
    selected_Book=Books_data[Book_number]
    current_day=0
    while current_day!=target_day:
        if chapter_number<chapter_counts[selected_Book]:chapter_number+=1
        else:
            Book_number=Book_number+1 if Book_number<len(Books_data)-1 else 0
            chapter_number=1
        selected_Book=Books_data[Book_number]

        current_day+=1
        if current_day==target_day:
            reading_url=form_reading_link(selected_Book,chapter_number)
            subtask_details.append((f'{Book_names_ua[selected_Book]} {chapter_number}',reading_url))

task_name=f"Біблія {target_day}"
day_task = safely_add_task(f"Біблія {target_day}", Task(task_name, "today"))
parent_id = day_task.id

for list_index,list_data in enumerate(subtask_details):
    reading_details,reading_link=list_data
    reading_subtask=safely_add_task(
        reading_details,
        Task(f'[{reading_details}]({reading_link})',parent=parent_id),
        [t for t in all_tasks if t.parent_id==parent_id]
    )