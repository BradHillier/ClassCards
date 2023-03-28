from flask import Flask, jsonify, request, render_template
from api import api_bp

app = Flask(__name__)

# Register the bluerpint.
app.register_blueprint(api_bp)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    # return jsonify({'message': 'Hello, World!'})

@app.route('/upload_deck', methods=['GET'])
def upload_deck():
    return render_template('upload_deck.html')


@app.route('/view_decks', methods=['GET'])
def view_deck():
    return render_template('view_decks.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
