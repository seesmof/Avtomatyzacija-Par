from dataclasses import dataclass

@dataclass
class Meeting:
    name: str 
    link: str 
    code: str = ""
    lecture: bool = False

classes_data='''
OS https://us04web.zoom.us/j/7235437806?pwd=T2lHS2NaOWkxN1J0UFRaOUU3YWR2QT09 3XzZDf T
'''.strip()
meetings=[]
for row in classes_data.split('\n'):
    name,link,code,lecture=
print(meetings)