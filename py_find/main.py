import os
import re

banned_folders = [".git", ".idea"]

root_patch = r"../"
my_folders = [os.path.join(root_patch, x) for x in os.listdir(root_patch) if x not in banned_folders and os.path.isdir(os.path.join(root_patch, x))]

i = 0

while i < len(my_folders):
    tmp_folder = my_folders[i]
    tmp_inside_folders = [os.path.join(tmp_folder, x) for x in os.listdir(tmp_folder) if x not in banned_folders and os.path.isdir(os.path.join(tmp_folder, x))]
    my_folders += tmp_inside_folders
    i += 1

my_files = []
for tmp_folder in my_folders:
    tmp_inside_files = [os.path.join(tmp_folder, x) for x in os.listdir(tmp_folder) if x not in banned_folders and os.path.isfile(os.path.join(tmp_folder, x))]
    my_files += tmp_inside_files


case_sensitive = False
text_to_find = "Tar"

for tmp_file in my_files:
    with open(tmp_file, 'r') as file:
        tmp_lines = file.readlines()
        for i, line in enumerate(tmp_lines):
            if not case_sensitive:
                line = line.lower()
                text_to_find = text_to_find.lower()

            if text_to_find in line:
                print(f"{i}   {tmp_file}")
                print(f"    {line}")





