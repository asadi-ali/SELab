from flask import Flask, request, jsonify
from db import run_migrations, close_connection, query_db

app = Flask(__name__)


@app.before_first_request
def start_up():
    run_migrations()


@app.teardown_appcontext
def tear_down(exception):
    close_connection()


@app.route('/book/create', methods=['POST'])
def create():
    user_type = request.headers.get('UserType')
    if user_type == 'admin':
        title = request.json.get('title')
        category = request.json.get('category')
        query_db("""
                    insert into book(title, category)
                    values (?, ?)
                """, [title, category], with_commit=True)
        return jsonify({}), 201
    elif user_type == 'client':
        return jsonify({'error': 'Only admin can perform this action.'}), 403
    else:
        return jsonify({'error': 'Please login first.'}), 401


@app.route('/book/update', methods=['PUT'])
def update():
    user_type = request.headers.get('UserType')
    if user_type == 'admin':
        id = request.json.get('id')
        info = query_db('select * from book where id=?', [id])
        if info:
            title = request.json.get('title')
            category = request.json.get('category')
            title = info[0].get('title') if title is None else title
            category = info[0].get('category') if category is None else category
            query_db('update book set title=?, category=? where id=?', [title, category, id], with_commit=True)
            return jsonify({}), 200
        else:
            return jsonify({'error': 'Bad request.'}), 400
    elif user_type == 'client':
        return jsonify({'error': 'Only admin can perform this action.'}), 403
    else:
        return jsonify({'error': 'Please login first.'}), 401


@app.route('/book/delete', methods=['DELETE'])
def delete():
    user_type = request.headers.get('UserType')
    if user_type == 'admin':
        id = request.json.get('id')
        info = query_db('select * from book where id=?', [id])
        if info:
            query_db('delete from book where id=?', [id], with_commit=True)
            return jsonify({}), 200
        else:
            return jsonify({'error': 'Bad request.'}), 400
    elif user_type == 'client':
        return jsonify({'error': 'Only admin can perform this action.'}), 403
    else:
        return jsonify({'error': 'Please login first.'}), 401


@app.route('/book/retrieve', methods=['GET'])
def retrieve():
    user_type = request.headers.get('UserType')
    if user_type == 'admin':
        id = request.json.get('id')
        info = query_db('select * from book where id=?', [id])
        if info:
            return jsonify(info[0]), 200
        else:
            return jsonify({'error': 'Bad request.'}), 400
    elif user_type == 'client':
        return jsonify({'error': 'Only admin can perform this action.'}), 403
    else:
        return jsonify({'error': 'Please login first.'}), 401


@app.route('/book/search', methods=['POST'])
def search():
    if 'User' not in request.headers:
        return jsonify({'error': 'Please login first.'}), 401

    filters = []
    if 'category' in request.json:
        filters.append(('category', request.json.get('category')))
    if 'title' in request.json:
        filters.append(('title', request.json.get('title')))

    query = 'select * from book where '
    query_args = []
    if len(filters) == 0:
        return jsonify({'error': 'You should add at least one filter.'}), 400
    elif len(filters) == 1:
        query += '{} = ?'.format(filters[0][0])
        query_args.append(filters[0][1])
    else:
        query += '{} = ? and {} = ?'.format(filters[0][0], filters[1][0])
        query_args.extend([filters[0][1], filters[1][1]])

    info = query_db(query, query_args)
    if info:
        return jsonify(info), 200
    else:
        return jsonify({'error': 'There is no book with these filters.'}), 404


if __name__ == '__main__':
    app.run(port=5003)
