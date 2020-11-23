import os
import sys

def main():
	path = "/Users/samuelvigneault/Desktop" + "/images"
	found = True
	while found:
		files_list = os.listdir(path)
		found = False
		for file in files_list:
			if file[0:3] == "spe":
				found = True
				os.rename(r'/Users/samuelvigneault/Desktop/images/' + file, r'/Users/samuelvigneault/Desktop/images/' + file[10:])
	path = "/Users/samuelvigneault/Desktop" + "/thumbs"
	found = True
	while found:
		files_list = os.listdir(path)
		found = False
		for file in files_list:
			if file[0:3] == "spe":
				found = True
				os.rename(r'/Users/samuelvigneault/Desktop/thumbs/' + file, r'/Users/samuelvigneault/Desktop/thumbs/' + file[10:])


main()