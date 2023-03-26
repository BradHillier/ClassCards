"""Handle user related functionality, including routing requests
"""

from flask import Blueprint, Flask, request, jsonify, session
import db
import bcrypt



login_page = Blueprint('user_login', __name__)

@login_page.route("/login")
def test_route():
    return "hello from user.py login route!"

@login_page.route("/login", methods=["POST"])
def login_POST():
    """attempts to log the user in with recieved POSTed username & password
    """

    content = request.get_json(force=True)
    print(content)

    username = content['username']
    password = content['password']

    # TODO: hash pwd, test against username entry

    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    # Debugging test: ensure password can be checked against hash
    test = password.encode("utf-8")
    result = bcrypt.checkpw(test, hash)


    if result == True:
        session["username"] = username    
    
    
    #test = get_DB()


    


    
        
    
    
    return jsonify(content)
