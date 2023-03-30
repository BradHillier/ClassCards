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

    # get a list of existing decks
    if request.method == 'GET':
        search_param = request.args.get('search')

        # get all the decks
        if not search_param:
            decks = [{
                        'name': 'Deck 1',
                        'deckID': 1,
                        'isPublic': True,
                        'tags': [],
                        'author': 'kermit',
                        'authorID': 1
                    }]

        # get just decks matching the search parameter
        else:
            decks = [{
                        'name': f'{search_param} deck',
                        'deckID': 1,
                        'isPublic': True,
                        'tags': [search_param],
                        'author': 'kermit',
                        'authorID': 1
                    }]
        return {'decks': decks}, 200

    # create a new deck
    if request.method == 'POST':
        # TODO: add ability to create a new deck
        return {'message': 'successfully created a new deck'}, 201


@api_bp.route('/api/decks/<int:deckID>/cards', methods=['GET', 'POST'])
def deck_cards(deckID: int):

    # get a list of cards belonging to the deck with the provided ID
    if request.method == 'GET':
        if deckID == 1:
            return [
                {
                    'front': 'what is the answer to this question?',
                    'back': 'this is the answer',
                    'cardID': 1,
                    'isApproved': True,
                    'tags': [],
                    'author': 'kermit',
                    'authorID': 1,
                    'deckID':  1,
                    'rating': 0
                }
            ], 200
        else:
            return {'error': 'Invalid deck id'}, 400

    # add a list of cards to the deck with the provided id
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
