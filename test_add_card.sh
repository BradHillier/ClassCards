#!/bin/bash
curl -XPOST -H "Content-type: application/json" -d '{ 
    "front": "Hiya", 
    "back": "world", 
    "deckID": 22 
}' 'localhost:5000/api/decks/22/cards'
