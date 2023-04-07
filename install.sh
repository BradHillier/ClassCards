#!/bin/bash


# ssh -x csci fork csci375/Team5/Project $USER/csci375/Project
# git clone csci:csci375/Team5/Project

# cd Project/

#
cp db.example.py db.py

# install required packages based on pip freeze
pip install -r requirements.txt

echo ""
echo "Note: you will need to configure db.py with database information in order to run the webserver."
read -n 1

clear

