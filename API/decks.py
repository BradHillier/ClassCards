from flask import Blueprint, jsonify, request

import mysql.connector
from db import get_DB
import sys

deck = Blueprint('deck', __name__)


@deck.route('/api/decks', methods=['GET', 'POST'])
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
        print("POST!")

        content = request.json

        #print(content)

        
        
        deck_name = content["name"]
       # print(deck_name)
        is_public = content["isPublic"]
        author_id = content["authorID"]
        cards     = content["cards"]

        
       # print(is_public)
       # print(author_id)
       # print(cards)

        # return {'message': 'test'}, 403
        
        # Check if authorID = ID in session before creating query



        # Set up DB session

        dbs = get_DB()
        crs = dbs.cursor()

        # Prepare sql statement
        sql = "INSERT INTO Deck  (name, isPublic, ownerID) VALUES (%s, %s, %s)"
        params = (deck_name, is_public, author_id,)
        
        try:
            crs.execute(sql, params)
            result = crs.fetchall()
        except mysql.connector.Error as err:
            print("Error at insert deck: ", err)

        # get the database ID of the deck for card inserts
        deck_id = crs.lastrowid
            
        ins_cards = []
        card_tags = []


        future = []
        
        ins_query = "INSERT INTO Card (front, back, isApproved, deckID) VALUES (%s,%s,%s,%s)"
        
        # for each card, add to array and place tags in a tag array mapped to cardID
        try:
            for card in cards:
                is_approved = True

                f = card["front"]
                b = card["back"]
                tags = card["tags"]
                
                # insert front, back, approved, deckid) tuple into array of cards for
                # one pass execution
                ins_cards.append( (f, b, is_approved, deck_id ) )

                
                for tag in tags:
                    # save card tags for another insert
                    card_tags.append(tag)
                    future.append( (f, b, tag,) )
                    print(tag)
                
        except mysql.connector.Error as err:
            print("Error: ", err)

        try:
            # attempt insert on every card in ins_cards
            crs.executemany(ins_query, ins_cards)
        except mysql.connector.Error as err:
            print("Error at insert every card: ", err)

        '''
        # get last card ID from insert
        card_last_id = crs.lastrowid
        card_start_id = len(card_tags) - card_last_id

        # Map card ID to a tag set
        itr_start = card_start_id
        
        cid_to_tags = []
        for tag_set in ins_cards:
            for tag in tag_set:
                cid_to_tags.append( (itr_start, tag) )   
            itr_start += 1
        

        formatted_tags = []
        for tag in card_tags:
            formatted_tags.append( (tag,) )
        
        # MYSQL: insert ignore will ignore existing tags in DB
        ins_tags_query = "INSERT IGNORE INTO Tag (tag) VALUES (?)"


        print(formatted_tags)
        
        try:
            crs.executemany(ins_tags_query, formatted_tags)
        except mysql.connector.Error as err:
            print("Error at insert tags: ", err)

        # commit changes before next part
        dbs.commit()

        qry = "INSERT INTO TagAssociation (cardID, tagID) VALUES ( (SELECT Card.ID FROM Card WHERE Card.front =%s AND Card.back=%s LIMIT 1), (SELECT Tag.ID FROM Tag WHERE Tag.tag =%s LIMIT 1) )"
            
        #Inserts a tag association using the id, and a select statement to find the ID of the tag
        ins_tag_assoc = "INSERT INTO TagAssociation (cardID, tagID) VALUES (%s, (SELECT Tag.ID FROM Tag WHERE Tag.tag = %s LIMIT 1))"

        # TODO: Insert tag associations into table for each tag on a card 
        try:
            crs.executemany(qry, future)
        except mysql.connector.Error as err:
            print("error at ins tag associations: ", err)
            
        # NOTE: do not uncomment until everything is working, otherwise partial
        #       changes could be made to DB unintended
        '''    
        dbs.commit()
            
        crs.close()
        dbs.close()
    
        # TODO: add ability to create a new deck
        return {'message': 'successfully created a new deck'}, 201


@deck.route('/api/decks/<int:deckID>/cards', methods=['GET', 'POST'])
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


        content = request.json
        
        front = content["front"]
        back  = content["back"]
       # author = content["authorID"]
        # front = content["tags"]
        deck = content["deckID"]


        query = "INSERT INTO Card (front, back, isApproved, deckID) VALUES (%s, %s, True, %s)"
        params = (front, back, deck,)


        
        dbs = get_DB()
        crs = dbs.cursor()

        
        try:
            crs.execute(query, params)

        except mysql.connector.Error as err:
            print(err)

            
        dbs.commit()
        crs.close()
        dbs.close()
        return {"message": "successfully added a new card to deck"}, 201
