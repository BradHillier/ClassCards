

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>hello, world!</p>"


@app.route("/test/<test_str>")
def show_input(test_str):
    return f'/test/{test_str}'



# /api/

