from flask import Flask, request, jsonify

from .db import run_migrations, close_connection, query_db

app = Flask(__name__)


@app.before_first_request
def start_up():
    run_migrations()


@app.teardown_appcontext
def tear_down(exception):
    close_connection()


@app.route('/auth/sign-up', methods=['POST'])
def sign_up():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    phone = request.json.get('phone')
    # TODO: Validate this values

    # TODO: send request to profile
    query_db("""
        insert into auth_user(username, password)
        values ({username}, {password})
    """.format(username=username, password=password))

    return jsonify({}), 201
