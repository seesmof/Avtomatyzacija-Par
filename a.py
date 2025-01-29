from dataclasses import dataclass
import os

root=os.path.dirname(os.path.abspath(__file__))
data=os.path.join(root,'data.md')
with open(data,encoding='utf-8',mode='r') as f:
    lines=f.readlines()

@dataclass
class Para:
    name: str
    link: str
    code: str = ""

for l in lines:
    p=Para(*l[2:].strip().split(' - '))
    print(p)