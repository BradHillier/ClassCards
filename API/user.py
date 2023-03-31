"""Handle user related functionality, including routing requests
"""

from flask import Blueprint, Flask, request, jsonify, session
import db
import bcrypt



user = Blueprint('user', __name__)

@user.route("/login")
def test_route():
    return "hello from user.py login route!"

@user.route("/login", methods=["POST"])
def login_POST():
    """attempts to log the user in with recieved POSTed username & password
    """

    content = request.get_json(force=True)
    print(content)

    username = content['username']
    password = content['password']

    # HASH PASSWORDS
    
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    # Debugging test: ensure password can be checked against hash
    test = password.encode("utf-8")
    result = bcrypt.checkpw(test, hash)

    # TODO: Access database and check pwdhash against input
        
    #test = get_DB()


    # For now, just let any username and password create a session
    if result == True:
        session["username"] = username    
        session["logged_in"] = True 

    
    if "username" in session:
        print("session exists?")
        print(session["username"])



    return jsonify(content)


@user.route("/logout")
def logout():
    """Log the user out by removing all variables from session
    """
    session.pop("username", None)
    session.pop("logged_in", None)
    return "Logged out"
    

        
    
    
    
