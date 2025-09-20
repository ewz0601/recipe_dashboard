import sqlite3
from flask import g

def connect_db():
    """
    Establish a connection to the SQLite database.

    The connection uses `sqlite3.Row` as the row factory,
    allowing column access by name.

    Returns:
        sqlite3.Connection: A database connection object.
    """
    sql = sqlite3.connect('./recipe_database.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    """
    Retrieve the database connection for the current request context.

    If no connection exists yet, one is created and stored in `g`.

    Returns:
        sqlite3.Connection: The database connection object.
    """
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db


def close_db(error=None):
    """
    Close the database connection if one exists.

    This is intended to be called at the end of the request context.

    Args:
        error (Exception | None): Optional error raised during teardown.
    """
    if hasattr(g, 'sqlite3_db'):
        g.sqlite3_db.close()


def init_app(app):
    """
    Register database teardown with the Flask application.

    Ensures that `close_db` is called automatically when
    the application context ends.

    Args:
        app (Flask): The Flask application instance.
    """
    app.teardown_appcontext(close_db)
