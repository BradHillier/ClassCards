from flask import Blueprint, jsonify, request


card = Blueprint('card', __name__)


@card.route('/api/cards/<int:cardID>/comments', methods=['GET', 'POST'])
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

@card.route('/api/cards/<int:cardID>/ratings', methods=['GET', 'POST'])
def card_ratings(cardID: int):

   # check if a user has rated a card and what type of rating they provided
   if request.method == 'GET':
       user = request.args.get('user')
       if user:
           return {'type': 1}, 200
       else:
           return {'error': 'no user id provided'}, 400

   if request.method == 'POST':
    pass
