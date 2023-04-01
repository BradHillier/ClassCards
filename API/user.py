"""Handle user related functionality, including routing requests
"""

from flask import Blueprint, Flask, request, jsonify, session, render_template, redirect, url_for
from db import get_DB
import mysql.connector
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

    # open connection to db
    dbs = get_DB()
    crs = dbs.cursor()
    
    sql = "SELECT username, Email, password from User WHERE Email = %s AND password = %s"

    # all PWD checks must encode the pwd into utf-8 bytes when checking against the hashed result
    adr = (email, password.encode("utf-8"), )

    try:
        crs.execute(sql, adr)
        result = crs.fetchall()
    except mysql.connector.Error as err:
        print(err)

    # if the user's login info is found, create a session 
    for (u, e, p) in result:
        if e == email and bcrypt.checkpw(pwd_encode, p.encode("utf-8")) == True:
            session["email"] = email    
            session["logged_in"] = True
            session["username"] = u


    # close connections to query, cursor, and DB to be safe
    crs.close()
    dbs.close()

    if "email" in session:
        print("session exists?")
        print(session["email"])

        return redirect(url_for("home"))


    #return jsonify(content)
    return "Login failed!"
    

@user.route("/register", methods=["POST"])
def register():
    """Takes registration data and attempts to create a new, unique account

    Example:
        curl -X POST http://127.0.0.1:5000/register \
             -F email=user@example.com -F username=myusername -F password=mypassword
    """
    
    # fetch data from form request
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]

    # prep the existing user check query
    usr_check = "SELECT * FROM User WHERE username = %s OR Email = %s"
    adr = (username, email,)

    # open connection to DB and get a cursor
    dbs = get_DB()
    crs = dbs.cursor()

    try:
        crs.execute(usr_check, adr)
        result = crs.fetchone()
    except mysql.connector.Error as err:
        print(err)

    if result is not None:
        # 409 is the HTTP status code for a conflict
        return {"Error": "existing user with email and username, please try again!"}, 409

    # close result after use
    # result.close() <-- this is a tuple and has no .close() method

    # salt and hash the pwd
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    pwdhash = bcrypt.hashpw(bytes, salt)
        
    # Debugging test: ensure password can be checked against hash
    test = password.encode("utf-8")
    hashres = bcrypt.checkpw(test, pwdhash)

    # prep insert query
    insert = "INSERT INTO User (username, Email, password) VALUES (%s, %s, %s)"
    adr = (username, email, pwdhash, )

    # attempt to insert user data
    try:
        crs.execute(insert, adr)
        #important to actually making changes in the DB
        dbs.commit()
    except mysql.connector.Error as err:
        print(err)

    # close DB connection and cursor
    crs.close()
    dbs.close()

    return redirect(url_for("login"))
    


@user.route("/logout")
def logout():
    """Log the user out by removing all variables from session
    """
    session.pop("email", None)
    session.pop("logged_in", None)
    return "Logged out"
    

        
    
    
    
