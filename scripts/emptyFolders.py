# Script to remove all empty folders

import os
import shutil

root = os.getcwd()

def remove_empty_folders(path_abs):
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            print(path)
            os.rmdir(path)

remove_empty_folders(root)