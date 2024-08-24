from flask import render_template
from flask import Flask
app = Flask(__name__)

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>This is Jack Li!</p>"

@app.route("/test")
def test():
    return render_template('test.html')

@app.route('/')
def hello_world():
    return 'Hello, World!'