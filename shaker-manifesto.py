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

#GLOBAL VARS
# resultDict = {}
# enteredText = "" # just for display
# topic = "" # just for display 
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
        # return jsonify(query)
        # query = enteredText
        # queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%{query}%' order by author_tag;" # add author to select
        # curr = mysql.connection.cursor()
        # curr.execute(queryString)
        # fetchdata = curr.fetchall() # is have the values returned by the query
        # curr.close()
        # print(type(fetchdata))
        # return redirect(url_for("basicResults1", values=fetchdata, enteredText = enteredText)) # put in the function of the url you want to go to
        # global resultDict
        resultDict = {}
        searchObj = SM_Search()
        artRes = searchObj.search(enteredText)
        print("Entire thing", artRes)
        print("First", artRes[0])
        numOfPages = artRes.page_num()
        print("num of pages", artRes.page_num())
        print("last page: ", artRes[numOfPages])
        return
        for i in range(len(artRes)):
            artRes[i] = list(artRes[i])
        resultDict[1] = artRes
        n = 2
        artRes = searchObj.generate_results()
        # fill result Dict
        while(artRes != None):
            for i in range(len(artRes)):
                artRes[i] = list(artRes[i])
            resultDict[n] = artRes
            artRes = searchObj.generate_results()
            n += 1

        # for i in range(len(results[page])):
            # results[page][i] = list(results[page][i])

        for i in resultDict.values():
            for j in i:
                queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{j[0]}';" 
                curr = mysql.connection.cursor()
                curr.execute(queryString)
                titleAuthor = curr.fetchall()
                curr.close()
                titleAuthor = list(titleAuthor)
                titleAuthor[0] = list(titleAuthor[0]) 
                j.append(titleAuthor[0][0]) # Here, we are appending the Article title
                author = titleAuthor[0][1].split(", ")
                # if(len(author)>1):
                #     temp = author[0]
                #     author[0] = author[1] + " "
                #     author[1] = temp
                j.append(", ".join(author))
                # j.append(titleAuthor[0][1])

        if(artRes == []):
            artRes = "None"
        print("article Results", resultDict)
        return redirect(url_for("basicResults1", values=enteredText, results = resultDict, page = 1)) # put in the function of the url you want to go to
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
        global resultDict
        global enteredText
        global topic
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
            resultDict = {}
            searchObj = SM_Search()
            artRes = searchObj.search(enteredText, idList)           
            for i in range(len(artRes)):
                artRes[i] = list(artRes[i])
            resultDict[1] = artRes
            n = 2
            artRes = searchObj.generate_results()
            # fill result Dict
            while(artRes != None):
                for i in range(len(artRes)):
                    artRes[i] = list(artRes[i])
                resultDict[n] = artRes
                artRes = searchObj.generate_results()
                n += 1

            # for i in range(len(results[page])):
                # results[page][i] = list(results[page][i])

            for i in resultDict.values():
                for j in i:
                    queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{j[0]}';" 
                    curr = mysql.connection.cursor()
                    curr.execute(queryString)
                    titleAuthor = curr.fetchall()
                    curr.close()
                    titleAuthor = list(titleAuthor)
                    titleAuthor[0] = list(titleAuthor[0]) 
                    j.append(titleAuthor[0][0]) # 
                    author = titleAuthor[0][1].split(", ")
                    # if(len(author)>1):
                    #     temp = author[0]
                    #     author[0] = author[1] + " "
                    #     author[1] = temp
                    # j.append("".join(author))
                    j.append(", ".join(author))

                    # j.append(titleAuthor[0][1])
            return redirect(url_for("topicWordResults", topic = topic, word = enteredText, results = resultDict, page = 1))


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
            resultDict = {}
            searchObj = SM_Search()
            artRes = searchObj.search(enteredText)
            for i in range(len(artRes)):
                artRes[i] = list(artRes[i])
            resultDict[1] = artRes
            n = 2
            artRes = searchObj.generate_results()
            # fill result Dict
            while(artRes != None):
                for i in range(len(artRes)):
                    artRes[i] = list(artRes[i])
                resultDict[n] = artRes
                artRes = searchObj.generate_results()
                n += 1

            # for i in range(len(results[page])):
                # results[page][i] = list(results[page][i])

            for i in resultDict.values():
                for j in i:
                    queryString = f"SELECT title, author_tag FROM articles WHERE id LIKE '{j[0]}';" 
                    curr = mysql.connection.cursor()
                    curr.execute(queryString)
                    titleAuthor = curr.fetchall()
                    curr.close()
                    titleAuthor = list(titleAuthor)
                    titleAuthor[0] = list(titleAuthor[0]) 
                    print(titleAuthor, type(titleAuthor))
                    j.append(titleAuthor[0][0]) # 
                    author = titleAuthor[0][1].split(", ")
                    # if(len(author)>1):
                    #     temp = author[0]
                    #     author[0] = author[1] + " "
                    #     author[1] = temp
                    # j.append("".join(author))
                    j.append(", ".join(author))

                    # j.append(titleAuthor[0][1])
            return redirect(url_for("basicResults1", values=enteredText, results = resultDict)) # put in the function of the url you want to go to


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

        # for i in range(len(query)):
        #         query[i][0] = query[i][0][1:]
        #         temp = query[i][-1] 
        #         query[i][-1] = query[i][0]
        #         query[i][0] = temp
        # query[-1][0] = query[-1][0][:-1]
        # print(query)
        # get rid of duplicates
       
        query = set(tuple(i) for i in query) # get rid of any possible dups (there shouldn't be any)
        query = list(query)
        # for i in range(len(query)):
        #     query[i] = list(query[i])
        #     query[i][0] = query[i][0][1:]
        # print(query)
        namesOfLetter = query
        # letter = json.dumps(letter)
        # letter = json.loads(letter)
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
            # curr = mysql.connection.cursor()
            # curr.execute(queryString)
            # fetchdata = curr.fetchall()
            
        # elif(len(nameList) == 3):
        #     queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && (author_tag LIKE '{nameList[2]}%' OR author_tag LIKE '%; {nameList[2]}%') order by author_tag;" # I think something happens when I don't have % in front of the last namelist
        #     curr = mysql.connection.cursor()
        #     curr.execute(queryString)
        #     fetchdata = curr.fetchall()
            
        # elif(len(nameList) == 4):
        #     queryString = f"SELECT title, author_tag FROM articles WHERE author_tag LIKE '%, {nameList[0]}%' && author_tag LIKE '%{nameList[1]}%' && author_tag LIKE '%{nameList[2]}%' && (author_tag LIKE '{nameList[3]}%' OR author_tag LIKE '%; {nameList[3]}%') order by author_tag;"
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

@app.route("/Results/<values>/<results>/<page>", methods=["POST", "GET"]) 
def basicResults1(values=None, results=None, page=None): 
    print("vals:",values)
    print("res:", results)
    page = int(page) # when vars get passed to other functions(routes), they get passed as strings, so I have to convert them
    
    
    # RESULTS IS THE DICT
    if(results != "None" and results != None):
        # print("THIS IS THE TYPE",type(results))
        # if(type(results) == str):
        results = ast.literal_eval(results) # convert str to whatever it actually is
        # print(type(results), "results are here", results, results[1])
        # print(type(results), results, results[0], type(results[0]))
        
        for i in range(len(results[1])):
            results[1][i][1] = results[1][i][1].replace("\'", "")
            results[1][i][1] = results[1][i][1].replace('"', "")
            results[1][i][1] = results[1][i][1].replace("\\", "")
            results[1][i][1] = results[1][i][1].replace("<!b>", "</b>")
        # global pageCount
        

        pageList = [str(i) for i in range(1,len(results)+1)]
        print(pageList)
    return render_template("index.html", enteredTerm = values, results =results[page], pageButtons=pageList, pageNum = page)# we're just using enteredText to display it

# @app.route("/NextResults/<values>/<page>", methods=["POST", "GET"]) # We need to get the page number through the URL
# def basicResults1Next(values=None, page=None): 
#     # values = enteredText 
#     print("vals:",values) # val is entered term
#     print("page from URL:", page)
#     print(type(page))
#     page = int(page)
#     # if(request.form.get("page")):
#     #     print("we are here")
#         # results = searchObj.generate_results()
#     #     for i in range(len(results)):
#     #         results[i] = list(results[i])# print(results)
#     #     for i in range(len(results)):
#     #         results[i][1] = results[i][1].replace("\'", "")
#     #         results[i][1] = results[i][1].replace('"', "")
#     #         results[i][1] = results[i][1].replace("\\", "")
#     #         results[i][1] = results[i][1].replace("<!b>", "</b>")
#     # page = int(request.form["page"]) 
#     # print("page from form:", page)
#     print(resultDict)
#     results = resultDict # it doesn't know what results is until this point
#     # print(results)
#     print(results[page])
#     if(results[page] != "None" and results[page] != None):
#         print("results are here", results[page])
#         # print(type(results), results, results[0], type(results[0]))
        
#         for i in range(len(results[page])):
#             results[page][i][1] = results[page][i][1].replace("\'", "")
#             results[page][i][1] = results[page][i][1].replace('"', "")
#             results[page][i][1] = results[page][i][1].replace("\\", "")
#             results[page][i][1] = results[page][i][1].replace("<!b>", "</b>")
#     # global pageCount
#     # pageCount += 1
#     pageList = [str(i) for i in range(1,len(results)+1)]
#     return render_template("index.html", enteredTerm = values, results =results[page], pageButtons=pageList, pageNum=page)# we're just using enteredText to display it

    
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

@app.route("/ArticleResults/<articleID>", methods=["POST", "GET"]) 
def articleResults(articleID=None): # Open the text and image file of the article
    # aID = request.form["article"]
    print(articleID)
    # filename = "0" + aID + ".txt"
    if(len(articleID)==6):
        path = f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\0{articleID}.txt"
        articleText = open(path, "r")
        articleText = articleText.read()
        print(articleText)
    else:
        path = f"C:\\Users\\nonso\\OneDrive\\Documents\\Shaker-Manifesto\\textfiles\\{articleID}.txt"
        articleText = open(path, "r")
        articleText = articleText.read()
        print(articleText)
    # replace non-UTF8 chars
    
    articleText = articleText.replace('ï¿½', '�') # em dash
    articleText = articleText.replace('.â€”', '—') # em dash
    articleText = articleText.replace('â€”', '—') # em dash
    
    articleText = articleText.replace("â€¢", '•') # dot

    
    return render_template("index.html", articleText = articleText, articleID=articleID) # we need to pass in everything here b/c we only want to use one page

@app.route("/TopicWordResults/<topic>/<word>/<results>/<page>", methods=["POST", "GET"]) 
def topicWordResults(topic=None, word=None, results=None, page=None): # all articles related to a certain topic
    page = int(page)
    # RESULTS IS THE DICT
    if(results != "None" and results != None):
        # print("THIS IS THE TYPE",type(results))
        # if(type(results) == str):
        results = ast.literal_eval(results) # convert str to whatever it actually is
        # print(type(results), "results are here", results, results[1])
        # print(type(results), results, results[0], type(results[0]))
        
        for i in range(len(results[1])):
            results[1][i][1] = results[1][i][1].replace("\'", "")
            results[1][i][1] = results[1][i][1].replace('"', "")
            results[1][i][1] = results[1][i][1].replace("\\", "")
            results[1][i][1] = results[1][i][1].replace("<!b>", "</b>")
        # global pageCount
        

        pageList = [str(i) for i in range(1,len(results)+1)]
        # print(results[1])
    # return render_template("index.html", enteredTerm = values, results =results[1], pageButtons=pageList)# we're just using enteredText to display it
    
    return render_template("index.html", topic=topic, topicWord= word, topicWordResults=results[1], pageButtons=pageList, pageNum=page)

@app.route("/TopicWordResultsNext/<topic>/<word>/<page>", methods=["POST", "GET"]) 
def topicWordResultsNext(topic=None, word=None, page=None): 
    # word = enteredText #getting the global var
    print("entered word:", word)
    theTopic = topic # getting the global var
    print("entered topic:", theTopic)
    page = int(page)

    print(resultDict)
    results = resultDict # it doesn't know what results is until this point
    # print("everything", results)
    print("the page", results[page])
    if(results[page] != "None" and results[page] != None):
        print("results are here", results[page])
        # print(type(results), results, results[0], type(results[0]))
        
        for i in range(len(results[page])):
            results[page][i][1] = results[page][i][1].replace("\'", "")
            results[page][i][1] = results[page][i][1].replace('"', "")
            results[page][i][1] = results[page][i][1].replace("\\", "")
            results[page][i][1] = results[page][i][1].replace("<!b>", "</b>")
    # global pageCount
    # pageCount += 1
    pageList = [str(i) for i in range(1,len(results)+1)]
    return render_template("index.html", topic=theTopic, topicWord= word, topicWordResults =results[page], pageButtons=pageList, pageNum=page)# we're just using enteredText to display it

    
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
    for i in query:
        # for j in i:
        queryString = f"SELECT id FROM articles WHERE title LIKE '{query[0][0]}';" 
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
