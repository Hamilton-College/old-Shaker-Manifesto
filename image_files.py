import os
import sys

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

def space_remover(str1):
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

def div_type(text):
	article = 1
	string_out = ""
	counter = 0
	# Loops through text to catch all types in a div tag
	for i in range(0, len(text)):
		if counter > 0:
			counter -= 1
		elif article == 1 and text[i:i + 6] == "type=\"":
			article = 21
			counter = 5
		elif article == 21 and text[i] == "\"":
			break
		elif article == 21:
			string_out += text[i].lower()
	return string_out

def ind_info(text):
	article = 1
	string_out = ""
	counter = 0
	# Loops through text to catch all types in a div tag
	for i in range(0, len(text)):
		if counter > 0:
			counter -= 1
		elif article == 1 and text[i:i+8] == "level1=\"":
			article = 21
			counter = 7
		elif article == 21 and text[i] == "\"":
			break
		elif article == 21:
			string_out += text[i]
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

def find_tag(text):
	text = text.lower()
	tags = ["div2", "div3", "div4", "div5", "byline", "p", "index", "persname",
		"dateline", "head", "cit", "bibl", "quote", "pb", "pb/", "!--"]
	for i in range(0, len(text)):
		if text[i] == " " or text[i] == ">":
			text = text[:i]
			break
	if text not in tags and text[1:] not in tags:
		print("ISSUE", text)
		return ""
	return text

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

def list_to_str_articles(list):
	return

def out_list(listing):
	return

def create_text_file(counter, file, text):
	count = ""
	if counter < 10:
		count = "00" + str(counter)
	elif counter < 100:
		count = "0" + str(counter)
	elif counter < 1000:
		count = str(counter)
	text_name = file[10:14] + count + ".txt"
	complete_name = os.path.join(os.getcwd() + "/textfiles/", text_name)
	text_file = open(complete_name, "a")
	text_file.truncate(0)
	text_file.write(space_remover(text))
	text_file.close()
	return

def read_pers(text):
	return ""


def create_article(level2, level3, level4, level5, level, counter, file):
	print("CREATED AN ARTICLE!!!")
	level2[2] = space_remover(level2[2])
	level2[12] = space_remover(level2[12])
	level3[2] = space_remover(level3[2])
	level3[12] = space_remover(level3[12])
	level4[2] = space_remover(level4[2])
	level4[12] = space_remover(level4[12])
	level5[2] = space_remover(level5[2])
	level5[12] = space_remover(level5[12])
	if level == 2:
		create_text_file(counter, file, level2[12])
	elif level == 3:
		create_text_file(counter, file, level3[12])
	elif level == 4 or level == 5:
		create_text_file(counter, file, level4[12])
	elif level == 5:
		create_text_file(counter, file, level5[12])
	#print(level2)
	#print(level3)
	#print(level4)
	#print(level5)
	return []

def output_articles(text, file):
	# found tags order
	tags =[]
	# depth of div
	level1 = 0
	# div types
	# [type - 0, head-index-tag - 1, head-text - 2, authors-tag(sep by colon)- 3, author - text - 4
	# list of dateline-tag - 5, list  of dateline - text-6, list of names tag -7, list of name text - 8
	# list of bibliography-tag- 9, list of bibliography-text 10,
	# list of quote - 11, text - 12, sp - 13, cp - 14]
	level2 = ["", "", "", "", "", [], [], [], [], [], [], [], "", 0, 0]
	level3 = ["", "", "", "", "", [], [], [], [], [], [], [], "", 0, 0]
	level4 = ["", "", "", "", "", [], [], [], [], [], [], [], "", 0, 0]
	level5 = ["", "", "", "", "", [], [], [], [], [], [], [], "", 0, 0]
	level = level2

	quotebuff = ""
	biblbuff = ""
	namebuff = ""
	datebuff = ""

	# start page
	sp = 0
	# current page
	cp = 0
	#num of char to skip
	skipper = 0
	# skip until closing
	skipper1 = ""

	# 1, read byline, waiting for author (persname)
	# 2, reading heading/title, waiting for index
	# 3, reading quote
	# 4, reading bibl
	# 5, reading regular text
	# 6 , reading date
	stage = [0]
	articles = []
	counter = 0
	comment = False
	closing = False
	for i in range(0, len(text)):
		if comment:
			if text[i:i+3] == "-->":
				comment = False
				closing = True
		elif text[i] == "<" and not closing:
			tag = find_tag(text[i+1:i+12])
			tags.append(tag)
			skipper = len(tag)
			if skipper == 0: return
			level[12] += " "
			closing = True
			if tag[0] == "/":
				if tag[1:] == "div2":
					level[14] = cp
					articles.append(create_article(level2, level3, level4, level5, level1, counter, file))
					level2 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0]
					level = level2
					level1 = 2
					counter += 1
				elif tag[1:] == "div3":
					level[14] = cp
					articles.append(create_article(level2, level3, level4, level5, level1, counter, file))
					level3 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0]
					level = level2
					level1 = 2
					counter += 1
				elif tag[1:] == "div4":
					level[14] = cp
					articles.append(create_article(level2, level3, level4, level5, level1, counter, file))
					level4 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0]
					level = level3
					level1 = 3
					counter += 1
				elif tag[1:] == "div5":
					level[14] = cp
					articles.append(create_article(level2, level3, level4, level5, level1, counter, file))
					level5 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0]
					level = level4
					level1 = 4
					counter += 1
				elif tag[1:] == "byline":
					print(stage, text[i])
					print("byline")
					stage.pop(-1)
				elif tag[1:] == "head":
					print(stage, text[i])
					print("head")
					stage.pop(-1)
				elif tag[1:] == "p":
					print(stage, text[i:i+25])
					print("p")
					stage.pop(-1)
				elif tag[1:] == "quote":
					level[11].append(space_remover(quotebuff))
					print(stage, text[i])
					print("quote")
					stage.pop(-1)
				elif tag[1:] == "bibl":
					level[10].append(space_remover(biblbuff))
					print(stage, text[i])
					print("bibl")
					stage.pop(-1)
				elif tag[1:] == "dateline":
					level[6].append(datebuff)
					print(stage, text[i])
					print("date")
					stage.pop(-1)
				elif tag[1:] == "persname":
					if stage[-1] == 7:
						stage.pop(-1)
						level[8].append(namebuff)
				elif tag[1:] == "cit":
					stage = stage
			elif tag == "div2":
				level = level2
				level[0] = div_type(text[i:i+500])
				level[13] = cp
				level1 = 2
			elif tag == "div3":
				level2 = level
				level = level3
				level[0] = div_type(text[i:i + 500])
				level[13] = cp
				level1 = 3
			elif tag == "div4":
				level3 = level
				level = level4
				level[0] = div_type(text[i:i + 500])
				level[13] = cp
				level1 = 4
			elif tag == "div5":
				level = level5
				level[0] = div_type(text[i:i + 500])
				level[13] = cp
				level1 = 5
			elif tag == "!--":
				print("COMMENT")
				comment = True
			elif tag == "byline":
				stage.append(1)
			elif tag == "head":
				stage.append(2)
			elif tag == "p":
				stage.append(5)
			elif tag == "quote":
				stage.append(3)
			elif tag == "bibl":
				stage.append(4)
			elif tag == "dateline":
				stage.append(6)
			elif tag == "persname":
				if not (stage[-1] == 1):
					stage.append(7)
					level[7].append(read_pers(text[i:i + 500]))
				else:
					level[3] += read_pers(text[i:i + 500])
			elif tag == "index":
				ind = ind_info(text[i+1:i+160])
			elif tag == "pb":
				cp += 1
				found = False
				for j in range(0, 100):
					if text[i+1+j:i+5+j] == "id=\"p":
						if int(text[i+5+j]) != cp:
							print("NOT EQUAL", cp, int(text[i+5+j]))
			elif tag == "pb/":
				cp = cp + 1
			elif tag == "cit":
				cp = cp
		elif closing and text[i] == ">":
			closing = False
		elif not closing:
			if stage[-1] == 1:
				level[4] += text[i]
			elif stage[-1] == 2:
				level[2] += text[i]
			elif stage[-1] == 3:
				quotebuff += text[i]
			elif stage[-1] == 4:
				biblbuff += text[i]
			elif stage[-1] == 6:
				datebuff += text[i]
			elif stage[-1] == 7:
				namebuff += text[i]
			#elif stage[-1] == 0:
				#print("STAGE RAN OUT OF STAGES :(", stage)
			level[12] += text[i]


def body_read(text, file, output):
	buffer = ""
	for i in range(0, len(text)):
		if text[i:i + 5] == "<div2" or text[i:i + 4] == "<!--":
			buffer = text[i:]
			break
	output_list = output_articles(buffer, file)
	#output_str = list_to_str_articles(output_list)
	#output.write(output_str)
	return


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

def main():
	path = os.getcwd() + "/journals"
	files_list = os.listdir(path)
	body_reader(files_list, path)
	print("made it")

main()
