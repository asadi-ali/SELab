import sqlite3
from flask import g

DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def run_migrations():
    db = get_db()
    db.execute("""
    create table if not exists auth_user (
        username text primary key,
        password text not null
    );
    """)


def close_connection():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
