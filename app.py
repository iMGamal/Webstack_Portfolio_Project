"""These are the modules for the application."""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    """Return the home page."""
    return "Welcome to the home page!"


if __name__ == '__main__':
    app.run(debug = True)
