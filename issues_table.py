import os
import sys

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
		if text[i:i+4] == "<div1":
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


def main():
	path = os.getcwd() + "/journals"
	files_list = os.listdir(path)
	issues_reader(files_list, path)
	print("made it")

main()
