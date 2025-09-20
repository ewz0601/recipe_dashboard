def insert_recipe(db, data):
    """
    Insert a new recipe into the database.

    Args:
        db (sqlite3.Connection): Database connection.
        data (dict): Form data with keys: title, ingredients, amounts, units, directions.
    """
    db.execute(
        "INSERT INTO recipes (title, ingredients, amounts, directions, units) VALUES (?,?,?,?,?)",
        [data['title'], data['ingredients'], data['amounts'], data['directions'], data['units']]
    )
    db.commit()