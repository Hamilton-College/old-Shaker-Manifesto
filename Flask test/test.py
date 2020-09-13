from flask import Flask

app = Flask(__name__)

@app.route('/') #which URL triggers function
def hello_world():
    return "Hello World!"
