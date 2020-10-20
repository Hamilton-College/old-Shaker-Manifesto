import os
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_mysqldb import MySQL
# from autocomplete import search, AUTOCOMPLETE
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

        enteredText = request.form["query"] # name in brackets matches the name of the post form in the HTML
        # return jsonify(query)
        query = enteredText
        queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{query}%' order by regauthor;" # add author to select
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        fetchdata = curr.fetchall() # is have the values returned by the query
        curr.close()
        print(type(fetchdata))
        return redirect(url_for("basicResults1", values=fetchdata, enteredText = enteredText)) # put in the function of the url you want to go to
        # return render_template("index.html", flask_token = query) # maybe display a flash message here


        # enteredText = query # This is so we can say, "search results related to:"
        # queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{query}%' order by regauthor;" # add author to select
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


# # ARTICLE TYPE SEARCH

@app.route("/ArticleType", methods=["POST", "GET"]) # From advanced search
def displayTypes():
    return render_template("index.html")

@app.route("/Author", methods=["POST", "GET"]) # From advanced search
def displayAuthors():
    return render_template("index.html")

@app.route("/VolumeIssue", methods=["POST", "GET"]) # From advanced search
def displayVolumes():
    return render_template("index.html")

# @app.route("/Results/<values>-<enteredText>", methods=["POST", "GET"]) # From advanced search
# def displayResults(values, enteredText):
    # print(values)
    # return render_template("index.html", flask_token = values, searchedText = enteredText)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return "You want path: %s" % path
    # return app.send_static_file("index.html")
#     print("Start")
#     if(request.method == "GET"):
#         return render_template("articleType.html")
#     else: # POST
#         if(not request.form["query"] and not request.form.getlist("checkbox")): # if no boxes checked and nothing entered
#             return render_template("articleType.html")
#         elif(request.form.getlist("checkbox")): # If we have a box checked
#             # print("Boxes checked:", request.form.getlist("checkbox"))
#             topics = request.form.getlist("checkbox")
#         else: # if no checkboxes checked, and just text entered
#             topics = None
#             # print("topics:", topics)

#         query = request.form["query"] # name matches the name of the post form in the HTML
#         enteredText = query
#         print("HERE")

#         if(query and topics):
#             return redirect(url_for("advancedResults", queryAd=query, topics = topics, enteredText = enteredText)) # put in the name of function of the url you want to go to
#         elif(not topics):
#             queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{query}%' order by regauthor;" # add author to select
#             print(queryString)
#             curr = mysql.connection.cursor()
#             curr.execute(queryString)
#             fetchdata = curr.fetchall()
#             curr.close()
#             return redirect(url_for("basicResults1", query = fetchdata, enteredText = enteredText)) # Query with no type. Perhaps we should force them to select a type
#         elif(not query):
#             return redirect(url_for("basicResults2", topics = topics)) # all articles related to a certain article type
#         else: # Don't have anything selected, stay on page
#             print("Here: ",topics, query)
#             return render_template("articleType.html")

# # AUTHOR SEARCH
# @app.route("/author.html", methods=["POST", "GET"]) # From advanced search
# def displayAuthors(): # display landing page
#     if(request.method == "GET"):
#         return render_template("author.html")
#     else: # POST
#         # curr = mysql.connection.cursor()
#         # curr.execute(queryString)
#         # fetchdata = curr.fetchall()
#         # curr.close()
#         if(request.form.get("letter")): # letter button is clicked
#             letter = request.form["letter"]
#             queryString = f"SELECT regauthor FROM authors WHERE regauthor LIKE '%, {letter}%' group by regauthor;" # add author to select
#             curr = mysql.connection.cursor()
#             curr.execute(queryString)
#             fetchdata = curr.fetchall()
#             curr.close()
#             print(fetchdata)
#             return redirect(url_for("letterOfAuthors", letter = letter, query=fetchdata)) 
#         else: # name was entered
#             name = request.form["query"]
#             if(" " in name): # this means first and last name entered or multiple names
#                 nameList = name.split()
#                 if(len(nameList) == 2):
#                     queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' order by regauthor;"
#                 elif(len(nameList) == 3):
#                     queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' && regauthor like '%{nameList[2]}%' order by regauthor;"
#             else:     
#                 queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{name}%' order by regauthor;" # add author to select
#             curr = mysql.connection.cursor()
#             curr.execute(queryString)
#             fetchdata = curr.fetchall()
#             # print("data: ", type(fetchdata)) # tuple
#             curr.close()
#             return redirect(url_for("authorResults", letterOrName = name, query=fetchdata)) # put in the function of the url you want to go to
# # AUTHOR FIRST LETTER
# @app.route("/author.html/<letter>-<query>", methods=["POST", "GET"]) 
# def letterOfAuthors(letter, query): # This gives us all the authors of the specified letter
#     multipleNames = False
#     print(letter, query)
#     if(query != "()"):
#         query = query.replace("(", "")
#         query = query.replace(",)", "")
#         query = query.replace(")", "") # this gets rid of the last )
#         print(query)
#         if(";" in query):
#             multipleNames = True
#         query = re.split("', |\", |,, |;", query)
#         print(query)

#         if(multipleNames == True):
#             ind = 0
#             while(ind < len(query)):
#                 if(query[ind][query[ind].index(",")+2] != letter): # look to the other function
#                     query.pop(ind) # get rid of the co-authors from list
#                 else:
#                     ind += 1

        
#         for i in range(len(query)):
#             query[i] = query[i].split(",")
            
#         print(query)
        
#         # if(multipleNames == True):
#         #     for i in range(len(query)):
#         #         query[i][1] = query[i][1][1:] # when we have multiple authors, because we split on ;, we don't have the leading '
#         #         temp = query[i][-2] 
#         #         query[i][-2] = query[i][-1]
#         #         query[i][-1] = temp
#         #     print(query)
#         #     newQuery = []
#         #     for i in query:
#         #         for j in i:
#         #             newQuery.append(j)
#         #     query = newQuery
#         #     print(query)
#         #     for i in range(2,len(query)-1,2):
#         #         query[i] = query[i]+", "

#         for i in range(len(query)):
#                 query[i][0] = query[i][0][1:]
#                 temp = query[i][-1] 
#                 query[i][-1] = query[i][0]
#                 query[i][0] = temp
#         query[-1][0] = query[-1][0][:-1]
#         print(query)
#         # get rid of duplicates
       
#         query = set(tuple(i) for i in query)
#         query = list(query)
#     return render_template("/authorNames.html", letter = letter, query=query) 

# # AUTHOR NAMES
# @app.route("/authorNames.html", methods=["POST", "GET"]) # From advanced search
# def displayNames(): # display author names
#     if(request.method == "GET"):
#         return render_template("authorNames.html") # it should never bet accessed through a get, so maybe we default it to home page
#     else: # POST
#         name = request.form["name"]
#         print("Name Displayed: ", name)
#         # if article written by multiple people:
#         # if(";" in name):
#         #     nameList = name.split(";") #COME BACK TO THIS
#         #article written by one person
#         nameList = name.split() # this doesn't work so great if we have a person with two first names
#         print(nameList)
#         if(len(nameList) == 2):
#             queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%, {nameList[0]}%' && regauthor LIKE '{nameList[1]}%' order by regauthor;"
#             curr = mysql.connection.cursor()
#             curr.execute(queryString)
#             fetchdata = curr.fetchall()
#             if(not fetchdata): # if we have nothing after that query, that means that the author has written an author with other people
#                 queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%, {nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' order by regauthor;"
#                 curr = mysql.connection.cursor()
#                 curr.execute(queryString)
#                 fetchdata = curr.fetchall()
#         elif(len(nameList) == 3):
#             queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%, {nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' && regauthor LIKE '{nameList[2]}%' order by regauthor;" # I think something happens when I don't have % in front of the last namelist
#             curr = mysql.connection.cursor()
#             curr.execute(queryString)
#             fetchdata = curr.fetchall()
#             if(not fetchdata):
#                 queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%, {nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' && regauthor LIKE '%{nameList[2]}%' order by regauthor;" # I think something happens when I don't have % in front of the last namelist
#                 curr = mysql.connection.cursor()
#                 curr.execute(queryString)
#                 fetchdata = curr.fetchall()
#         elif(len(nameList) == 4):
#             queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%, {nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' && regauthor LIKE '%{nameList[2]}%' && regauthor LIKE '{nameList[3]}%' order by regauthor;"
#             curr = mysql.connection.cursor()
#             curr.execute(queryString)
#             fetchdata = curr.fetchall()
#             if(not fetchdata):
#                 queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%, {nameList[0]}%' && regauthor LIKE '%{nameList[1]}%' && regauthor LIKE '%{nameList[2]}%' && regauthor LIKE '%{nameList[3]}%' order by regauthor;"
#                 curr = mysql.connection.cursor()
#                 curr.execute(queryString)
#                 fetchdata = curr.fetchall()
#         else:     
#             queryString = f"SELECT id, regauthor FROM authors WHERE regauthor LIKE '%{name}%' order by regauthor;" # add author to select
#         curr = mysql.connection.cursor()
#         curr.execute(queryString)
#         fetchdata = curr.fetchall()
#         curr.close()
#         return redirect(url_for("authorResults", letterOrName = name, query=fetchdata)) # put in the function of the url you want to go to
# # VOLUME & ISSUE SEARCH
# @app.route("/volumeIssue.html", methods=["POST", "GET"]) # From advanced search
# def displayVolumes():
#     return render_template("volumeIssue.html")


# # RESULTS

@app.route("/Results/<values>-<enteredText>", methods=["POST", "GET"]) 
def basicResults1(values, enteredText): 
    print(values)

    values = values.replace("(", "")
    values = values.replace(")", "")
    # values = values.split("',")

    values = re.split("', |\",", values)
    print(values)

    # values[-1] = values[-1].replace(values[-1][-1][-1], "", 1)
    for i in range(len(values)):
        values[i] = values[i].split(",")

    print(values)
    for i in range(len(values)):
        values[i][1] = values[i][1][2:]
        temp = values[i][-2] 
        values[i][-2] = values[i][-1]
        values[i][-1] = temp
    
    values[-1][1] = values[-1][1][:-1]

    print(values)
    return render_template("index.html", flask_token = values, searchedText = enteredText)# we're just using enteredText to display it

# @app.route("/resultsPage/<topics>", methods=["POST", "GET"]) 
# def basicResults2(topics=None): # all articles related to a certain topic

#     return render_template("resultsPage.html", topics=topics)

# @app.route("/resultsPage/<queryAd>-<topics>-<enteredText>", methods=["POST", "GET"]) # since we redirected it, it expects to see <query> and <topics> in the URL
# def advancedResults(queryAd, topics, enteredText): # this input str var will eventually get converted into a SQL query to be ran against the database to return results.
#     # if(request.method == "GET"):
#     queryAd = None

#     print("topics:", topics) # when we don't have a query the hyphen stays. So we'll have to strip it later on
#     return render_template("resultsPage.html", queryAd=queryAd, topics=topics, enteredText=enteredText)

# # AUTHOR RESULTS

# @app.route("/authorList/<letterOrName>-<query>", methods=["POST", "GET"])
# def authorResults(letterOrName, query): # query right now is the data retrieved from the sql query
#     if(len(letterOrName) == 1): # then it's a letter. When is this ever the case?
#         query = query.replace("(", "")
#         query = query.replace(")", "")
#         query = re.split("', |\",", query)
#         # print(query)
#         for i in range(len(query)):
#             query[i] = query[i].split(",")
#         # print(query)
#         for i in range(len(query)):
#             query[i][1] = query[i][1][2:]
#             temp = query[i][-2] 
#             query[i][-2] = query[i][-1]
#             query[i][-1] = temp
#         query[-1][1] = query[-1][1][:-1]
#         # print(query)
#         return #render_template("authorList.html", authorNames=query) # this needs to go to a different page (i.e. not authorList). Just one with all the names of a particular letter
#     else: # name typed in
#         multipleNames = False
#         print("start", query)
#         query = ast.literal_eval(query)
#         query = list(query)
#         articleDict = {} # key = article ID : val = author(s)
#         print("Here: ", query[0], query[0][0]) 
#         for a, b in query:
#             b = re.split(",|;", b)
#             if(len(b) > 2):
#                 for i in reversed(range(2, len(b)-1, 2)):
#                     b[i] = b[i]+","
#             # b = b.split(",")
#             # if(";" in b):
#             #     b = b.split(";")
#             # b = b.replace(",", "")
#             articleDict[a] = b

        

#         # query = query.replace("(", "")
#         # query = query.replace(")", "")
#         # query = query.replace(";", ",")
#         # query = query.replace("\'", "") # get rid of extra quotes
#         # if(query[-1] == ","): # there's a comma at the end of the names of people with only one article
#         #     query = query[:-1]
#         # print(query)
#         # if(";" in query):
#         #     multipleNames = True
#         # query = re.split("\', |\",|;", query)
#         # print(query)
#         # if(multipleNames == True): #This is only the case when a specific person is the co-author of just 1 article 
#         #     query[0] = query[0][:query[0].index("\'")] + query[0][query[0].index("\'")+1:] # this gets rid of the leading quote
#         #     query[-1] = query[-1][:query[-1].index("\'")] + query[-1][query[-1].index("\'")+1:] # this gets rid of the ending quote
#         # print(query)
#         # for i in range(len(query)):
#         #     query[i] = query[i].split(",")
#         # print(query)
#         # if(multipleNames == True):
#         #     for i in range(len(query)):
#         #         query[i][1] = query[i][1][1:] # when we have multiple authors, because we split on ;, we don't have the leading '
#         #         temp = query[i][-2] 
#         #         query[i][-2] = query[i][-1]
#         #         query[i][-1] = temp
#         #     print(query)
#         #     newQuery = []
#         #     for i in query:
#         #         for j in i:
#         #             newQuery.append(j)
#         #     query = newQuery
#         #     print(query)
#         #     for i in range(2,len(query)-1,2):
#         #         query[i] = query[i]+", "
#         # else:
#         #     for i in range(len(query)):
#         #         query[i][1] = query[i][1][2:]
#         #         temp = query[i][-2] 
#         #         query[i][-2] = query[i][-1]
#         #         query[i][-1] = temp
#         #     print(query)
#         #     query[-1][1] = query[-1][1][:-1]
#         print(articleDict)
#         print(type(query))
#         return render_template("authorList.html", name=letterOrName, articleDict=articleDict) # return all articles written by an author



# @app.route("/autocomplete", methods=["POST", "GET"])
# def autocomplete():
#     return reduce(lambda x, y: str(x) + ',' + str(y),
#             [item for sublist in search(request.form["word"]) for item in sublist])



if __name__ == "__main__":
    app.run(debug=True, use_reloader = True)