import os
from flask import Flask, render_template

template_dir= os.path.abspath("./Frontend/templates")
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/advancedSearch")
def advancedSearch():
    return render_template("advancedSearch.html")

if __name__ == "__main__":
    app.run(debug=True)
