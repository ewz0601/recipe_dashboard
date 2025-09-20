def get_all_recipes(db):
    """
    Fetch all recipes.

    Args:
        db (sqlite3.Connection): Database connection.

    Returns:
        list[sqlite3.Row]: List of recipes with id and title.
    """
    cursor = db.execute('SELECT id, title FROM recipes')
    return cursor.fetchall()


def get_recipe_by_id(db, recipe_id):
    """
    Fetch a single recipe by ID.

    Args:
        db (sqlite3.Connection): Database connection.
        recipe_id (int | str): Recipe ID.

    Returns:
        sqlite3.Row | None: Recipe row if found, else None.
    """
    cursor = db.execute('SELECT * FROM recipes WHERE id = ?', [recipe_id])
    return cursor.fetchone()
