
# are all of these being used? session?
from flask import Flask, session, jsonify, request, render_template, redirect, url_for
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


# db_session = get_DB()

# API
app.register_blueprint(user)
app.register_blueprint(deck)
app.register_blueprint(card)

#@app.route("/")
#def hello():
#    if "logged_in" in session:
#        return "<p>Hello, Kermit!</p>"
#    return "<p>hello, world!</p>"
#
#
#@app.route("/test/<test_str>")
#def show_input(test_str):
#    return f'/test/{test_str}'

@app.route('/', methods=['GET'])
def home():
    if "logged_in" in session:
        return render_template('index.html')
    else:
        return redirect( url_for("login") )
    # return jsonify({'message': 'Hello, World!'})

@app.route('/upload_deck', methods=['GET'])
def upload_deck():

    if "logged_in" in session:
        return render_template('upload_deck.html')
    else:
        return redirect( url_for("login") )
    


@app.route('/view_decks', methods=['GET'])
def view_deck():
    
    if "logged_in" in session:
        return render_template('view_decks.html')
    else:
        return redirect( url_for("login") )
    

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)




