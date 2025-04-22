from bottle import Bottle, run, request, response, static_file, template, abort, json_dumps
import json
import sqlite3
from database import db_connect, create_user, get_user
from models import User
import hashlib

app = Bottle()

@app.route('/')
def home():
    return template('index.html', root='./views/')

@app.route('/login', method='POST')
def login():
    data = request.json
    email = data.get('email')
    password = data.get('psw')

    print(f"Received data: Email={email}, Password={password}")

    response_data = {
        "message": "Data received successfully",
        "received_data": {
            "email": email,
            "password": password
        }
    }

    response.content_type = 'application/json'
    return json_dumps(response_data)

# @app.route('/register')
# def register_view():
#     return template('register.html', root='./views/')


@app.route('/login/view', method='GET')
def login_view():
    return template('login.html', root='./views/')

# @app.route('/api/register', method='POST')
# def register():
#     try:
#         # Parse JSON data from the request
#         data = request.json
#         if not data:
#             response.status = 400
#             return {'error': 'Invalid JSON data'}

#         # Validate required fields
#         required_fields = ['firstname', 'lastname',
#                            'username', 'email', 'phone', 'role', 'password']
#         for field in required_fields:
#             if field not in data or not data[field]:
#                 response.status = 400
#                 return {'error': f'Missing or empty field: {field}'}

#         # Hash the password
#         hashed_password = hash_password(data['password'])

#         # Insert data into SQLite database
#         conn = db_connect()
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO users (firstname, lastname, username, email, phone, location, role, password)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (
#             data['firstname'],
#             data['lastname'],
#             data['username'],
#             data['email'],
#             data['phone'],
#             # Default to empty string if location is not provided
#             data.get('location', ''),
#             data['role'],
#             hashed_password
#         ))
#         conn.commit()
#         conn.close()

#         response.status = 201
#         return {'message': 'User registered successfully!'}

#     except sqlite3.IntegrityError as e:
#         response.status = 400
#         return {'error': f'Database error: {str(e)}'}

#     except Exception as e:
#         # Log the exception for debugging
#         print(f'Error: {str(e)}')
#         response.status = 500
#         return {'error': 'An internal error occurred'}


# @app.route('/api/login', method='POST')
# def login():
#     # Implement login logic here
#     pass


# @app.route('/api/topics', method='GET')
# def get_topics():
#     # Implement fetching topics logic here
#     pass


# @app.route('/api/topics', method='POST')
# def create_topic():
#     # Implement creating topic logic here
#     pass


# @app.route('/api/topic/<topic_id>', method='GET')
# def get_topic(topic_id):
#     # Implement fetching topic logic here
#     pass


# @app.route('/api/comments', method='POST')
# def create_comment():
#     # Implement creating comment logic here
#     pass


# @app.route('/api/messages', method='POST')
# def create_message():
#     # Implement creating message logic here
#     pass


# def hash_password(password):
#     """Hash a password for storing."""
#     return hashlib.sha256(password.encode()).hexdigest()


@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
