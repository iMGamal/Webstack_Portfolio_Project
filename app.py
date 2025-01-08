"""These are the modules for the application."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """Define a user table in the database."""
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), unique = True, nullable = False)


class Quiz(db.Model):
    """Define a quiz table in the database."""
    quiz_id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(250), unique = True, nullable = False)
    correct_option = db.Column(db.String(125), unique = True, nullable = False)
    option1 = db.Column(db.String(125), unique = True, nullable = False)
    option2 = db.Column(db.String(125), unique = True, nullable = False)
    option3 = db.Column(db.String(125), unique = True, nullable = False)
    option4 = db.Column(db.String(125), unique = True, nullable = False)


class Score(db.Model):
    """Define a score table in the database."""
    score_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.ForeignKey('user.user_id'), nullable = False)
    score = db.Column(db.Integer, nullable = False)
    score_timestamp = db.Column(db.DateTime, default = db.func.current_timestamp(), nullable = False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    """Return the home page."""
    return "Welcome to the home page!"


if __name__ == '__main__':
    app.run(debug = True)
