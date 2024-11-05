import os
import time
from const import *

class Task:
    def __init__(
        self,
        content: str,
        due: str = None,
        parent: int = None,
        project: str = str(2342885371),
        description:str=None
    ):
        self.content = content
        self.due = due
        self.project_id = project
        self.parent_id = parent
        self.description=description

def safely_add_task(
    task_name: str,
    task_details: Task,
    search_tasks: list = todoist_api.get_tasks()
):
    check_for_task = [t for t in search_tasks if task_name in t.content]
    if not check_for_task:
        target_task = todoist_api.add_task(
            content=task_details.content,
            due_string=task_details.due,
            project_id=task_details.project_id,
            parent_id=task_details.parent_id,
            description=task_details.description
        )
    else:
        target_task = check_for_task[0]
    return target_task

def form_reading_link(Book:int,chapter:int): 
    return f"https://ebible.org/study/?w1=bible&t1=local%3Aukr1871&v1={tiny_abbreviations[Book]}{chapter}"

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"readings_cache.txt")) as f:
    data=[l.strip() for l in f.readlines()]
    day,lists=data[0],data[1:]

""" 
day_number = 67
day_task = safely_add_task(f"Day {day_number}", Task("Day 67", "today"))
parent_id = day_task.id

day_details = "Luke 24, Exodus 18, Proverbs 5".split(", ")
for list_number,list_name in enumerate(day_details):
    new_sub_task = safely_add_task(
        list_name,
        Task(f'**{list_number+1}** {list_name}', parent=parent_id),
        [t for t in all_tasks if t.parent_id == parent_id],
    )
"""

target_day=68
current_day=0
selected_list=Book_lists[4]
Book_number=0
chapter_number=0
selected_Book=selected_list[Book_number]
while current_day != target_day:
    current_day+=1
    if chapter_number<chapter_counts[selected_Book]: chapter_number+=1
    else:
        if Book_number<len(selected_list)-1: Book_number+=1
        else:
            Book_number=0
        chapter_number=1
    selected_Book=selected_list[Book_number]
    if current_day==target_day:
        print(Book_names_en[selected_Book],chapter_number)
        exit()