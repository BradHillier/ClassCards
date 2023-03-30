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
                    {
                        'name': 'Deck 1',
                        'deckID': 1,
                        'isPublic': True,
                        'tags': [],
                        'author': 'kermit'
                    },
                    {
                        'name': 'Deck 2',
                        'deckID': 2,
                        'isPublic': True,
                        'tags': [],
                        'author': 'kermit'
                    }
                ]
        return jsonify({'decks': decks}), 200
    if request.method == 'POST':
        # TODO: add ability to create a new deck
        return {'message': 'successfully created a new deck'}, 201

@api_bp.route('/api/decks/<int:deckID>/cards', methods=['GET', 'POST'])
def get_deck_cards(deckID: int):
    if request.method == 'GET':
        if deckID == 1:
            return [
                {
                    'cardData': {
                        "noteId": 1672966457463,
                        "tags": [],
                        "fields": {
                            "Question": {
                                "value": "What is the differences between data and information?",
                                "order": 0
                                },
                            "Answer": {
                                "value": "Data is collection of facts, which by itself has no meaning. Information puts those facts into context.",
                                "order": 1
                                }
                            },
                        "modelName": "Basic",
                        "cards": [
                            1672966457465
                            ]
                    },
                    'isApproved': True,
                    'tags': [],
                    'author': 'kermit',
                    'authorID': 0,
                    'deckID':  1,
                    'rating': 0
                }
            ], 200
        else:
            return {'error': 'Invalid deck id'}, 400

    if request.method == 'POST':
        # TODO: add functionality for adding a card to a deck
        pass

@api_bp.route('/api/cards/<int:cardID>/comments', methods=['GET', 'POST'])
def card_comments(cardID: int):
    if request.method == 'GET':
        if cardID == 1:
            return [
                  {
                    'id': 1,
                    'Content': 'this card is very good',
                    'cardID': 1,
                    'userID': 45  
                  },
                  {
                    'id': 2,
                    'Content': 'this card is very bad',
                    'cardID': 1,
                    'userID': 1
                  }
            ], 200
        else:
            return {'error': 'Invalid card id'}, 400
    if request.method == 'POST':
        # TODO: add functionality for adding a card to a deck
        pass
