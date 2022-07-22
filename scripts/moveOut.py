# Script to move all files in directories and subdirectories to the root folder

import os
import shutil

start = os.getcwd()

for root, dirs, files in os.walk(start):
	print(f"root-{root}")
	print(f"dirs-{dirs}")
	if not root == start:
		for file in files:
			print(file)
			shutil.move(os.path.join(root, file), start)