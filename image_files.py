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
	string_out = "INSERT INTO authors (id, type, regauthor, author) VALUES (" + file[10:14]
	if counter < 10:
		string_out += "00" + str(counter) + ", "
	elif counter < 100:
		string_out += "0" + str(counter) + ", "
	else:
		string_out += str(counter) + ", "
	return string_out

def author_remover(str1):
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
	if len(str1) != 0:
		while str1[0] == " ":
			str1 = str1[1:]
			if len(str1) == 0:
				break
	if len(str1) != 0:
		while str1[-1] == " ":
			str1 = str1[:-1]
			if len(str1) == 0:
				break
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

def run1():
	path = os.getcwd() +  "/journals"
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

def find_tag(text):
	text = text.lower()
	tags = ["div2", "div3", "div4", "div5", "byline", "p", "index", "persname",
		"dateline", "head", "cit", "bibl", "quote", "pb", "pb/"]
	for i in range(0, len(text)):
		if text[i] == " " or text[i] == ">":
			text = text[:i]
			break
	if text not in tags and text[1:] not in tags:
		print("ISSUE", text)
		return
	return text

def list_to_str_articles(list):
	return

def create_article():
	return

def output_articles(text, file):
	levelers = ["div2", "div3", "div4", "div5"]
	tags =[]
	level = 0
	level1 = []
	level2 = []
	level3 = []
	level4 = []
	quote = []
	dateline = []
	bibl = []
	sp = 0
	cp = 0
	para =[]
	skipper = 0
	state = 0
	closed = False
	articles = []
	for i in range(0, len(text)):
		if skipper > 0:
			skipper -= 1
		elif text[i] == "<":
			tag = find_tag(text[i+1:i+10])
			skipper = len(tag)
			if tag[0] == "/":
				if tag[1:] in levelers:
					if not closed:
						articles.append(create_article())
						closed = True
			elif tag == "pb":
				cp += 1
				found = False
				for j in range(0, 100):
					if text[i+1+j:i+5+j] == "id=\"p":
						if int(text[i+5+j]) != cp:
							print("NOT EQUAL", cp, int(text[i+5+j]))
			elif tag == "pb/":
				cp = cp



def body_read(text, file, output):
	buffer = ""
	for i in range(0, len(text)):
		if text[i:i + 7] == "<div1>":
			buffer = text[i+7:]
	output_list = output_articles(buffer, file)
	#output_str = list_to_str_articles(output_list)
	#output.write(output_str)
	return

def between(filetext, index):
	stage = 0
	buffer = ""
	for i in range(0, len(filetext)):
		if filetext[index+i] == ">" and stage == 0:
			stage = 1
		elif filetext[index+i] == "<" and stage == 1:
			break
		elif stage == 1:
			buffer += filetext[index+i]
	return buffer

def output_issues(text, file):
	stage = 0
	listing = []
	listing.append(int(file[10:14]))
	listing.append(int(file[10:12]))
	listing.append(int(file[12:14]))
	for i in range(0, len(text)):
		if text[i:i+10] == "<fileDesc " and stage == 0:
			stage = 1
		elif text[i:i+7] == "<title " and stage == 1:
			stage = 2
			listing.append(between(text, i+7))
		elif text[i:i+7] == "<editor" and stage == 2:
			listing.append("Lomas, G. A.")
			stage = 3
		elif text[i:i+7] == "<extent" and stage == 3:
			stage = 4
			listing.append(int(between(text, i+7)))
		elif text[i:i+7] == "<extent" and stage == 2:
			listing.append("None")
			stage = 4
			listing.append(int(between(text, i+7)))
		elif text[i:i+11] == "<sourceDesc" and stage == 4:
			stage = 5
		elif text[i:i+10] == "<publisher" and stage == 5:
			stage = 6
			listing.append(between(text, i+10))
		elif text[i:i+9] == "<pubPlace" and stage == 6:
			stage = 7
			listing.append(between(text, i+9))
		elif text[i:i+5] == "<date" and stage == 7:
			stage = 8
			listing.append(between(text, i+9))
		elif text[i:i+7] == "value=\"" and stage == 8:
			listing.append(int(text[i+7:i+11]))
			listing.append(int(text[i + 11:i + 13]))
	return listing

def list_to_str_issues(listing):
	buffer = "INSERT INTO issues (id, volume, issue, title, editor, pages, publisher, pubplace, date, year, month) VALUES ("
	for i in range(0, len(listing)-1):
		if type(listing[i]) == int:
			buffer += str(listing[i])
		else:
			buffer += "\"" + listing[i] + "\""
		buffer += ", "
	buffer += str(listing[-1]) + ")" + "\n"
	return buffer

def header_read(text, file, output):
	buffer = ""
	for i in range(0, len(text)):
		if text[i:i+7] == "</div1>":
			buffer = text[0:i]
	output_list = output_issues(buffer, file)
	output_str = list_to_str_issues(output_list)
	output.write(output_str)

def issues_reader(files_list, path):
	issues_name = "SQL_issues.txt"
	issues_file = open(issues_name, "a")
	issues_file.truncate(0)
	for file in files_list:
		lol = open(path + "/" + file)
		if file[0:3] == "spe":
			file_text = lol.read()
			header_read(file_text, file, issues_file)

def body_reader(files_list, path):
	articles_name = "SQL_articles.txt"
	articles_file = open(articles_name, "a")
	articles_file.truncate(0)
	for file in files_list:
		lol = open(path + "/" + file)
		if file[0:3] == "spe":
			print(file)
			file_text = lol.read()
			body_read(file_text, file, articles_file)
			break

def main():
	path = os.getcwd() + "/journals"
	files_list = os.listdir(path)
	#issues_reader(files_list, path)
	body_reader(files_list, path)
	print("made it")

main()
