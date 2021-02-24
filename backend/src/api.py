import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()


@app.route('/drinks')
def drinks():
    # Get a list of the short version of drinks. Aboart 422 if the request
    # couldn't be processed
    try:
        list = Drink.query.all()
        return jsonify({'success': True, 'drinks': [i.short() for i in list]})
    except BaseException:
        aboart(422)


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def drinks_detail(payload):
    # Get a list of the long version of drinks. Aboart 422 if the request
    # couldn't be processed
    try:
        list = Drink.query.all()
        return jsonify({'success': True, 'drinks': [i.long() for i in list]})
    except BaseException:
        aboart(422)


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def new_drink(payload):
    # Create new drink
    data = request.get_json()
    try:
        drink = Drink()
        drink.title = data['title']
        drink.recipe = json.dumps(data['recipe'])
        drink.insert()
        return jsonify({'success': True, 'drinks': [drink.long()]})
    except BaseException:
        abort(422)


@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def drink_update(payload, id):
    # Update drink
    data = request.get_json()

    drink = Drink.query.filter_by(id=int(id)).one_or_none()
    if drink is None:
        abort(404)
    if 'title' in data:
        drink.title = data['title']
    if 'recipe' in data:
        drink.recipe = json.dumps(data.get('recipe'))
    drink.update()
    return jsonify({'success': True, 'drinks': [drink.long()]})


@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    # Delete the drink with provided id
    try:
        drink = Drink.query.get(id)
        drink.delete()
        return jsonify({'success': True, 'deleted': id})
    except BaseException:
        abort(404)


# Error Handling

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable'
    }), 422


@app.errorhandler(404)
def notfound(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Resource not found'
    }), 404


@app.errorhandler(401)
def unauth(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'Unauthirized'
    }), 401


@app.errorhandler(AuthError)
def handle_auth_error(error):
    return jsonify({
        'success': False,
        'error': error.error,
        'message': error.error['description']
    }), error.status_code
