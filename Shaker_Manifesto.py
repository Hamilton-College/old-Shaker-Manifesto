import os
from flask import Flask, render_template

template_dir = os.path.abspath("./Frontend/templates")
static_dir = os.path.abspath("./Frontend/static")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir )

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/advancedSearch.html")
def advancedSearch():
    return render_template("advancedSearch.html")

@app.route("/resultsPage.html")
def results():
    return render_template("resultsPage.html")

if __name__ == "__main__":
    app.run(debug=True)
