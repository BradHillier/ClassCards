from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

'''
@api_bp.route('/api/data')
def data():
    # Your JSON response code here
    return jsonify({'data': 'Hello, World!'})
'''

@api_bp.route('/api/decks', methods=['GET', 'POST'])
def get_decks():
    if request.method == 'GET':
        decks = [
                    {'title': 'Deck 1'}, 
                    {'title': 'Deck 2'}, 
                    {'title': 'Deck 3'}
                ]
        return jsonify({'decks': decks}), 200
    if request.method == 'POST':
        # TODO: add ability to create a new deck
        return {'message': 'successfully created a new deck'}, 201

