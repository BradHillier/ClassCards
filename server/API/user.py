"""Handle user related functionality, including routing requests
"""

from flask import Blueprint, Flask, request, jsonify
import db

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

    print(content['test'])

    username = content['username']
    pwd      = content['password']

    # TODO: hash pwd, test against username entry

    test = get_DB()
    
    
    return jsonify(content)
