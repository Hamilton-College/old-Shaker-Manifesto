import os, sys, json, re, ast, io
from functools import reduce

from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from urllib.parse import urlparse
from ngram_search import *
from autocomplete import *
import urllib.parse 

from base64 import encodebytes #For sending images
from PIL import Image
from waitress import serve

images_dir = os.path.join("..", "C:/images")#"C:\\Users\\nonso\\OneDrive\\Documents\\images\\images\\"
template_dir = os.path.abspath("./flask-server/templates")
static_dir = os.path.abspath("./flask-server/static")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir )
CORS(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"#"csteam"
app.config["MYSQL_PASSWORD"] = "root" #"Lib-CS-Collab"
app.config["MYSQL_DB"] = "shaker"
mysql = MySQL(app)

#GLOBAL Search Obj
searchObj = SM_Search()


# BASIC SEARCH

# POST is to send/change data.
@app.route("/", methods=["POST", "GET"])
def basicSearch():
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(request.form.get("query").strip() == ""): # if nothing typed in the search bar
            return render_template("index.html") # stay on the page

        enteredText = request.form["query"] # name in brackets matches the name of the post form in the HTML

        firstPage = searchObj.search(enteredText) # when you call search. It's just the 1st page
        if(not firstPage):
            firstPage = "None"
            return redirect(url_for("basicResults1", values=enteredText, results = firstPage, numOfPages = 0, page = 0))

        else:
            numOfPages = searchObj.page_num()
            searchResults = searchObj.store_results() # store as jsonified string so that we can pass it through urls
            searchResults = urllib.parse.quote_plus(searchResults)# encode results for URL passing
            return redirect(url_for("basicResults1", values=enteredText, results = searchResults, numOfPages = numOfPages, page = 1))


# ARTICLE TYPE SEARCH

@app.route("/ArticleType", methods=["POST", "GET"])
def displayTypes():
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(request.form.get("query").strip() == "" and not request.form.get("checkbox")): # if no boxes checked and nothing entered
            return render_template("index.html") # stay on page

        elif(request.form.get("checkbox") and request.form.get("query").strip() != ""): # Typical: If we have a box checked and word entered
            enteredText = request.form.get("query")
            topic = request.form.get("checkbox")[:request.form.get("checkbox").index(";")]
            topicID = request.form.get("checkbox")[request.form.get("checkbox").index(";")+1:]
            queryString = f"SELECT id FROM articles WHERE topics LIKE '%{topic}%' order by author_tag;"
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()

            idList = list(fetchdata)
            idList = [list(i) for i in idList]
            idList = [j for i in idList for j in i] # flatten

            global searchObj

            firstPage = searchObj.search(enteredText, idList) # when you call search. It's just the 1st page
            print(idList)
            print(firstPage)
            if(not firstPage): # no results
                firstPage = "None"
                return redirect(url_for("topicWordResults", topic = topicID, word = enteredText, results = firstPage, numOfPages = 0, page = 0))
            else:
                numOfPages = searchObj.page_num()
                searchResults = searchObj.store_results() # store as jsonified string so that we can pass through urls
                searchResults = urllib.parse.quote_plus(searchResults) # encode results for URL passing
                return redirect(url_for("topicWordResults", topic = topicID, word = enteredText, results = searchResults, numOfPages = numOfPages, page = 1))


        elif(request.form.get("checkbox")): # just a box checked, nothing typed
            topic = request.form.get("checkbox")[:request.form.get("checkbox").index(";")]
            topicID = request.form.get("checkbox")[request.form.get("checkbox").index(";")+1:]
            queryString = f"SELECT title, author_tag, id FROM articles WHERE topics LIKE '%{topic}%' order by author_tag;"
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()
            return redirect(url_for("topicResults", topic = topicID, results = fetchdata))

        else: # if no checkboxes checked, and just text entered. work like basic
            enteredText = request.form["query"]

            firstPage = searchObj.search(enteredText) # when you call search. It's just the 1st page
            if(not firstPage): # if no results for that word
                firstPage = "None"
                return redirect(url_for("basicResults1", values=enteredText, results = firstPage, numOfPages = 0, page = 0))
            else:
                numOfPages = searchObj.page_num()
                searchResults = searchObj.store_results() # store as jsonified string so that we can pass it through urls
                searchResults = urllib.parse.quote_plus(searchResults)# encode results for URL passing
                return redirect(url_for("basicResults1", values=enteredText, results = searchResults, numOfPages = numOfPages, page = 1)) # put in the function of the url you want to go to


# AUTHOR SEARCH
@app.route("/Author", methods=["POST", "GET"])
def displayAuthors():
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(request.form.get("letter")): # letter button is clicked
            letter = request.form["letter"]
            queryString = f"SELECT author_tag FROM articles WHERE author_tag LIKE '{letter}%' OR author_tag LIKE '%; {letter}%' group by author_tag;" # add author to select
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()
            return redirect(url_for("letterOfAuthors", letter = letter, query=fetchdata))
        else: # name was entered
            name = request.form.get("query").strip()
            if(name == ""):
                return render_template("index.html")
            if(" " in name): # this means a first and last name entered or multiple names
                nameList = name.split()
                if(len(nameList) == 2):
                    queryString = f"SELECT title, author_tag, id FROM articles WHERE author_tag LIKE '%{nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' order by author_tag;"
                elif(len(nameList) == 3):
                    queryString = f"SELECT title, author_tag, id FROM articles WHERE author_tag LIKE '%{nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && author_tag like '%{nameList[2]}%' order by author_tag;"
            elif(len(name) == 1):
                queryString = f"SELECT title, author_tag, id FROM articles WHERE author_tag LIKE '%, {name}%' group by author_tag;" # add author to select
            else: # either someone's first or last name was displayed. Not both
                queryString = f"SELECT title, author_tag, id FROM articles WHERE author_tag LIKE '%, {name}%' OR author_tag LIKE '{name}%' order by author_tag;" # add author to select
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()
            return redirect(url_for("authorResults", letterOrName = name, query=fetchdata))

# AUTHOR FIRST LETTER
@app.route("/AuthorNames/<letter>~<query>", methods=["POST", "GET"])
def letterOfAuthors(letter, query): # This gives us all the authors of the clicked letter
    multipleNames = False
    if(query != "()"):
        query = query.replace("(", "")
        query = query.replace(",)", "")
        query = query.replace(")", "") # this gets rid of the last )
        if(";" in query):
            multipleNames = True
        query = re.split("', |\", |,, |;", query)

        if(multipleNames == True): # this is to get rid of the authors that don't begin with the chosen letter
            ind = 0
            while(ind < len(query)):
                query[ind] = query[ind].strip()
                if(query[ind][0] != letter and query[ind][1] != letter):
                    query.pop(ind)
                else:
                    ind += 1

        # get rid of ' on last item
        query[-1] = query[-1][:-1]
        for i in range(len(query)):
            if('"' in query[i]):
                query[i] = query[i].replace('"', "")
            if(query[i][0] == "'"):
                query[i] = query[i][1:]
            query[i] = query[i].split(",")


        for i in range(len(query)):
            if(len(query[i]) > 1):
                query[i][0] = query[i][0] +","

        query = set(tuple(i) for i in query) # get rid of any possible dups (there shouldn't be any)
        query = list(query)

        namesOfLetter = query
        query.sort()
    else: # query = () meaning empty meaning no authors
        namesOfLetter = []
    return render_template("index.html", firstLetter = letter, namesOfLetter=namesOfLetter)

# AUTHOR NAMES
@app.route("/AuthorNames", methods=["POST", "GET"])
def displayNames(): # display author articles When user clicks on an author's name,
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        undefined = False
        name = request.form["name"]

        if(name[-9:] == "undefined"):
            name = name[:-9]
            undefined = True
        name = name.replace("'", "''") # double up the apostrophre in SQL to escape it
        nameList = name.split(", ")

        if(undefined==True): # one name author, single letter, etc
            queryString = f"SELECT title, author_tag, id FROM articles WHERE author_tag LIKE '{name}' order by author_tag;" # add author to select

        elif(len(nameList) == 2):
            queryString = f"SELECT title, author_tag, id FROM articles WHERE (author_tag LIKE '{nameList[0]}%' && author_tag LIKE '%, {nameList[1]}%') OR (author_tag LIKE '%; {nameList[0]}%' && author_tag LIKE '%, {nameList[1]}%') order by author_tag;"# either the last name appears first or it appears after a semicolon

        else: # one word name
            queryString = f"SELECT title, author_tag, id FROM articles WHERE author_tag LIKE '%{name}%' order by author_tag;" # add author to select
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        fetchdata = curr.fetchall()
        curr.close()
        name = name.replace("''", "'")
        return redirect(url_for("authorResults", letterOrName = name, query=fetchdata)) # put in the function of the url you want to go to


# VOLUME & ISSUE SEARCH
@app.route("/VolumeIssue", methods=["POST", "GET"])
def displayVolumes():
    return render_template("index.html")

# RESULTS

# BASIC SEARCH RESULTS
@app.route("/Results/<values>/<results>/<numOfPages>/<page>", methods=["POST", "GET"])
def basicResults1(values=None, results=None, numOfPages=0, page=0):

    if(results=="None"): # no results for entered item
        return render_template("index.html", enteredTerm = values, results =results, pageNum = 0)# we're just passing enteredText to display it

    page = int(page) -1 # index begins at 0
    numOfPages = int(numOfPages)

    results = urllib.parse.unquote_plus(results) # decode the results
   
    searchObj.load_results(results) # results is a jsonified string. This just sets some of the internal state of SM obj

    pageOfResults = searchObj.generate_results(page) # results is our search obj
    for i in pageOfResults:
        i[1] = i[1].replace("\'", "")
        i[1] = i[1].replace('"', "")
        i[1] = i[1].replace("\\", "")
        i[1] = i[1].replace("<!b>", "</b>")
        queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{int(i[0])}';"
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        titleAuthor = curr.fetchall()
        curr.close()
        titleAuthor = list(titleAuthor)

        titleAuthor[0] = list(titleAuthor[0])

        if(titleAuthor[0][0] == ""):
            titleAuthor[0][0] = "Title Unknown"
        i.append(titleAuthor[0][0]) # Here, we are appending the Article title

        if(titleAuthor[0][1] == ""):
            titleAuthor[0][1] = "Author Unknown"
            i.append(titleAuthor[0][1])
        else:
            author = titleAuthor[0][1].split(", ")
            i.append(", ".join(author))

    pageList = [str(i) for i in range(1, numOfPages+1)]
    return render_template("index.html", enteredTerm = values, results =pageOfResults, pageButtons=pageList, pageNum = page+1)# we're just passing enteredText to display it


@app.route("/TopicResults/<topic>~<results>", methods=["POST", "GET"])
def topicResults(topic=None, results =None): # all articles related to a certain topic. We come here when button is checked, but no text is entered.

    results = ast.literal_eval(results)
    results = list(results)
    results = [list(i) for i in results]

    for i in results:
        if(i[0] == ""):
            i[0] = "Title Unknown"
        if(i[1] == ""):
            i[1] = "Author Unknown"
    results.sort()

    return render_template("index.html", topic=topic, topicResults=results)

@app.route("/ArticleResults/<articleID>", methods=["POST", "GET"])
def articleResults(articleID=None): # Open the text and image file of the article
    queryString = f"SELECT start FROM articles WHERE id LIKE '{int(articleID)}';"
    curr = mysql.connection.cursor()
    curr.execute(queryString)
    startPage = list(curr.fetchall())
    print(startPage)
    print(startPage[0])
    curr.close()
    startPage = startPage[0][0]
    startPage += 1 # image files are 1-indexed
    print(startPage)

    if(len(articleID)==6):
        articleID = "0" + articleID
        textStart = articleID[:4] + "000"
    else: # ID length is 7
        textStart = articleID[:4] + "000"

    curr = textStart
    issueText = ""
    while(os.path.exists(f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{str(curr)}.txt")):
        path = f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{str(curr)}.txt"
        articleText = open(path, "r")
        articleText = articleText.read()
        if(curr == articleID):
            if(articleID[-3:] == "000"): # if first article in the issue
                issueText += "<b>" + articleText+ " </b>" + "<br/> <br/> <br/>"
            else: # everything else
                issueText += ("<div id=\"target\">  </div>" + "<b>" + articleText+ " </b>" + "<br/> <br/> <br/>")
        else:
            issueText += (articleText + "<br/> <br/> <br/>")
        curr = int(curr) + 1 # lose leading zero
        if(len(str(curr))==6):
            curr = "0" + str(curr)
        else: # 7
            curr = str(curr)

    # replace non-UTF8 chars
    issueText = issueText.replace('ï¿½', '�') # ?
    issueText = issueText.replace('.â€”', '—') # em dash
    issueText = issueText.replace('â€”', '—') # em dash
    issueText = issueText.replace("â€¢", '•') # dot
    issueText = issueText.replace("â€ž", '„') # quote

    # Get list of  image paths
    curr = textStart[:-1] + str(1) # images start at 1
    imagePaths = []
    while(os.path.exists(imgPath := os.path.join(images_dir, "{}.jpg".format(str(curr))))):
        imagePaths.append(imgPath)
        curr = int(curr) + 1
        if(len(str(curr))==6):
            curr = "0" + str(curr)# int() loses leading zero
        else: # 7
            curr = str(curr)

    encodedImages = []
    print(imagePaths)
    for i in range(len(imagePaths)):
        newResponseImg = get_response_image(imagePaths[i]).replace("\n", "\\n")
        encodedImages.append(newResponseImg)

    return render_template("index.html", articleText = issueText, articleID=articleID, images=encodedImages, startPage=startPage) # we need to pass in everything here b/c we only want to use one page

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='JPEG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img

@app.route("/VolumeIssueResults/<articleID>", methods=["POST", "GET"])
def volumeIssueResults(articleID=None): # Open the text and image file of the article
    if(len(articleID)==6):
        articleID = "0" + articleID
        textStart = articleID[:4] + "000"
    else: # ID length is 7
        textStart = articleID[:4] + "000"
    curr = textStart
    issueText = ""
    while(os.path.exists(f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{str(curr)}.txt")):
        path = f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{str(curr)}.txt"
        articleText = open(path, "r")
        articleText = articleText.read()
        issueText += (articleText + "<br/> <br/> <br/>")
        curr = int(curr) + 1 # lose leading zero
        if(len(str(curr))==6):
            curr = "0" + str(curr)
        else: # 7
            curr = str(curr)

    # replace non-UTF8 chars
    issueText = issueText.replace('ï¿½', '�') # ?
    issueText = issueText.replace('.â€”', '—') # em dash
    issueText = issueText.replace('â€”', '—') # em dash
    issueText = issueText.replace("â€¢", '•') # dot
    issueText = issueText.replace("â€ž", '„') # quote

    # Get list of  image paths
    curr = textStart[:-1] + str(1) # images start at 1
    imagePaths = []
    while(os.path.exists(imgPath := os.path.join(images_dir, "{}.jpg".format(str(curr))))):
        imagePaths.append(imgPath)
        curr = int(curr) + 1
        if(len(str(curr))==6):
            curr = "0" + str(curr)# int() loses leading zero
        else: # 7
            curr = str(curr)


    encodedImages = []
    print(imagePaths)
    for i in range(len(imagePaths)):
        newResponseImg = get_response_image(imagePaths[i]).replace("\n", "\\n")
        encodedImages.append(newResponseImg)

    return render_template("index.html", articleText = issueText, articleID=articleID, images=encodedImages) # we need to pass in everything here b/c we only want to use one page


@app.route("/TopicWordResults/<topic>/<word>/<results>/<numOfPages>/<page>", methods=["POST", "GET"])
def topicWordResults(topic=None, word=None, results=None, numOfPages =None, page=None): # all articles related to a certain topic
    if(results == "None"):
        return render_template("index.html", topic=topic, topicWord= word, topicWordResults=results, pageNum=0)
        
    else:
        page = int(page) -1 # index begins at 0
        numOfPages = int(numOfPages)

        results = urllib.parse.unquote_plus(results) # decode the results
        searchObj.load_results(results) # results is a jsonified string. This just sets some of the internal state of SM obj
        pageOfResults = searchObj.generate_results(page) # results is our search obj
        for i in pageOfResults:
            i[1] = i[1].replace("\'", "") # these characters prevent json from parsing the string on the react end
            i[1] = i[1].replace('"', "")
            i[1] = i[1].replace("\\", "")
            i[1] = i[1].replace("<!b>", "</b>")
            queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{int(i[0])}';"
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            titleAuthor = curr.fetchall()
            curr.close()
            titleAuthor = list(titleAuthor)
            titleAuthor[0] = list(titleAuthor[0])
            if(titleAuthor[0][0] == ""):
                titleAuthor[0][0] = "Title Unknown"
            i.append(titleAuthor[0][0]) # Here, we are appending the Article title

            if(titleAuthor[0][1] == ""):
                titleAuthor[0][1] = "Author Unknown"
                i.append(titleAuthor[0][1])
            else:
                author = titleAuthor[0][1].split(", ")
                i.append(", ".join(author))

        pageList = [str(i) for i in range(1, numOfPages+1)]
        return render_template("index.html", topic=topic, topicWord= word, topicWordResults=pageOfResults, pageButtons=pageList, pageNum=page+1)

# # AUTHOR RESULTS

@app.route("/AuthorList/<letterOrName>~<query>", methods=["POST", "GET"])
def authorResults(letterOrName = None, query = None): # query right now is the data retrieved from the sql query

    multipleNames = False
    if(";" in query):
        multipleNames = True
    query = ast.literal_eval(query)
    query = list(query)
    query = [list(i) for i in query]
    for i in range(len(query)):
        query[i][1]=re.split(", |;", query[i][1])


    for i in range(len(query)):
        if(len(query[i][1]) > 2): # multiple author article
            for j in range(1, len(query[i][1]), 2):
                temp = query[i][1][j-1]
                query[i][1][j-1] = query[i][1][j]
                query[i][1][j] = temp
                query[i][1][j] = query[i][1][j]+", "   # delete leading space and add a space between the names
            query[i][1][-1] = query[i][1][-1][:-2] # get rid of extra comma and space after last item
            query[i][1][0] += " "
        else: # this is to flip the author name
            if(len(query[i][1])>1):
                temp = query[i][1][0]
                query[i][1][0] = query[i][1][1]
                query[i][1][1] = " " + temp

    return render_template("index.html", enteredText=letterOrName, articlesList=query) # return all articles written by an author

@app.route("/HowTo", methods=["POST", "GET"])
def howToUser(): #
    return render_template("index.html")

auto = SM_Autocomplete()
@app.route("/autocomplete", methods=["POST", "GET"])
def autocomplete(): # basic and topic

    return json.dumps([item for sl in auto.general(json.loads(request.data)["txt"]) for item in sl ])

@app.route("/autocomplete2", methods=["POST", "GET"])
def autocomplete2(): # This is for the author search

    return json.dumps([item for sl in auto.author(json.loads(request.data)["txt"]) for item in sl ])



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return "ERROR: URL NOT FOUND"

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-d':
        serve(app)
    else:
        app.run(debug=True, use_reloader = True)
