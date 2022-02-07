import sqlite3
from flask import g

def connect_db():
    return sqlite3.connect("database.db")

def get_db():
    db=getattr(g, 'db', None)
    if db is None:
        db = g.db=connect_db()
    return db

def disconnect_db():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        g.db = None

def create_profile(email, password, firstname, familyname, gender, city, country):
    try:
        get_db().execute("insert into contact values(?, ?, ?, ?, ?, ?, ?, ?)", [email, password, firstname, familyname, gender, city, country])
        get_db().commit()
        return True
    except:
        return False

def getby_email(email):
    cursor = get_db().execute("select * from contact where name like ?", [email])
    rows = cursor.fetchall()
    cursor.close()
    return rows