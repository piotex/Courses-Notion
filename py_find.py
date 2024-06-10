import os
import re


class bcolors:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'     # purple
    WARNING = '\033[93m'    # yellow
    FAIL = '\033[91m'       # red
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


def main(text_to_find: str):
    banned_folders = [".git", ".idea", ".archiv"]
    banned_files = ["pdf"]
    supported_files = ["md"]
    root_patch = r"."
    my_folders = [os.path.join(root_patch, x) for x in os.listdir(root_patch) if x not in banned_folders and os.path.isdir(os.path.join(root_patch, x))]

    i = 0
    while i < len(my_folders):
        tmp_folder = my_folders[i]
        tmp_inside_folders = [os.path.join(tmp_folder, x) for x in os.listdir(tmp_folder) if x not in banned_folders and os.path.isdir(os.path.join(tmp_folder, x))]
        my_folders += tmp_inside_folders
        i += 1

    my_files = []
    for tmp_folder in my_folders:
        tmp_inside_files = [os.path.join(tmp_folder, x) for x in os.listdir(tmp_folder) if x not in banned_folders and os.path.isfile(os.path.join(tmp_folder, x)) and x.split('.')[-1] in supported_files]
        my_files += tmp_inside_files

    case_sensitive = False
    for tmp_file in my_files:
        with open(tmp_file, 'r', encoding='utf8') as file:
            tmp_lines = file.readlines()
            for i, line in enumerate(tmp_lines):
                if not case_sensitive:
                    line = line.lower()
                    text_to_find = text_to_find.lower()

                if text_to_find in line:
                    splited_text = line.split(text_to_find)
                    print(f"{bcolors.HEADER+str(i+1)+bcolors.ENDC}   {tmp_file[2:]}")
                    print(f"     {splited_text[0]}{bcolors.WARNING+text_to_find+bcolors.ENDC}{splited_text[1]}")


if __name__ == "__main__":
    os.system('clear')
    input_str = input("Text to find: ")
    main(input_str)




