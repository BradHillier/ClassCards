from flask import Blueprint, jsonify, abort

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/decks')
def get_decks():
    decks = [{'title': 'Deck 1', 'id': '0000001'}, {'title': 'Deck 2', 'id': '0000002'}, {'title': 'Deck 3', 'id': '0000003'}]
    return jsonify({'decks': decks})

@api_bp.route('/api/decks/<int:deckID>/cards', methods=['GET'])
def get_cards(deckID):

    # TODO: Implement code to retrieve cards for the specified deckID
    # You can use the deckID parameter to query the database or data source
    # and retrieve the corresponding cards.

    # Example response with dummy data
    cards = [
        {
            "id": 1,
            "front": "What is the capital of France?",
            "back": "Paris"
        },
        {
            "id": 2,
            "front": "What is the tallest mountain in the world?",
            "back": "Mount Everest"
        }
    ]

    # Check if the deckID is valid and return a 404 error if not
    if deckID < 1 or deckID > 10:  # Assuming deckIDs are between 1 and 10
        abort(404)

    # Return a JSON response with the cards for the specified deckID
    return jsonify(cards)
