from flask import Flask, g
import sqlite3
import jsonify
import requests as request

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

@app.route('/users')
def viewusers():
    db = get_db()
    cursor = db.execute('SELECT id, name, age FROM users')
    results = cursor.fetchall()
    if results:
        return f"<h1>The ID is {results[0]['id']}. <br> The name is {results[0]['name']}.<br> The age is {results[0]['age']}. <br>"
    else:
        return "<h1>No users found.</h1>"

@app.route('/users', methods = ['post'])
def create_user():
    db = get_db()
    name = request.json['name']
    age = request.json['age']
    db.execute('INSERT INTO users (name, age) VALUES (?,?)', [name, age])
    db.commit()
    return jsonify({'message': 'User created successfully!'})

if __name__ == '__main__':
    app.run(debug=True)