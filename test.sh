#!/bin/bash
curl -XPOST -H "Content-type: application/json" -d '{ 
    "name": "sample deck", 
    "isPublic": true, 
    "authorID": 1, 
    "cards": [ 
        { "front": "hello", "back": "world", "tags": ["none"] } 
        ] 
}' 'localhost:5000/api/decks'
