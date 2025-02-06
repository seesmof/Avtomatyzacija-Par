import os


def get_full_para_kind(short_class_type: str):
    return 'Lekcija' if short_class_type.upper() == 'L' else 'Praktyka'

def copy_text(text: str):
    command = f'echo {text.strip()}| clip'
    os.system(command)
