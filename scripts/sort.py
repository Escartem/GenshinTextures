# Script to sort all files in folders, not finished script

import os
import shutil

root = os.getcwd()

files = [f for f in os.listdir('.') if os.path.isfile(f)]

# print(len(files))

for file in files:
	if file.endswith(".png"):
		splitted = file.split(".")[0].split("_")
		# tempSplit = splitted
		pathBegin = []
		for part in splitted:
			# print(part)
			# print(pathBegin)
			if part.lstrip("-").isnumeric():
				break
			else:
				pathBegin.append(part)
				# pathBegin.append(tempSplit)
		pathToMake = os.path.join(root, "/".join(pathBegin))
		if not os.path.exists(pathToMake):
			os.makedirs(pathToMake)
		shutil.move(os.path.join(root, file), os.path.join(pathToMake, file))
		print(os.path.join(pathToMake, file))