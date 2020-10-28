import os
import sys

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
	print(lol)

def naming(file, counter):
	string_out = "INSERT INTO authors (id, type, regauthor, author) VALUES (" + file[10:14]
	if counter < 10:
		string_out += "00" + str(counter) + ", "
	elif counter < 100:
		string_out += "0" + str(counter) + ", "
	else:
		string_out += str(counter) + ", "
	return string_out

def run1():
	path = os.getcwd() + "/journals"
	dir_list = os.listdir(path)
	listing222 = []
	listing444 = []
	for file in dir_list:
		lol = open(path + "/" + file)
		print(file)
		if file[0:3] == "spe":
			text = lol.read()
			listing111, listing333 = extract_text(text, file)
			for i in listing111:
				if i not in listing222:
					listing222.append(i)
			for i in listing333:
				if i not in listing444:
					listing444.append(i)
	print(listing222)
	print(listing444)

def run111():
	path = os.getcwd() + "/journals"
	dir_list = os.listdir(path)
	listing222 = []
	for file in dir_list:
		lol = open(path + "/" + file)
		print(file)
		if file[0:3] == "spe":
			texting3 = lol.read()
			text_file = "journals.txt"
			f = open(text_file, "a")
			f.write(texting3)
	f.close()

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
	string_out += "\"" + author_remover(text1[len(text1)-COUNTER:]) + "\""
	return(string_out)

def extract_text(text, file):
	counter = 0
	text_file  = "SQL.txt"
	f = open(text_file, "a")
	article = 0
	text1 = ""
	auth = False
	listing111 = []
	listing333 = []

	# Loops through text to catch all articles and tags
	for i in range(0, len(text)):
		if article == 0:
			checker = ""
			string_out = naming(file, counter)
			article = 1
			text1 = ""
			auth = False
		elif article == 1 and text[i:i+5] == "type=":
			article = 21
		elif article == 21 and text[i] == "\"":
			article = 22
			string_out += "\""
		elif article == 22 and text[i] == "\"":
			article = 2
			string_out += "\", "
			if checker not in listing111:
				listing111.append(checker)
		elif article == 22:
			string_out += text[i].lower()
			checker += text[i].lower()
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
			#print(string_out)
		if text[i] == "<":
			found34 = False
			counter34 = 1
			while not found34:
				if text[i+counter34] == " " or text[i+counter34] == ">":
					found34 = True
					if text[i+1] == "/":
						lolol12 = text[i+2:i+counter34]
					else:
						lolol12 = text[i+1:i+counter34]
					if lolol12 not in listing333:
						listing333.append(text[i+1:i+counter34])
				counter34 += 1
	listing333.sort()
	f.close()
	return listing111, listing333