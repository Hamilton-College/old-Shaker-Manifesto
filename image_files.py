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
			lol[x] = []
	print("Files and directories in '", path, "' :")
	print(lol)
	#print(dir_list)

def naming(file, counter):
	string_out = "INSERT INTO authors (id, regauthor, author) VALUES (" + file[10:14]
	if counter < 10:
		string_out += "00" + str(counter) + ","
	elif counter < 100:
		string_out += "0" + str(counter) + ","
	else:
		string_out += str(counter) + ","
	return string_out

def extract_text(text, file):
	counter = 0
	text_file  = "SQL_insert.txt"
	article = 10
	text1 =  ""
	for i in range(0, len(text)):
		if article == 10:
			string_out = naming(file, counter)
			reg = ""
			auth = ""
		if text[i:i+5] == "type=":
			article = 0
		elif article == 0 and text[i:i+9] == "<persName":
			article = 1
		elif article == 1 and text[i:i+4] == "reg=":
			article = 2
			count = 0
			while text[i+4+count] != " ":
				string_out += text[i+4+count]
		elif text[i:i+3] == "<p ":
			article = 4
		elif article == 4 and text[i] == ">":
			article = 5
		elif text[i:i+3] == "<p>":
			article = 5
		elif article == 5 and text[i:i+4] == "</p>":
			article = 10
			counter += 1
		elif article == 5:
			text1 += text[i]




def run1():
	path = os.getcwd() +  "/journals"
	dir_list = os.listdir(path)
	for file in dir_list:
		lol = open(path + "/" + file)
		print(file)
		if file[0:3] == "spe":
			text = lol.read()
			extract_text(text, file)

def main():
	run1()
	print("made it")

main()
