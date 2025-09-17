import sqlite3
from flask import g

def connect_db():
    sql = sqlite3.connect('./recipe_database.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

def close_db(error = None):
    if hasattr(g, 'sqlite3_db'):
        g.sqlite3_db.close()

def init_app(app):
    app.teardown_appcontext(close_db)