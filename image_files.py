import os
import sys

# Get the list of all files and directories
# in the root directory

def read_div(text):
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

def read_index(text):
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

def read_pers(text):
	article = 1
	string_out = ""
	counter = 0
	# Loops through text to catch all types in a div tag
	for i in range(0, len(text)):
		if counter > 0:
			counter -= 1
		elif article == 1 and text[i:i + 5] == "reg=\"":
			article = 21
			counter = 7
		elif article == 21 and text[i] == "\"":
			break
		elif article == 21:
			string_out += text[i]
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

def find_tag(text):
	text = text.lower()
	tags = ["div2", "div3", "div4", "div5", "byline", "p", "index", "persname",
		"dateline", "head", "cit", "bibl", "quote", "pb", "pb/", "!--"]
	if text[0:3] == "!--":
		return text[0:3]
	for i in range(0, len(text)):
		if text[i] == " " or text[i] == ">" or text[i] == "\n":
			text = text[:i]
			break
	if text not in tags and text[1:] not in tags:
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


def list_to_str_articles1(list1, key):
	str1 = "("
	str1 += key + ", "
	str1 += key[0:4] + ", "
	#str1 += "\"" + list1[9] + "\", "
	str1 += "\"" + key + "\", "
	str1 += "\"" + key + "\", "
	return

def list_to_str_articles4(list1, list2, list3, list4):
	str1 = ""

	return

def out_list(listing):
	return

def key_creator(counter, file):
	count = ""
	if counter < 10:
		count = "00" + str(counter)
	elif counter < 100:
		count = "0" + str(counter)
	elif counter < 1000:
		count = str(counter)
	return file[10:14] + count

def create_text_file(key, text):
	text_name = key + ".txt"
	complete_name = os.path.join(os.getcwd() + "/textfiles/", text_name)
	text_file = open(complete_name, "a")
	text_file.truncate(0)
	text_file.write(space_remover(text))
	text_file.close()
	return

def checker(lister):
	#if len(lister[10]) > 1:
	#	print("HUGE ISSUES - DATE", len(lister[10]))
	return

def diction(str1, level1):
	dictio = {"plant":"crops",
		"the commications fo farmers...":"farming",
		"healthe":"health",
		"text":"other",
		"home":"house",
		"for the children":"juvenile",
		"nationalnews":"national-news",
		"nationalnews":"national-news",
		"worldnews":"world-news",
		"world news":"world-news",
		"world=news":"world-news",
		"shaker-reportt":"shaker-report",
		"shaker-reports":"shaker-report",
		"ashaker-report":"shaker-report",
		"shaker report":"shaker-report",
		"society record":"shaker-report",
		"poerm":"poem",
		"1883":"poem",
		"poetry":"poem",
		"aphorism":"saying",
		"sayings":"saying",
		"book notice":"book",
		"book-notice":"book",
		"books":"book",
		"lessons":"lesson",
		"bible class":"lesson",
		"instructions":"instruction",
		"death notices":"obituary",
		"deaths":"obituary",
		"obituaries":"obituary",
		"editorials":"editorial",
		"lette":"letter",
		"corresondence":"letter",
		"correspondences":"letter",
		"correspondence":"letter",
		"corresponce":"letter",
		"letters":"letter",
		"notes":"note",
		"sectio":"section",
		"sections":"section"}
	listing1 = ["equipment", "livestock", "recipe", "food", "shaker-press", "shaker-history", "history", "music",
		  "dance", "hymn", "humor", "fiction", "story", "figure", "lecture", "science", "publication",
		  "biography", "ann lee", "quote"]
	all_list = listing1
	all_list.append("other")
	for x in dictio:
		if dictio[x] not in all_list:
			all_list.append(dictio[x])
	all_list.remove("section")
	if original:
		if str1 in dictio:
			if dictio[str1] == "section":
				return diction(level1, "")
			else:
				return dictio[str1]
		elif str1 == "section":

		elif str1 in listing1:
			return str1
		return "other"


def create_article(level2, level3, level4, level5, level, counter, file):
	key = key_creator(counter, file)
	lol = [level2, level3, level4, level5]
	for i in lol:
		i[2] = space_remover(i[2])
		i[12] = space_remover(i[12])
		i[0] = dictio(i[0], i[1])
		checker(i)
	if level == 2:
		if level2[15] > 0:
			create_text_file(key, level2[12])
			return list_to_str_articles1(level2, key)
		else: return ""
	elif level == 3:
		if level3[15] > 0:
			level3[0] += ":" + level2[0]
			create_text_file(key, level3[12])
			return list_to_str_articles1(level3, key)
	elif level == 4:
		if level4[15] > 0:
			level4[0] += ":" + level3[0] + ":" + level2[0]
			create_text_file(key, level4[12])
			return list_to_str_articles1(level4, key)
	elif level == 5:

		if level5[15] > 0:
			level5[0] += ":" + level4[0] + ":" + level3[0] + ":" + level2[0]
			create_text_file(key, level4[12])
			return list_to_str_articles1(level4, key)
	return ""

# [type - 0, head-index-tag - 1, head-text - 2, authors-tag(sep by colon)- 3, author - text - 4
	# list of dateline-tag - 5, list  of dateline - text-6, list of names tag -7, list of name text - 8
	# list of bibliography-tag- 9, list of bibliography-text 10,
	# list of quote - 11, text - 12, sp - 13, cp - 14, text? - 15]
def output_articles(text, file):
	# found tags order
	tags =[]
	# depth of div
	level1 = 0
	# div types
	# [type - 0, head-index-tag - 1, head-text - 2, authors-tag(sep by colon)- 3, author - text - 4
	# list of dateline-tag - 5, list  of dateline - text-6, names tag -7, name text - 8
	# list of bibliography-tag- 9, list of bibliography-text 10,
	# list of quote - 11, text - 12, sp - 13, cp - 14, text? - 15]
	level2 = ["", "", "", "", "", [], [], "", "", [], [], [], "", 0, 0, 0]
	level3 = ["", "", "", "", "", [], [], "", "", [], [], [], "", 0, 0, 0]
	level4 = ["", "", "", "", "", [], [], "", "", [], [], [], "", 0, 0, 0]
	level5 = ["", "", "", "", "", [], [], "", "", [], [], [], "", 0, 0, 0]
	level = level2

	quotebuff = ""
	biblbuff = ""
	namebuff = ""
	datebuff = ""

	# current page
	cp = 0

	# 1, read byline (author) (persname) // 2, reading heading/title, waiting for index
	# 3, reading quote // 4, reading bibl
	# 5, reading regular text // 6, reading date
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
			if skipper == 0:
				return articles
			level[12] += " "
			closing = True
			if tag[0] == "/":
				if tag[1:4] == "div":
					level[14] = cp
					if tag[1:] == "div2":
						article = create_article(level2, level3, level4, level5, level1, counter, file)
						level2 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0, 0]
						level = level2
					elif tag[1:] == "div3":
						article = create_article(level2, level3, level4, level5, level1, counter, file)
						level3 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0, 0]
						level = level2
					elif tag[1:] == "div4":
						article = create_article(level2, level3, level4, level5, level1, counter, file)
						level4 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0, 0]
						level = level3
					elif tag[1:] == "div5":
						article = create_article(level2, level3, level4, level5, level1, counter, file)
						level5 = ["", "", "", "", "", [], [], [], [], [], [],[], "", 0, 0, 0]
						level = level4
					level1 = int(tag[4]) - 1
					counter += 1
				elif tag[1:] == "byline" or tag[1:] == "head" or tag[1:] == "p":
					stage.pop(-1)
				elif tag[1:] == "quote" or tag[1:] == "bibl" or tag[1:] == "dateline":
					stage.pop(-1)
					if tag[1:] == "bibl":
						level[10].append(space_remover(biblbuff))
					elif tag[1:] == "dateline":
						level[6].append(space_remover(datebuff))
					elif tag[1:] == "quote":
						level[11].append(space_remover(quotebuff))
				elif tag[1:] == "persname" and stage[-1] == 7:
					stage.pop(-1)
					level[8] = (space_remover(namebuff))
			elif tag[0:3] == "div":
				if tag == "div2":
					level = level2
				elif tag == "div3":
					level2 = level
					level = level3
				elif tag == "div4":
					level3 = level
					level = level4
				elif tag == "div5":
					level = level5
				level[0] = read_div(text[i:i + 500])
				level1 = int(tag[3])
				level[13] = cp
			elif tag == "!--":
				comment = True
			elif tag == "byline":
				stage.append(1)
			elif tag == "head":
				stage.append(2)
			elif tag == "p":
				level[15] += 1
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
					level[7] = (read_pers(text[i:i + 500]))
				else:
					level[3] += read_pers(text[i:i + 500])
			elif tag == "index":
				ind = read_index(text[i+1:i+1000])
				if stage[-1] == 2:
					level[1] = ind
				elif stage[-1] == 4:
					level[9] += ":" + ind
			elif tag == "pb":
				cp += 1
				found = False
				for j in range(0, 100):
					if text[i+1+j:i+5+j] == "id=\"p":
						if int(text[i+5+j]) != cp:
							print("NOT EQUAL", cp, int(text[i+5+j]))
			elif tag == "pb/":
				cp = cp + 1
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
			level[12] += text[i]

def body_read(text, file, output):
	buffer = ""
	for i in range(0, len(text)):
		if text[i:i + 5] == "<div2" or text[i:i + 4] == "<!--":
			buffer = text[i:]
			break
	output_list = output_articles(buffer, file)
	#print(output_list)
	#output_str = list_to_str_articles(output_list)
	#output.write(output_str)
	return mylist


def body_reader(files_list, path):
	section = []
	articles_name = "SQL_articles.txt"
	articles_file = open(articles_name, "a")
	articles_file.truncate(0)
	for file in files_list:
		lol = open(path + "/" + file)
		if file[0:3] == "spe":
			print(file)
			file_text = lol.read()
			lolol = body_read(file_text, file, articles_file)
			for i in lolol:
				if i not in section:
					section.append(i)
	print(section)

def main():
	path = os.getcwd() + "/journals"
	files_list = os.listdir(path)
	body_reader(files_list, path)
	print("made it")

main()
