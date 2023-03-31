from flask import Flask, session
from flask_session import Session

from API.user import user
from API.decks import deck
from API.cards import card

from db import get_DB

app = Flask(__name__)

app.secret_key = "test string, DO NOT USE IN DEPLOYMENT!!!"
# filesystem: store session info on the server under folder "flask_session"
app.config["SESSION_TYPE"] = "filesystem"

#build the session
Session(app)


db_session = get_DB()

app.register_blueprint(user)
app.register_blueprint(deck)
app.register_blueprint(card)

@app.route("/")
def hello():
    if "logged_in" in session:
        return "<p>Hello, Kermit!</p>"
    return "<p>hello, world!</p>"


@app.route("/test/<test_str>")
def show_input(test_str):
    return f'/test/{test_str}'



# /api/



