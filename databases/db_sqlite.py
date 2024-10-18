import sqlite3


def one():
    # make a connection to a sqlite database
    con = sqlite3.connect("tutorial.db")
    # similar to any other relational database, open a cursor
    # acursor is like the client to the database

    # a cursor is like a 'actor' that one can execute on a database.
    cur = con.cursor()
    cur.execute()

    # cursor fetch

    con.commit()

    # closing a cursor
