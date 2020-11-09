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

template_dir = os.path.abspath("./Frontend/templates") # change THESE
static_dir = os.path.abspath("./Frontend/static")
app = Flask(__name__) #, template_folder=template_dir, static_folder=static_dir )
CORS(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "shaker"
#articles.sql
mysql = MySQL(app)

# BASIC SEARCH

# POST is to send/change data.
@app.route("/", methods=["POST", "GET"]) #both paths work
# @app.route("/basicSearch", methods=["POST", "GET"])
def basicSearch():
    # return render_template("index.html", flask_token = "hi, there")
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(request.form.get("query") == False):
            return render_template("index.html") # maybe display a flash message here

        print("Right before we get query")
        enteredText = request.form["query"] # name in brackets matches the name of the post form in the HTML
        # enteredText = request.get_json()
        print(enteredText, type(enteredText))
        # return jsonify(query)
        # query = enteredText
        # queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{query}%' order by author_tag;" # add author to select
        # curr = mysql.connection.cursor()
        # curr.execute(queryString)
        # fetchdata = curr.fetchall() # is have the values returned by the query
        # curr.close()
        # print(type(fetchdata))
        # return redirect(url_for("basicResults1", values=fetchdata, enteredText = enteredText)) # put in the function of the url you want to go to
        artRes = articleSearch(enteredText)
        if(artRes == None):
            artRes = "None"
        print("article Results", artRes)
        return redirect(url_for("basicResults1", values=enteredText, results = artRes)) # put in the function of the url you want to go to
        # return render_template("index.html", flask_token = enteredText) # maybe display a flash message here


        # enteredText = query # This is so we can say, "search results related to:"
        # queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{query}%' order by author_tag;" # add author to select
        # print(queryString)
        # curr = mysql.connection.cursor()
        # curr.execute(queryString)
        # fetchdata = curr.fetchall() # is have the values returned by the query 
        # curr.close()

        # # return render_template("resultsPage.html", query=query) # query(left) is the name of the variable we put in the html.
        # return redirect(url_for("basicResults1", query=fetchdata, enteredText = enteredText)) # put in the function of the url you want to go to
        # return redirect(url_for("basicResults1", query=query)) # put in the function of the url you want to go to. L is there, R is here

# @app.route("/resultsPage/<query>", methods=["POST", "GET"]) 
# def basicResults1(query): 
#     return render_template("resultsPage.html", query=query)


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
            searchWord = request.form.get("query")
            topic = request.form.get("checkbox")
            queryString = f"SELECT id FROM articles WHERE topics LIKE '%{topic}%' order by author_tag;" 
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()

            idList = list(fetchdata)
            idList = [list(i) for i in idList]
            idList = [j for i in idList for j in i] # flatten
            artResults = articleSearch(searchWord, idList)
            if(artResults == None):
                artResults = "None"
            return redirect(url_for("topicWordResults", topic = topic, word = searchWord, results = artResults))

        elif(request.form.get("checkbox")): # just a box checked, nothing typed
            topic = request.form.get("checkbox")
            queryString = f"SELECT title, author_tag FROM articles WHERE topics LIKE '%{topic}%' order by author_tag;" 
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            curr.close()
            # Return articles of certain topic
            return redirect(url_for("topicResults", topic = topic, results = fetchdata))

        else: # if no checkboxes checked, and just text entered. work like basic
            enteredText = request.form["query"] # name in brackets matches the name of the post form in the HTML
            print(enteredText, type(enteredText))
            artRes = articleSearch(enteredText)
            if(artRes == None):
                artRes = "None"
            print("article Results", artRes)
            return redirect(url_for("basicResults1", values=enteredText, results = artRes)) # put in the function of the url you want to go to


        # enteredText = request.form["query"] # name matches the name of the post form in the HTML
        # print("HERE")

        # if(enteredText and topics):
        #     return redirect(url_for("advancedResults", queryAd=enteredText, topics = topics, enteredText = enteredText)) # put in the name of function of the url you want to go to
        # elif(not topics):
        #     queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{enteredText}%' order by author_tag;" # add author to select
        #     print(queryString)
        #     curr = mysql.connection.cursor()
        #     curr.execute(queryString)
        #     fetchdata = curr.fetchall()
        #     curr.close()
        #     return redirect(url_for("basicResults1", query = fetchdata, enteredText = enteredText)) # Query with no type. Perhaps we should force them to select a type
        # elif(not enteredText):
        #     return redirect(url_for("basicResults2", topics = topics)) # all articles related to a certain article type
        # else: # Don't have anything selected, stay on page
        #     print("Here: ",topics, enteredText)
        #     return render_template("index.html")

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
            queryString = f"SELECT author_tag FROM articles WHERE author_tag LIKE '%, {letter}%' group by author_tag;" # add author to select
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
        print(query)

        if(multipleNames == True):
            ind = 0
            while(ind < len(query)):
                if(query[ind][query[ind].index(",")+2] != letter): # look to the other function
                    query.pop(ind) # get rid of the co-authors from list
                else:
                    ind += 1

        
        for i in range(len(query)):
            query[i] = query[i].split(",")
            
        print(query)
        
        # if(multipleNames == True):
        #     for i in range(len(query)):
        #         query[i][1] = query[i][1][1:] # when we have multiple authors, because we split on ;, we don't have the leading '
        #         temp = query[i][-2] 
        #         query[i][-2] = query[i][-1]
        #         query[i][-1] = temp
        #     print(query)
        #     newQuery = []
        #     for i in query:
        #         for j in i:
        #             newQuery.append(j)
        #     query = newQuery
        #     print(query)
        #     for i in range(2,len(query)-1,2):
        #         query[i] = query[i]+", "

        for i in range(len(query)):
                query[i][0] = query[i][0][1:]
                temp = query[i][-1] 
                query[i][-1] = query[i][0]
                query[i][0] = temp
        query[-1][0] = query[-1][0][:-1]
        print(query)
        # get rid of duplicates
       
        query = set(tuple(i) for i in query)
        query = list(query)
        for i in range(len(query)):
            query[i] = list(query[i])
            query[i][0] = query[i][0][1:]
        print(query)
        namesOfLetter = query
        # letter = json.dumps(letter)
        # letter = json.loads(letter)
        print(letter)
    else: # query = () meaning empty meaning no authors
        namesOfLetter = []
    return render_template("index.html", firstLetter = letter, namesOfLetter=namesOfLetter) 

# AUTHOR NAMES
@app.route("/AuthorNames", methods=["POST", "GET"]) # From advanced search
def displayNames(): # display author names. When user clicks on an author's name,
    if(request.method == "GET"):
        return render_template("index.html") # it should never bet accessed through a get, so maybe we default it to home page
    else: # POST
        name = request.form["name"]
        print(name)
        name = name.replace("'", "\'")
        print("Name Displayed: ", name)
        # if article written by multiple people:
        # if(";" in name):
        #     nameList = name.split(";") #COME BACK TO THIS
        #article written by one person
        nameList = name.split() # this doesn't work so great if we have a person with two first names
        print(nameList)
        if(len(nameList) == 2):
            queryString = f'SELECT title, author_tag FROM articles WHERE author_tag LIKE "%, {nameList[0]}%" && (author_tag LIKE "{nameList[1]}%" OR author_tag LIKE "%; {nameList[1]}%") order by author_tag;'# either the last name appears first or it appears after a semicolon
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            # if(not fetchdata): # if we have nothing after that query, that means that the author has written an author with other people
            #     queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' order by author_tag;"
            #     curr = mysql.connection.cursor()
            #     curr.execute(queryString)
            #     fetchdata = curr.fetchall()
        elif(len(nameList) == 3):
            queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && (author_tag LIKE '{nameList[2]}%' OR author_tag LIKE '%; {nameList[2]}%') order by author_tag;" # I think something happens when I don't have % in front of the last namelist
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            # if(not fetchdata):
            #     queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && author_tag LIKE '%{nameList[2]}%' order by author_tag;" # I think something happens when I don't have % in front of the last namelist
            #     curr = mysql.connection.cursor()
            #     curr.execute(queryString)
            #     fetchdata = curr.fetchall()
        elif(len(nameList) == 4):
            queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && author_tag LIKE '%{nameList[2]}%' && (author_tag LIKE '{nameList[3]}%' OR author_tag LIKE '%; {nameList[3]}%') order by author_tag;"
            curr = mysql.connection.cursor()
            curr.execute(queryString)
            fetchdata = curr.fetchall()
            # if(not fetchdata):
            #     queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && author_tag LIKE '%{nameList[2]}%' && author_tag LIKE '%{nameList[3]}%' order by author_tag;"
            #     curr = mysql.connection.cursor()
            #     curr.execute(queryString)
            #     fetchdata = curr.fetchall()
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

@app.route("/Results/<values>~<results>", methods=["POST", "GET"]) 
def basicResults1(values=None, results=None): 
    print("vals:",values)
    if(results != "None"):
        results = ast.literal_eval(results)
    # print(results)
        for i in range(len(results)):
            results[i][1] = results[i][1].replace("\'", "")
            results[i][1] = results[i][1].replace('"', "")
            results[i][1] = results[i][1].replace("\\", "")
            results[i][1] = results[i][1].replace("<!b>", "</b>")

    # results = results.strip('][').split(', ')
        print(type(results), results)
        print(type(results[0][1]))
    # print(results[1])
    
    # if(values != "()"):
    #     values = values.replace("(", "")
    #     values = values.replace(")", "")
    #     # values = values.split("',")

    #     values = re.split("', |\",", values)
    #     print(values)

    #     # values[-1] = values[-1].replace(values[-1][-1][-1], "", 1)
    #     for i in range(len(values)):
    #         values[i] = values[i].split(",")

    #     print(values)
    #     for i in range(len(values)):
    #         values[i][1] = values[i][1][2:]
    #         temp = values[i][-2] 
    #         values[i][-2] = values[i][-1]
    #         values[i][-1] = temp
        
    #     values[-1][1] = values[-1][1][:-1]

    #     print(values)
    #     print(jsonify(values))
    return render_template("index.html", enteredTerm = values, results =results)# we're just using enteredText to display it
    # return values
@app.route("/TopicResults/<topic>~<results>", methods=["POST", "GET"]) 
def topicResults(topic=None, results =None): # all articles related to a certain topic
    
    print("start", type(results), results)
    results = ast.literal_eval(results)
    results = list(results)
    results = [list(i) for i in results]
    print("new: ", results)
    # for i in range(len(query)):
    #     query[i][1]=re.split(", |;", query[i][1])
    
    return render_template("index.html", topic=topic, topicResults=results)

@app.route("/ArticleResults", methods=["POST", "GET"]) 
def articleResults(): # Open the text and image file of the article
    
    # print("start", type(results), results)
    # results = ast.literal_eval(results)
    # results = list(results)
    # results = [list(i) for i in results]
    # print("new: ", results)
    # for i in range(len(query)):
    #     query[i][1]=re.split(", |;", query[i][1])
    
    return render_template("index.html")

@app.route("/TopicWordResults/<topic>~<word>~<results>", methods=["POST", "GET"]) 
def topicWordResults(topic=None, word=None, results=None): # all articles related to a certain topic
    
    if(results != "None"):
        results = ast.literal_eval(results)
        print(results)
        for i in range(len(results)):
            results[i][1] = results[i][1].replace("\'", "")
            results[i][1] = results[i][1].replace('"', "")
            results[i][1] = results[i][1].replace("\\", "") # JSON gets confused when it tries to parse over these chars
            results[i][1] = results[i][1].replace("<!b>", "</b>")
    # for i in range(len(query)):
    #     query[i][1]=re.split(", |;", query[i][1])
    print(results)
    
    return render_template("index.html", topic=topic, topicWord= word, topicWordResults=results)

# @app.route("/resultsPage/<queryAd>-<topics>-<enteredText>", methods=["POST", "GET"]) # since we redirected it, it expects to see <query> and <topics> in the URL
# def advancedResults(queryAd, topics, enteredText): # this input str var will eventually get converted into a SQL query to be ran against the database to return results.
#     # if(request.method == "GET"):
#     queryAd = None

#     print("topics:", topics) # when we don't have a query the hyphen stays. So we'll have to strip it later on
#     return render_template("resultsPage.html", queryAd=queryAd, topics=topics, enteredText=enteredText)

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
        else:
            temp = query[i][1][0]
            query[i][1][0] = query[i][1][1]
            query[i][1][1] = " " + temp


        # b = query[0][1][i].split(";")
        # b = re.split(",|;", query[0][1][i])
        # if(len(b) > 2): # multiple authors
        #     for i in reversed(range(2, len(b)-1, 2)):
        #         b[i] = b[i]+","
        # b = b.split(",")
        # if(";" in b):
        #     b = b.split(";")
        # b = b.replace(",", "")
        # print(query)
        # articlesList[a] = b


    # if(multipleNames):
    #     query[0][1][0] = " " + query[0][1][0] # add a space in front of the first name to be consistent 
    #     for i in range(1, len(query[0][1]), 2):
    #         temp = query[0][1][i-1]
    #         query[0][1][i-1] = query[0][1][i]
    #         query[0][1][i] = temp
    #         # query[0][1][i-1] = query[0][1][i-1][1:]  # delete leading space and add a space between the names
    #         query[0][1][i] = query[0][1][i]+", "   # delete leading space and add a space between the names
    #     query[0][1][-1] = query[0][1][-1][:-2] # get rid of extra comma and space
    #     print(query[0][1])
    # else: # only one author of the article
    #     for i in range(len(query)):
    #         query[i][1][1] = query[i][1][1] 
    #         temp = query[i][1][0]
    #         query[i][1][0] = query[i][1][1]
    #         query[i][1][1] = " " + temp
    print(query)

    # articlesList = {} # key = article ID : val = author(s)
    # print("Here: ", query[0], query[0][0]) 
    
    # print(query[0][1])

    # print(type(articlesList))
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
