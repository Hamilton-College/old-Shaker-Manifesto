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
		string_out += "00" + str(counter) + ", "
	elif counter < 100:
		string_out += "0" + str(counter) + ", "
	else:
		string_out += str(counter) + ", "
	return string_out

def remover(str1):
	while "\n" in str1:
		str1 = str1.replace("\n", " ")
	while "\r" in str1:
		str1 = str1.replace("\r", " ")
	while "\r\n" in str1:
		str1 = str1.replace("\r\n", " ")
	while "\t" in str1:
		str1 = str1.replace("\t", " ")
	while "\"" in str1:
		str1 = str1.replace("\"", "'")
	while "  " in str1:
    		str1 = str1.replace("  ", " ")
	return str1

def persname(text1):
	string_out = "\""
	article = 0
	for i in range(0, len(text1)):
		if article == 0 and text1[i:i + 4] == "reg=":
			article = 4
		elif article == 4 and text1[i] == "\"":
			article = 5
		elif article == 5 and text1[i] == "\"":
			break
		elif article == 5:
			string_out += text1[i]
	string_out += "\", "
	COUNTER = 0

	for i in range(len(text1)-1, -1, -1):
		if text1[i] == ">":
			break
		else:
			COUNTER += 1

	string_out += "\"" + remover(text1[len(text1)-COUNTER:]) + "\""
	return(string_out)

def extract_text(text, file):
	counter = 0
	text_file  = "SQL.txt"
	f = open(text_file, "a")
	article = 0
	text1 =  ""
	auth = False
	for i in range(0, len(text)):
		if article == 0:
			string_out = naming(file, counter)
			article = 1
			text1 = ""
			auth = False
		if article == 1 and text[i:i+5] == "type=":
			article = 2
		elif article == 2 and text[i:i+9] == "<persName":
			article = 3
		elif article == 3 and (text[i:i+11] == "</persName>" or text[i:i+9] == "</byline>"):
			article = 7
			string_out += persname(text1)
			auth = True
		elif article == 3:
			text1 += text[i]
		elif text[i:i+3] == "<p ":
			article = 70
		elif article == 70 and text[i] == ">":
			article = 8
		elif text[i:i+3] == "<p>":
			article = 8
		elif article == 8 and text[i:i+4] == "</p>":
			article = 0
			counter += 1
			if auth:
				string_out += ");" + "\n"
				f.write(string_out)
			else:
				string_out += "\"None\", \"None\");"+ "\n"
				f.write(string_out)
			print(string_out)
	f.close()




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
