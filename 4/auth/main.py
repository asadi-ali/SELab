from flask import Flask, request, g

from .user import User
from .db import run_migrations, close_connection

app = Flask(__name__)


@app.before_first_request
def start_up():
    run_migrations()


@app.teardown_appcontext
def tear_down(exception):
    close_connection()


@app.route('/auth/sign-up', methods=['POST'])
def sign_up():
    return ''
