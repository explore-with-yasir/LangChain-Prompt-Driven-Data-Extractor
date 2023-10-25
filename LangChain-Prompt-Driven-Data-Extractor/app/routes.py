from app import app
from flask import jsonify, request

# Define a simple route
@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

# Define an example route that accepts parameters
@app.route('/greet/<name>')
def greet(name):
    return jsonify(message=f'Hello, {name}!')

# Define a POST route that accepts JSON data
@app.route('/post_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify(received_data=data)

# Define more routes as needed for your application

# Example error handling
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error='Internal server error'), 500
