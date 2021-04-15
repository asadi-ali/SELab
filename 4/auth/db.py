import sqlite3
from flask import g

DATABASE = 'database.db'


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
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


def query_db(query, one=False):
    cur = get_db().execute(query)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
