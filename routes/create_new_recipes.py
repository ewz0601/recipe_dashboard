from database.insert_recipes import insert_recipe
from database.app_setup.connect_to_database import get_db
from flask import request, render_template

def create_new_recipes():
    """
    Route to create a new recipe.
    """
    if request.method == 'POST':
        data = request.form.to_dict()
        insert_recipe(get_db(), data)
        return '<h2>Recipe added successfully</h2><a href="/">View Recipes</a>'
    
    return render_template('new_recipe.html')