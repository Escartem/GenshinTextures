# script to list all files in folder

import os

root = os.getcwd()

final = []

for path, subdirs, files in os.walk(root):
    for name in files:
    	if name.split(".")[-1] != "py":
    		final.append(name)
        # print(os.path.join(path, name))

for elem in final:
	print(elem)