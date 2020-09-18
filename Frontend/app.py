from flask import Flask, request, render_template

app = Flask(__name__)

# def hello_world():
#     return "Hello World2"

@app.route("/")
def home():
    return render_template("index.html") # display the html page

@app.route("/advancedSearch.html")
def displayAdvanced():
    return render_template("advancedSearch.html") # display the html page

@app.route("/", methods=["POST", "GET"]) # From basic search
def my_form_post():
    # text = request.form["query"]
    # processed_text = text.upper()

    return render_template("resultsPage.html")

@app.route("/resultsPage.html")
def results():
    return render_template("resultsPage.html")

@app.route("/advancedSearch.html", methods=["POST", "GET"]) # From advanced search
def my_form_post2():
    # text = request.form["query"]
    # processed_text = text.upper()

    return render_template("resultsPage.html")

# @app.route("/results")
# def displayResults():
#     return render_template("resultsPage.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)