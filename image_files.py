import os

# Get the list of all files and directories
# in the root directory
#
def run():
	lol = []
	for x in range(0, 31):
		lol.append([])
	path = os.getcwd()
	print(path)
	path = "/Users/samuelvigneault/Desktop/images"
	dir_list = os.listdir(path)
	counter = 0
	poop = ""
	for file in dir_list:
		if file[0:5] == "spe-s":
			poop = int(file[12:14])
			index1 = int(file[10:12])
			lol[index1].append(poop)
	for x in range(0, 31):
		lol[x] = list(dict.fromkeys(lol[x]))
		lol[x] = sorted(lol[x])
		if lol[x] == [1,2,3,4,5,6,7,8,9,10,11,12]:
			lol[x] = [
	print("Files and directories in '", path, "' :")
	print(lol)
	#print(dir_list)

def main():
	run()
	print("made it")

main()
