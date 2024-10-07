from todoist_api_python.api import TodoistAPI
import time
api=TodoistAPI("e3b0b2ed0642281f8f775fc954ef1567ea84537c")
valid=[t for t in api.get_tasks() if t.due and t.due.date==time.strftime("%Y-%m-%d") and len(t.content)==4 and " " in t.content and ("P" in t.content or "L" in t.content)]
for t in valid:
    class_type,class_name=t.content.split()
    class_time=t.due.string.split()[-1]