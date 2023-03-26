from flask import Flask, session

from flask_session import Session

from API.user import login_page

app = Flask(__name__)

app.secret_key = "test string, DO NOT USE IN DEPLOYMENT!!!"
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

app.register_blueprint(login_page)

@app.route("/")
def hello():
    return "<p>hello, world!</p>"


@app.route("/test/<test_str>")
def show_input(test_str):
    return f'/test/{test_str}'



# /api/



