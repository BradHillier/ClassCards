"""Handle user related functionality, including routing requests
"""

from flask import Blueprint, Flask, request, jsonify, session, render_template
from db import get_DB
import bcrypt



user = Blueprint('user', __name__)

@user.route("/login")
def test_route():
    return render_template("login.html")

@user.route("/login", methods=["POST"])
def login_POST():
    """attempts to log the user in with recieved POSTed username & password
    """

    #content = request.get_json(force=True)
    #print(content)

    email = request.form['email']
    password = request.form['password']

    # HASH PASSWORDS
    
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    # Debugging test: ensure password can be checked against hash
    # test = password.encode("utf-8")
    # result = bcrypt.checkpw(test, hash)

    # TODO: Access database and check pwdhash against input
        
    dbs = get_DB()

    crs = dbs.cursor()
    
    sql = "SELECT * from User WHERE Email = %s AND password = %s"
    adr = (email, password)

    crs.execute(sql, adr)

    result = crs.fetchall()

    pwd_encode = password.encode("utf-8")

    pee = "empty"
    
    for (e, p) in result:
        if e == email and bcrypt.checkpw(pwd_encode, p.encode("utf-8")) == True:
            session["email"] = email    
            session["logged_in"] = True 
            pee = p
            
    
    # For now, just let any username and password create a session
#    if result == True:
#        session["username"] = username    
#        session["logged_in"] = True 

    
    if "email" in session:
        print("session exists?")
        print(session["email"])

        return "cool beans!"


    #return jsonify(content)
    return "hello! : "
    

@user.route("/logout")
def logout():
    """Log the user out by removing all variables from session
    """
    session.pop("email", None)
    session.pop("logged_in", None)
    return "Logged out"
    

        
    
    
    
