import os
import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from search import *
from autocomplete import search, AUTOCOMPLETE
from functools import reduce
import re
import ast
from flask_cors import CORS
#For sending images
import io
from base64 import encodebytes
from PIL import Image
# from Face_extraction import face_extraction_v2

from ngram_search import *

template_dir = os.path.abspath("./flask-server/templates") # change THESE
static_dir = os.path.abspath("./flask-server/static") # 
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir )
CORS(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "shaker"
#articles.sql
mysql = MySQL(app)

#GLOBAL SM_Search Obj

searchObj = SM_Search()


# BASIC SEARCH

# POST is to send/change data.
@app.route("/", methods=["POST", "GET"]) #both paths work
# @app.route("/basicSearch", methods=["POST", "GET"])
def basicSearch():
    # return render_template("index.html", flask_token = "hi, there")
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(request.form.get("query") == False): # if nothing typed in the search bar
            return render_template("index.html") # maybe display a flash message here

        print("Right before we get query")
        # global enteredText # declare it first if you're going to change it
        enteredText = request.form["query"] # name in brackets matches the name of the post form in the HTML
        # enteredText = request.get_json()
        print(enteredText, type(enteredText))

        firstPage = searchObj.search(enteredText) # when you call search. It's just the 1st page
        print("First Page", firstPage)
        numOfPages = searchObj.page_num()
        print("num of pages", numOfPages)

        

        if(firstPage == []):
            firstPage = "None"
        searchResults = searchObj.store_results() # store as jsonified string so that we can pass through urls
        return redirect(url_for("basicResults1", values=enteredText, results = searchResults, numOfPages = numOfPages, page = 1)) # put in the function of the url you want to go to
       
# ARTICLE TYPE SEARCH

@app.route("/ArticleType", methods=["POST", "GET"]) # From advanced search
def displayTypes():
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(not request.form.get("query") and not request.form.get("checkbox")): # if no boxes checked and nothing entered
            return render_template("index.html") # display flash message

        elif(request.form.get("checkbox") and request.form.get("query")): # Typical: If we have a box checked and word entered 
            # print("Boxes checked:", request.form.getlist("checkbox"))
            enteredText = request.form.get("query")
            topic = request.form.get("checkbox")
            queryString = f"SELECT id FROM articles WHERE topics LIKE '%{topic}%' order by author_tag;" 
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()

            idList = list(fetchdata)
            idList = [list(i) for i in idList]
            idList = [j for i in idList for j in i] # flatten
            global searchObj
            firstPage = searchObj.search(enteredText) # when you call search. It's just the 1st page
            print("First Page", firstPage)
            numOfPages = searchObj.page_num()
            print("num of pages", numOfPages)

            if(firstPage == []):
                firstPage = "None"
            searchResults = searchObj.store_results() # store as jsonified string so that we can pass through urls          

            return redirect(url_for("topicWordResults", topic = topic, word = enteredText, results = searchResults, numOfPages = numOfPages, page = 1))


        elif(request.form.get("checkbox")): # just a box checked, nothing typed
            topic = request.form.get("checkbox")
            queryString = f"SELECT title, author_tag, id FROM articles WHERE topics LIKE '%{topic}%' order by author_tag;" 
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()
            # Return articles of certain topic
            return redirect(url_for("topicResults", topic = topic, results = fetchdata))

        else: # if no checkboxes checked, and just text entered. work like basic
            enteredText = request.form["query"] # name in brackets matches the name of the post form in the HTML
            print(enteredText, type(enteredText))
            
            firstPage = searchObj.search(enteredText) # when you call search. It's just the 1st page
            print("First Page", firstPage)
            numOfPages = searchObj.page_num()
            print("num of pages", numOfPages)

            if(firstPage == []):
                firstPage = "None"
            searchResults = searchObj.store_results() # store as jsonified string so that we can pass through urls
            return redirect(url_for("basicResults1", values=enteredText, results = searchResults, numOfPages = numOfPages, page = 1)) # put in the function of the url you want to go to
       

# AUTHOR SEARCH
@app.route("/Author", methods=["POST", "GET"]) # From advanced search
def displayAuthors(): # display landing page
    if(request.method == "GET"):
        print("just arrived on Author")
        return render_template("index.html")
    else: # POST
        print("Did a post on Author")
        if(request.form.get("letter")): # letter button is clicked
            letter = request.form["letter"]
            queryString = f"SELECT author_tag FROM articles WHERE author_tag LIKE '{letter}%' OR author_tag LIKE '%; {letter}%' group by author_tag;" # add author to select
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()
            print(fetchdata)
            return redirect(url_for("letterOfAuthors", letter = letter, query=fetchdata)) 
        else: # name was entered
            name = request.form["query"]
            # name = request.get_json(force=True)
            # name = request.json
            print("entered val: ", name)
            if(" " in name): # this means first and last name entered or multiple names
                nameList = name.split()
                if(len(nameList) == 2):
                    queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' order by author_tag;"
                elif(len(nameList) == 3):
                    queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && author_tag like '%{nameList[2]}%' order by author_tag;"
            elif(len(name) == 1):
                queryString = f"SELECT author_tag FROM articles WHERE author_tag LIKE '%, {name}%' group by author_tag;" # add author to select
            else: # either someone's firs or last name was displayed
                queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {name}%' OR author_tag LIKE '{name}%' order by author_tag;" # add author to select
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            # print("data: ", type(fetchdata)) # tuple
            curr.close()
            return redirect(url_for("authorResults", letterOrName = name, query=fetchdata)) # put in the function of the url you want to go to

# AUTHOR FIRST LETTER
@app.route("/AuthorNames/<letter>~<query>", methods=["POST", "GET"]) 
def letterOfAuthors(letter, query): # This gives us all the authors of the clicked letter
    multipleNames = False
    print(letter, query)
    if(query != "()"):
        query = query.replace("(", "")
        query = query.replace(",)", "")
        query = query.replace(")", "") # this gets rid of the last )
        print(query)
        if(";" in query):
            multipleNames = True
        query = re.split("', |\", |,, |;", query)
        print("PRE-ERROR", query)
        # print(query[1], type(query[1]))
            
        if(multipleNames == True): # this is to get rid of the authors that don't begin with the chosen letter
            ind = 0
            while(ind < len(query)):
                query[ind] = query[ind].strip()
                # print(query[ind], type(query[ind]))
                # print(query[ind][0], type(query[ind][0]))
                if(query[ind][0] != letter and query[ind][1] != letter):
                    query.pop(ind)
                else:
                    ind += 1
            # while(ind < len(query)):
            #     if(query[ind][query[ind].index(",")+2] != letter): # look to the other function
            #         query.pop(ind) # get rid of the co-authors from list
            #     else:
            #         ind += 1

        print("Look here", query)
        
        # get rid of ' on last item
        query[-1] = query[-1][:-1]
        for i in range(len(query)):
            if('"' in query[i]):
                query[i] = query[i].replace('"', "")
            if(query[i][0] == "'"):
                query[i] = query[i][1:]
            query[i] = query[i].split(",")
            
        
        print("Got rid of leading ':", query)
        
        for i in range(len(query)):
            if(len(query[i]) > 1):
                query[i][0] = query[i][0] +","
       
        query = set(tuple(i) for i in query) # get rid of any possible dups (there shouldn't be any)
        query = list(query)
      
        namesOfLetter = query
        query.sort()
        print(" final", query)
    else: # query = () meaning empty meaning no authors
        namesOfLetter = []
    return render_template("index.html", firstLetter = letter, namesOfLetter=namesOfLetter) 

# AUTHOR NAMES
@app.route("/AuthorNames", methods=["POST", "GET"]) # We render this page, and then we perform a post when we click on a name. We need to copy this
def displayNames(): # display author names. When user clicks on an author's name,
    if(request.method == "GET"):
        return render_template("index.html") # it should never bet accessed through a get, so maybe we default it to home page
    else: # POST
        undefined = False
        name = request.form["name"]
        print(name)
        name = name.replace("'", "\'") # do we need this? Maybe
        print("Name Displayed: ", name)
        # if article written by multiple people:
        # if(";" in name):
        #     nameList = name.split(";") #COME BACK TO THIS
        #article written by one person
        if(name[-9:] == "undefined"):
            name = name[:-9]
            undefined = True
        nameList = name.split(", ") # 
        print(nameList)
        print(undefined)
        if(undefined==True): # one name author, single letter, etc
            queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '{name}' order by author_tag;" # add author to select

        elif(len(nameList) == 2):
            queryString = f'SELECT title, author_tag FROM articles WHERE (author_tag LIKE "{nameList[0]}%" && author_tag LIKE "%, {nameList[1]}%") OR (author_tag LIKE "%; {nameList[0]}%" && author_tag LIKE "%, {nameList[1]}%") order by author_tag;'# either the last name appears first or it appears after a semicolon
     
        else: # one word name
            queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{name}%' order by author_tag;" # add author to select
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        fetchdata = curr.fetchall()
        curr.close()
        print(fetchdata)
        return redirect(url_for("authorResults", letterOrName = name, query=fetchdata)) # put in the function of the url you want to go to


# VOLUME & ISSUE SEARCH
@app.route("/VolumeIssue", methods=["POST", "GET"]) # From advanced search
def displayVolumes():
    return render_template("index.html")


# RESULTS

@app.route("/Results/<values>/<results>/<numOfPages>/<page>", methods=["POST", "GET"]) 
def basicResults1(values, results, numOfPages, page): 
    print("vals:",values)
    page = int(page) -1 # index begins at 0
    numOfPages = int(numOfPages) 

    searchObj.load_results(results) # results is a jsonified string. This just sets some of the internal state of SM obj 
    
    pageOfResults = searchObj._generate_results(page) # results is our search obj
    
    for i in pageOfResults:
        i[1] = i[1].replace("\'", "")
        i[1] = i[1].replace('"', "")
        i[1] = i[1].replace("\\", "")
        i[1] = i[1].replace("<!b>", "</b>")
        queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{i[0]}';" 
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        titleAuthor = curr.fetchall()
        curr.close()
        titleAuthor = list(titleAuthor)
        titleAuthor[0] = list(titleAuthor[0]) 
        i.append(titleAuthor[0][0]) # Here, we are appending the Article title
        author = titleAuthor[0][1].split(", ")
        i.append(", ".join(author))

    pageList = [str(i) for i in range(1, numOfPages+1)]
    print(pageList)
    return render_template("index.html", enteredTerm = values, results =pageOfResults, pageButtons=pageList, pageNum = page+1)# we're just using enteredText to display it
    
@app.route("/TopicResults/<topic>~<results>", methods=["POST", "GET"]) 
def topicResults(topic=None, results =None): # all articles related to a certain topic
    
    print("start", type(results), results)
    results = ast.literal_eval(results)
    results = list(results)
    results = [list(i) for i in results]
    print("new: ", results)
    results.sort()
    
    return render_template("index.html", topic=topic, topicResults=results)

@app.route("/ArticleResults/<articleID>", methods=["POST", "GET"]) 
def articleResults(articleID=None): # Open the text and image file of the article
    # aID = request.form["article"]
    sixDigits = False
    print(articleID)
    print(len(articleID))
    if(len(articleID)==6):
        sixDigits = True
        articleID = "0" + articleID
        textStart = articleID[:4] + "000"
    else: # ID length is 7
        textStart = articleID[:4] + "000"
    # print(textStart)
    # textStart = int(textStart)
    curr = textStart
    issueText = ""
    while(os.path.exists(f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{str(curr)}.txt")):
    # while(curr[3] == textStart[3]):
        path = f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{str(curr)}.txt"
        articleText = open(path, "r")
        articleText = articleText.read()
        if(curr == articleID):
            issueText += ("<b>" + articleText+ "</b>" + "<br/> <br/> <br/>")
        else:
            issueText += (articleText + "<br/> <br/> <br/>")
        curr = int(curr) + 1 # lose leading zero 
        if(sixDigits):
            curr = "0" + str(curr)
        else: # 7
            curr = str(curr)

    # replace non-UTF8 chars
    issueText = issueText.replace('ï¿½', '�') # em dash
    issueText = issueText.replace('.â€”', '—') # em dash
    issueText = issueText.replace('â€”', '—') # em dash
    issueText = issueText.replace("â€¢", '•') # dot
    issueText = issueText.replace("â€ž", '„') # dot
    
    # Get list of thumbnail paths
    curr = textStart[:-1] + str(1) # images start at 1
    thumbPaths = []
    # print((f"C:\\Users\\nonso\\OneDrive\\Documents\\thumbs\\thumbs\\{str(curr)}.jpg"))
    while(os.path.exists(f"C:\\Users\\nonso\\OneDrive\\Documents\\thumbs\\thumbs\\{str(curr)}.jpg")):
        path = f"C:\\Users\\nonso\\OneDrive\\Documents\\thumbs\\thumbs\\{str(curr)}.jpg"
        thumbPaths.append(path)
        curr = int(curr) + 1 
        if(sixDigits):
            curr = "0" + str(curr)# int() loses leading zero 
        else: # 7
            curr = str(curr)

    encodedImages = []
    for i in thumbPaths:
        # print(i)

        newResponse = get_response_image(i).replace("\n", "\\n")
        encodedImages.append(newResponse)
        

    # image_path = f"C:\\Users\\nonso\\OneDrive\\Documents\\images\\images\\0107001.jpg"#{articleID}.jpg" # point to your image location
    # encoded_img = get_response_image(image_path)
    print(thumbPaths)
    print(encodedImages)
    print(len(encodedImages))
    # print(thumbPaths[0])
    # print("no escape:", get_response_image(thumbPaths[0]))
    print("after escape:",encodedImages[0])

    return render_template("index.html", articleText = issueText, articleID=articleID, image=encodedImages) # we need to pass in everything here b/c we only want to use one page

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='JPEG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img

@app.route("/TopicWordResults/<topic>/<word>/<results>/<numOfPages>/<page>", methods=["POST", "GET"]) 
def topicWordResults(topic=None, word=None, results=None, numOfPages =None, page=None): # all articles related to a certain topic
    page = int(page) -1 # index begins at 0
    numOfPages = int(numOfPages) 

    searchObj.load_results(results) # results is a jsonified string. This just sets some of the internal state of SM obj 
    
    pageOfResults = searchObj._generate_results(page) # results is our search obj
    
    for i in pageOfResults:
        i[1] = i[1].replace("\'", "")
        i[1] = i[1].replace('"', "")
        i[1] = i[1].replace("\\", "")
        i[1] = i[1].replace("<!b>", "</b>")
        queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{i[0]}';" 
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        titleAuthor = curr.fetchall()
        curr.close()
        titleAuthor = list(titleAuthor)
        titleAuthor[0] = list(titleAuthor[0]) 
        i.append(titleAuthor[0][0]) # Here, we are appending the Article title
        author = titleAuthor[0][1].split(", ")
        i.append(", ".join(author))

    pageList = [str(i) for i in range(1, numOfPages+1)]
    print(pageList)

    return render_template("index.html", topic=topic, topicWord= word, topicWordResults=pageOfResults, pageButtons=pageList, pageNum=page+1)

# # AUTHOR RESULTS

@app.route("/AuthorList/<letterOrName>~<query>", methods=["POST", "GET"])
def authorResults(letterOrName = None, query = None): # query right now is the data retrieved from the sql query
    #In order to enable re-searching on this page, I'd need to run the query again on this function. We don't want to do that
    # Perhaps in the form, I can hardcode the path to the previous function that generates the query?
    # if(len(letterOrName) == 1): # then it's a letter. When is this ever the case?
    #     query = query.replace("(", "")
    #     query = query.replace(")", "")
    #     query = re.split("', |\",", query)
    #     # print(query)
    #     for i in range(len(query)):
    #         query[i] = query[i].split(",")
    #     # print(query)
    #     for i in range(len(query)):
    #         query[i][1] = query[i][1][2:]
    #         temp = query[i][-2] 
    #         query[i][-2] = query[i][-1]
    #         query[i][-1] = temp
    #     query[-1][1] = query[-1][1][:-1]
    #     # print(query)
    #     return #render_template("authorList.html", authorNames=query) # this needs to go to a different page (i.e. not authorList). Just one with all the names of a particular letter
    # else: # name typed in
    multipleNames = False
    if(";" in query):
        multipleNames = True
    print("start", type(query), query)
    query = ast.literal_eval(query)
    query = list(query)
    query = [list(i) for i in query]
    for i in range(len(query)):
        query[i][1]=re.split(", |;", query[i][1])
    

    print("After: ", query)

    for i in range(len(query)):
        if(len(query[i][1]) > 2): # multiple author article
            for j in range(1, len(query[i][1]), 2):
                temp = query[i][1][j-1]
                query[i][1][j-1] = query[i][1][j]
                query[i][1][j] = temp
                # query[0][1][i-1] = query[0][1][i-1][1:]  # delete leading space and add a space between the names
                query[i][1][j] = query[i][1][j]+", "   # delete leading space and add a space between the names
            query[i][1][-1] = query[i][1][-1][:-2] # get rid of extra comma and space after last item
            query[i][1][0] += " "
        else: # this is to flip the author name
            if(len(query[i][1])>1):
                temp = query[i][1][0]
                query[i][1][0] = query[i][1][1]
                query[i][1][1] = " " + temp

    for i in query:
        # for j in i:
        authorCombined = i[1][1][1:] + ", " + i[1][0]
        print(authorCombined)
        queryString = f"SELECT id FROM articles WHERE title LIKE '{i[0]}' AND author_tag LIKE '%{authorCombined}%';" 
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        artID = curr.fetchall()
        curr.close()
        artID = list(artID)
        i.append(artID)

    print(query)
    print(type(query))
    # articlesList = json.dumps(query)
    # articlesList = json.loads(query)
    return render_template("index.html", enteredText=letterOrName, articlesList=query) # return all articles written by an author



@app.route("/autocomplete", methods=["POST", "GET"])
def autocomplete():
    print("in shaker-manifestoo.py")
    # print(json.dumps(request.data))
    # print("raw data: ", request.get_data())
    print("request.data: ", request.data)
    # print("request.json: ", request.json)
    # print(type(request.json))
    # print("request.get_json: ", request.get_json()) #bad request err on client
    # print(type(request.form.get("txt")))
    # print("request.form: ", request.form["txt"]) # key err

    return json.dumps([item for sl in search(json.loads(request.data)["txt"]) for item in sl ])

    # return reduce(lambda x, y: str(x) + ',' + str(y),
            # [item for sublist in search(json.loads(request.data)["txt"]) for item in sublist]) # this is what produces the list of options

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return "ERROR: URL NOT FOUND"
    # return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader = True)
