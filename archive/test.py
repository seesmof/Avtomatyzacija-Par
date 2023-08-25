import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")

for item in os.listdir(downloads_folder):
    item_path = os.path.join(downloads_folder, item)
    if os.path.isfile(item_path):
        os.remove(item_path)
    elif os.path.isdir(item_path):
        shutil.rmtree(item_path)

print("Downloads folder cleared.")
