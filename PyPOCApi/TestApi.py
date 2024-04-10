# save this as app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (replace with your actual data)
data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
}

# GET endpoint for retrieving all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data['users'])

# GET endpoint for retrieving a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in data['users'] if user['id'] == user_id]
    if user:
        return jsonify(user[0])
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)