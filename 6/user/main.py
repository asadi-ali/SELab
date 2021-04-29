from flask import Flask, request, jsonify
from db import run_migrations, close_connection, query_db

app = Flask(__name__)


@app.before_first_request
def start_up():
    run_migrations()


@app.teardown_appcontext
def tear_down(exception):
    close_connection()


@app.route('/user/show-profile', methods=['GET'])
def show_profile():
    username = request.headers.get('User')
    if username:
        info = query_db('select * from profile where username=?', [username])
        if info:
            return jsonify(info[0]), 200
        else:
            return jsonify({'error': 'Bad request.'}), 400
    else:
        return jsonify({'error': 'Please login first.'}), 401


@app.route('/user/edit-profile', methods=['POST'])
def edit_profile():
    username = request.headers.get('User')
    if username:
        info = query_db('select * from profile where username=?', [username])
        if info:
            email = request.json.get('email')
            phone = request.json.get('phone')
            email = info[0].get('email') if email is None else email
            phone = info[0].get('phone') if phone is None else phone
            query_db('update profile set email=?, phone=? where username=?', [email, phone, username], with_commit=True)
            return jsonify({}), 200
        else:
            return jsonify({'error': 'Bad request.'}), 400
    else:
        return jsonify({'error': 'Please login first.'}), 401


@app.route('/user/create-profile', methods=['POST'])
def create_profile():
    username = request.json.get('username')
    email = request.json.get('email')
    phone = request.json.get('phone')
    user_type = request.json.get('type')
    query_db("""
            insert into profile(username, email, phone, type)
            values (?, ?, ?, ?)
        """, [username, email, phone, user_type], with_commit=True)
    return jsonify({}), 201


@app.route('/user/all-profiles', methods=['GET'])
def all_profiles():
    user_type = request.headers.get('UserType')
    if user_type == 'admin':
        info = query_db('select * from profile where type=?', ['client'])
        if info:
            return jsonify(info), 200
        else:
            return jsonify({'error': 'No record found.'}), 404
    elif user_type == 'client':
        return jsonify({'error': 'Only admin can perform this action.'}), 403
    else:
        return jsonify({'error': 'Please login first.'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
