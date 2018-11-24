from flask import Flask
app = Flask(__name__)

@app.route("/search")
def search():
    return "Hello World!"
