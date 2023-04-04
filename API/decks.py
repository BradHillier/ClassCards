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

        deck_name = request.form["name"]
        is_public = request.form["is_public"]
        author_id = request.form["authorID"]
        cards = request.form["cards"]



        # Check if authorID = ID in session before creating query



        # Set up DB session

        dbs = get_DB()
        crs = dbs.get_cursor()

        # Prepare sql statement
        sql = "INSERT (name, isPublic, ownerID) INTO Deck VALUES (?, ?, ?)"
        params = (deck_name, is_public, author_id,)
        
        try:
            crs.execute(sql, params)
            result = crs.fetchall()
        except mysql.Connector.Error as err:
            sys.exit(err)

        # get the database ID of the deck for card inserts
        deck_id = crs.lastrowid
            
        ins_cards = []
        card_tags = []

        ins_query = "INSER INTO Card (front, back, isApproved, deckID) VALUES (?,?,?,?)"
        
        # for each card, add to array and place tags in a tag array mapped to cardID
        try:
            for f, b, t in cards:
                is_approved = True

                # insert front, back, approved, deckid) tuple into array of cards for
                # one pass execution
                ins_cards.append( (f, b, is_approved, deck_id ) )

                # save card tags for another insert
                card_tags.append(t)
                
        except mysql.Connector.Error as err:
            print(err)

        try:
            # attempt insert on every card in ins_cards
            crs.executemany(ins_query, ins_cards)
        except mysql.Connector.Error as err:
            print(err)

        # get last card ID from insert
        card_last_id = crs.lastrowid

        card_start_id = card_tags.len - card_last_insert

        ins_tags = []

        # Collect all tags from different cards into one set
        for tag_set in card_tags:
            # Use set theory to merge tags without duplicates :>
            ins_tags = list( set(ins_tags) | set(tag_set) )

        # MYSQL: insert ignore will ignore existing tags in DB
        ins_tags_query = "INSERT IGNORE INTO Tag (tag) VALUES (?)"

        try:
            crs.executemany(ins_tags_query, ins_tags)
        except mysql.Connector.Error as err:
            print(err)


    # TODO: Insert tag associations into table for each tag on a card 

    
    
    
            
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
        pass
