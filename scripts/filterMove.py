# Script to move all required blocks in subdirectories based of the list oldBlocks.sublime

import os
import shutil

root = os.getcwd()

old = []

with open("oldBlocks.sublime", "r") as f:
	old = f.readlines()

# print(len(aaaa))*

remove = []

for elem in old:
	temp = elem.rstrip('\r\n')
	temp = temp.split("/")
	remove.append(temp[-1])


for path, subdirs, files in os.walk(root):
    for name in files:
    	if name in remove:
    		shutil.move(os.path.join(path, name), root)
    		print(name)
