from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

'''
@api_bp.route('/api/data')
def data():
    # Your JSON response code here
    return jsonify({'data': 'Hello, World!'})
'''

@api_bp.route('/api/decks')
def get_decks():
    decks = [{'title': 'Deck 1'}, {'title': 'Deck 2'}, {'title': 'Deck 3'}]
    return jsonify({'decks': decks})
