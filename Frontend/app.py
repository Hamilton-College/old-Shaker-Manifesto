from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Shakers!"
app.config["MYSQL_DB"] = "sample-db"

mysql = MySQL(app)

# BASIC SEARCH

# POST is to send/change data.
@app.route("/", methods=["POST", "GET"])
def basicSearch():
    print(app.root_path)
    if(request.method == "GET"):
        return render_template("index.html")
    else: # POST
        if(not request.form["query"]):
            return render_template("index.html") # maybe display a flash message here

        query = request.form["query"] # name in brackets matches the name of the post form in the HTML
        enteredText = query
        queryString = f"SELECT articleid from article where author = '{query}';"
        print(queryString)
        curr = mysql.connection.cursor()
        curr.execute(queryString)
        fetchdata = curr.fetchall()
        curr.close()

        # return render_template("resultsPage.html", query=query) # query(left) is the name of the variable we put in the html.
        return redirect(url_for("basicResults1", query=fetchdata, enteredText = enteredText)) # put in the function of the url you want to go to



# ADVANCED SEARCH

@app.route("/advancedSearch.html", methods=["POST", "GET"]) # From advanced search
def displayAdvanced():
    print("Start")
    if(request.method == "GET"):
        return render_template("advancedSearch.html")
    else: # POST
        if(not request.form["query"] and not request.form.getlist("checkbox")): # if no boxes checked and nothing entered
            return render_template("advancedSearch.html")
        elif(request.form.getlist("checkbox")): # If we have a box checked
            # print("Boxes checked:", request.form.getlist("checkbox"))
            topics = request.form.getlist("checkbox")
        else: # if no checkboxes checked, and just text entered
            topics = None
            # print("topics:", topics)
        query = request.form["query"] # name matches the name of the post form in the HTML
        query = query.upper()
        print("query:", query)
            # return render_template("resultsPage.html", query=query) # query(left) is the name of the variable in results.html. Right var is the one here.
        if(query and topics):
            return redirect(url_for("advancedResults", query=query, topics = topics)) # put in the function of the url you want to go to
        elif(not topics):
            print("why?")
            return redirect(url_for("basicResults1", query = query)) # put in the function of the url you want to go to
        elif(not query):
            return redirect(url_for("basicResults2", topics = topics)) # put in the function of the url you want to go to
        else:
            print("Here: ",topics, query)
            return render_template("advancedSearch.html")

# RESULTS

# def results(query=None, topics=None, topicOrQuery=None): # this input str var will eventually get converted into a SQL query to be ran against the database to return results.
#     # if(request.method == "GET"):
#     if(topicOrQuery):
#         if(topicOrQuery.isalnum()):
#             query = topicOrQuery
#         else:
#             topics = topicOrQuery

#     print(query)
#     print("topics:", topics) # when we don't have a query the hyphen stays. So we'll have to strip it later on
#     return render_template("resultsPage.html", query=query, topics=topics)
@app.route("/resultsPage/<query>-<enteredText>", methods=["POST", "GET"]) # since we redirected it, it expects to see <query> and <topics> in the URL
def basicResults1(enteredText, query=None): # this input str var will eventually get converted into a SQL query to be ran against the database to return results.
    # this is to figure out if it's a topic or query
    print(type(query))
    query = query.split("),")
    for i in range(len(query)):
        j = 0
        while(j < len(query[i])):
            if(query[i][j].isalnum() == False):
                query[i] = query[i].replace(query[i][j], "", 1)
            else:
                j += 1
    print(query)
    return render_template("resultsPage.html", query=query, enteredText=enteredText)#, topics=topics)

@app.route("/resultsPage/<topics>", methods=["POST", "GET"]) # since we redirected it, it expects to see <query> and <topics> in the URL
def basicResults2(topics=None): # this input str var will eventually get converted into a SQL query to be ran against the database to return results.
    # this is to figure out if it's a topic or query

    return render_template("resultsPage.html", topics=topics)

@app.route("/resultsPage/<query>-<topics>", methods=["POST", "GET"]) # since we redirected it, it expects to see <query> and <topics> in the URL
def advancedResults(query=None, topics=None, topicOrQuery=None): # this input str var will eventually get converted into a SQL query to be ran against the database to return results.
    # if(request.method == "GET"):
    if(topicOrQuery):
        if(topicOrQuery.isalnum()):
            query = topicOrQuery
        else:
            topics = topicOrQuery

    print(query)
    print("topics:", topics) # when we don't have a query the hyphen stays. So we'll have to strip it later on
    return render_template("resultsPage.html", query=query, topics=topics)



if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)
