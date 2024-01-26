from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Naila"
    return "This is my new website"