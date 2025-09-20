from flask import g

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