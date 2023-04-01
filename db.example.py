import mysql.connector


def get_DB():
    """Creates and returns a connection to the database
    """
    mdb = mysql.connector.connect(
        host="",
        database="",
        user="",
        password=""
    )
    return mdb

