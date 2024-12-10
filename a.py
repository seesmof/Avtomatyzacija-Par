import os
import re
from todoist_api_python.api import TodoistAPI

todoist_key = "e3b0b2ed0642281f8f775fc954ef1567ea84537c"
todoist_api = TodoistAPI(todoist_key)

tasks = [
    t.content for t in todoist_api.get_tasks() if re.findall(r"\d+[:\s]\d+", t.content)
]
root_directory = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(root_directory, "Table.md")
with open(target_path, encoding="utf-8", mode="w") as f:
    f.write("\n- ".join(tasks))
