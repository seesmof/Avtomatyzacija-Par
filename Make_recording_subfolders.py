'''
JESUS CHRIST IS LORD

Making folders for each course
'''

import os

import lib
from run import make_paras_data

paras_data=make_paras_data()

unique_names=[p.name for p in paras_data]
seen_names=set()
for this_para_data in paras_data:
    para_kind,para_name=this_para_data.name.split()
    if para_name=='K' or para_name=='P': continue

    if para_name not in seen_names: seen_names.add(para_name)
    else: continue

    folder_path=os.path.join(lib.recordings_folder,para_name)
    os.mkdir(folder_path)

    lecture_folder=os.path.join(folder_path,'L')
    practice_folder=os.path.join(folder_path,'P')
    os.mkdir(lecture_folder)
    os.mkdir(practice_folder)
