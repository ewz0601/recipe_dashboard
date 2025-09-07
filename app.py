from flask import Flask, g, request, jsonify, render_template
import sqlite3

# for next time E: https://www.youtube.com/watch?v=sx8DpAVlocg

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect('./recipe_database.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3_db'):
        g.sqlite3_db.close()

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/new_recipe', methods = ['GET', 'POST'])
def new_recipe():
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

        return '<h2> Recipe added successfully </h2><a href="/recipes">View Recipes</a>'
    
    return render_template('new_recipe.html')

@app.route('/recipes')
def view_recipes():
    db = get_db()

    # Get all recipe names for dropdown
    cursor = db.execute('SELECT id, title FROM recipes')
    recipe_list = cursor.fetchall()

    # Get the id of the selected recipe (this comes from the html form)
    selected_id = request.args.get('id')
    selected_recipe = None

    # If there an id selected, pull all the columns for that id
    if selected_id:
        cursor = db.execute(
            'SELECT * FROM recipes WHERE id = ?',
            [selected_id]
        )
        selected_recipe = cursor.fetchone()

    return render_template("recipes.html", 
                           recipes = recipe_list,
                           selected = selected_recipe)


if __name__ == '__main__':
    app.run(debug=True)