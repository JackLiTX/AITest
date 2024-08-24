from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is Jack Li!</p>"

@app.route("/test")
def test():
    return render_template('test.html')