import requests
from flask import Flask

from db import run_migrations, close_connection, query_db

create_profile_endpoint = 'http://localhost:5002/user/create-profile'


def create_admin():
    app = Flask(__name__)
    with app.app_context():
        run_migrations()
        username = 'admin'
        password = 'admin_password'

        response = requests.post(create_profile_endpoint, json={
            'username': 'admin',
            'email': 'admin@selab.com',
            'phone': '09120000000',
            'type': 'admin'
        })

        if response.status_code != 201:
            raise Exception(response.json())

        query_db("""
                insert into auth_user(username, password)
                values (?, ?);
            """, args=(username, password), with_commit=True)

        close_connection()
        print('Admin created.')


if __name__ == '__main__':
    create_admin()
