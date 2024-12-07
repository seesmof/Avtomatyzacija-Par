from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Meeting:
    link: str 
    code: str = ""

new_meeting=Meeting("https://meet.google.com/kmj-jfpk-vtg")
print(new_meeting.link)
print(new_meeting)