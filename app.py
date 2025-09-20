from flask import Flask, g, request, render_template
from flash_setup import get_db, init_app

app = Flask(__name__)

init_app(app)

@app.route('/new_recipe', methods=['GET', 'POST'])
def create_new_recipe():
    """
    Handle the creation of a new recipe.

    GET:
        Render the new recipe form template.

    POST:
        Accept form data (title, ingredients, amounts, units, directions),
        insert a new recipe into the database, and confirm success.

    Returns:
        str | Response: Success message with link to recipes list (POST),
        or rendered HTML template for recipe creation (GET).
    """
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        amounts = request.form['amounts']
        directions = request.form['directions']
        units = request.form['units']

        db = get_db()
        db.execute(
            "INSERT INTO recipes (title, ingredients, amounts, directions, units) VALUES (?,?,?,?,?)",
            [title, ingredients, amounts, directions, units]
        )
        db.commit()

        return '<h2> Recipe added successfully </h2><a href="/">View Recipes</a>'
    
    return render_template('new_recipe.html')


@app.route('/')
def view_recipes():
    """
    Display a list of all recipes and details for a selected recipe.

    Retrieves all recipe titles for a dropdown list. If a recipe ID is
    provided in query parameters, fetch its details.

    Query Parameters:
        id (int, optional): The ID of the recipe to display in detail.

    Returns:
        Response: Rendered HTML template with recipe list and optionally
        selected recipe details.
    """
    db = get_db()

    # Get all recipe names for dropdown
    cursor = db.execute('SELECT id, title FROM recipes')
    recipe_list = cursor.fetchall()

    # Get the id of the selected recipe (this comes from the html form)
    selected_id = request.args.get('id')
    selected_recipe = None

    # If there is an id selected, pull all the columns for that id
    if selected_id:
        cursor = db.execute(
            'SELECT * FROM recipes WHERE id = ?',
            [selected_id]
        )
        selected_recipe = cursor.fetchone()

    return render_template(
        "recipes.html",
        recipes=recipe_list,
        selected=selected_recipe
    )


if __name__ == '__main__':
    app.run(debug=True)
