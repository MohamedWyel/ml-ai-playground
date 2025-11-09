# put and delete APIs
# working with API--(Json) using flask
# to-do list application
from flask import Flask, jsonify, request
app = Flask(__name__)

# in-memory data structure to store to-do items
todos = [
    {'id': 1, 'item': 'Learn Flask', 'description': 'Study the Flask web framework'},
    {'id': 2, 'item': 'Build API', 'description': 'Create a RESTful API using Flask'},
    {'id': 3, 'item': 'Test API', 'description': 'Test the API endpoints'},
    {'id': 4, 'item': 'Deploy API', 'description': 'Deploy the API to a server'},
    {'id': 5, 'item': 'Maintain API', 'description': 'Monitor and maintain the API'},
]
@app.route('/')
def home():
    return "welcome to To-Do List application"
#GET retrieve all to-do items
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

#GET retrieve a specific to-do item by id
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None) # find item by id(iterate through list and match id)
    if todo:
        return jsonify(todo)
    return jsonify({'message': 'To-Do item not found'}), 404

#POST create a new to-do item
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(new_todo), 201

#PUT update an existing to-do item by id
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo:
        updated_data = request.get_json()
        todo.update(updated_data)
        return jsonify(todo)
    return jsonify({'message': 'To-Do item not found'}), 404