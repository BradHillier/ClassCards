from flask import Flask

from API.user import login_page

app = Flask(__name__)


app.register_blueprint(login_page)

@app.route("/")
def hello():
    return "<p>hello, world!</p>"


@app.route("/test/<test_str>")
def show_input(test_str):
    return f'/test/{test_str}'



# /api/



