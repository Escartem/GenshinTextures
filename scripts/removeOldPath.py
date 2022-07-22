# script to remove the begining of the path in oldBlocks.sublime when originaly extracted from game

old = []

with open("oldBlocks.sublime", "r") as f:
	old = f.readlines()

# print(len(aaaa))

for elem in old:
	temp = elem.rstrip('\r\n')
	temp = temp.split("/")
	print(temp[-1])