'''
JESUS CHRIST IS LORD

Making folders for each course
'''

import os

from lib.data import ParaData

p=os.path.join(r'C:\Users\seesm\Videos\Лекції')

def m():
    target_file_path=os.path.join(r"E:\Notatnyk\Університет\20250130174547 32 Інформація про курси - посилання на заняття, список завдань та викладачів з дисциплін.md")
    paras: list[ParaData] = list()

    with open(target_file_path,encoding="utf-8",mode='r') as f:
        lines=f.readlines()

    for line in lines:
        # Remove the beginning `- ` and leading symbols
        clean_line=line[2:].strip()

        para=ParaData(*clean_line.split(' - '))
        paras.append(para)

    return paras

ps=m()

unique_names=[p.name for p in ps]
seen_names=set()
for n in unique_names:
    k,nazva=n.split()
    if nazva=='K' or nazva=='P': continue

    if nazva not in seen_names: seen_names.add(nazva)
    elif nazva in seen_names: continue

    print(nazva)
    os.mkdir(os.path.join(p,nazva))

'''
JESUS CHRIST IS LORD

Making folders for each course
'''

import os

from lib.data import ParaData

p=os.path.join(r'C:\Users\seesm\Videos\Лекції')

subfolders= [folder.path for folder in os.scandir(p) if folder.is_dir()]
for folder in subfolders:
    lecture_folder=os.path.join(folder,'L')
    practice_folder=os.path.join(folder,'P')
    os.mkdir(lecture_folder)
    os.mkdir(practice_folder)