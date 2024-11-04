from pprint import pprint
from run import todoist_api
target_project=2342885371
pprint([t for t in todoist_api.get_tasks() if "Bible test" in t.content])