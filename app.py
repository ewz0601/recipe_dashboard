from flask import Flask
from database.app_setup.close_database import init_app
from routes.view_recipes import view_recipes
from routes.create_new_recipes import create_new_recipes


app = Flask(__name__)

# Initialize database teardown
init_app(app)

@app.route('/')
def run_view_recipes():
    return view_recipes()

@app.route('/new_recipe', methods = ['GET', 'POST'])
def run_create_new_recipe():
    return create_new_recipes()

if __name__ == "__main__":
    app.run(debug=True)
