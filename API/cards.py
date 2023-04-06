from flask import Blueprint, jsonify, request

from db import get_DB

card = Blueprint('card', __name__)


@card.route('/api/cards/<int:cardID>/comments', methods=['GET', 'POST'])
def card_comments(cardID: int):
    """Handle actions related to comments on a specific card

    Parameters:
        cardID (int): The ID of the card to perform an action on

    GET: get a list of comments for the specified card

        Example usage:
            curl http://127.0.0.1:5000/api/cards/1/comments

        Returns:
            a list containing a collection of comments in JSON format. Each card has the 
            following fields: 

                id      (int):  the unique identifier for the comment
                content (str):  the message left on the comment by a user
                cardID  (int):  the identifier for the card the comment was left on
                userID  (int):  the identifier of the user who left the comment
        
    POST: add a comment to the specified card

        Example usage:
            curl http://127.0.0.1:5000/api/cards/1/comments -d '{
                "content": "this card is great", 
                "userID: 45
            }'

        Returns:
            If the request was valid, a 201 status code and a json message indicating
            that the  comment was successfully created. Otherwise, a 400 status code
            along with a json error messaging indicating which portion of the request 
            was invalid
    """
    if request.method == 'GET':

        query = "SELECT * FROM Feedback"

        dbs = get_DB()
        crs = dbs.cursor()

        try:
            crs.execute(query)

        except mysql.connector.Error as err:
            print(err)    
        

        result = crs.fetchall();

        return jsonify(result), 200
        
        if cardID == 1:
            return [
                  {
                    'id': 1,
                    'content': 'this card is very good',
                    'cardID': 1,
                    'userID': 45  
                  },
                  {
                    'id': 2,
                    'content': 'this card is very bad',
                    'cardID': 1,
                    'userID': 1
                  }
            ], 200
        else:
            return {'error': 'Invalid card id'}, 400

    if request.method == 'POST':

        content = request.json

        comment = content["content"]
        userID = content["userID"]

        query = "INSERT INTO Feedback (content, cardID, userID) VALUES (%s, %s, %s)"
        params = (content, cardID, userID,)
        dbs = get_DB()
        crs = dbs.cursor()

        try:
            crs.execute(query, params)
            
        except mysql.connector.Error as err:
            print(err)

        cursor.close()
        dbs.close()
            
        # TODO: add functionality for adding a card to a deck
        return {'success': 1}, 200

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
       # TODO: Check if user has rated card before, don't apply same rating twice
       return {'success': 1}, 200
   pass
