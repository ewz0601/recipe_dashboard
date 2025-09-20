from flask import request, render_template
from database.app_setup.connect_to_database import get_db
from database.get_recipes import get_all_recipes, get_recipe_by_id

def view_recipes():
    """
    Route to display recipe list and optionally a selected recipe.
    """
    db = get_db()
    recipes = get_all_recipes(db)

    selected_id = request.args.get('id')
    selected_recipe = get_recipe_by_id(db, selected_id) if selected_id else None

    return render_template("recipes.html", recipes=recipes, selected=selected_recipe)
