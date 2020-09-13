from flask import Flask, request, render_template

app = Flask(__name__)

# def hello_world():
#     return "Hello World2"

@app.route("/")
def home():
    return render_template("index.html") # display the html page


@app.route("/", methods=["POST", "GET"])
def my_form_post():
    # text = request.form["query"]
    # processed_text = text.upper()

    return render_template("resultsPage.html")

# @app.route("/results")
# def displayResults():
#     return render_template("resultsPage.html")

if __name__ == "__main__":
    app.run()