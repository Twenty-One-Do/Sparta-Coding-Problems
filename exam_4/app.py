
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import random

def start_rock_scissors_paper(my):
    options = ['scissor', 'rock', 'paper']
    winning_set = [['scissor', 'paper'], ['rock', 'scissor'], ['paper', 'rock']]
    
    com = random.choice(options)
       
    if my == com:
        return {'my': my, 'com': com, 'res':'tie'}
    elif [my, com] in winning_set:
        return {'my': my, 'com': com, 'res':'win'}
    else:
        return {'my': my, 'com': com, 'res':'lose'}

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    my = db.Column(db.String(100), nullable=False)
    com = db.Column(db.String(100), nullable=False)
    res = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('main.html')


@app.route("/choice/<choice>")
def choice(choice):
    result = start_rock_scissors_paper(choice)
    record = Record(username="wondo", my=result['my'], com=result['com'], res=result['res'])
    db.session.add(record)
    db.session.commit()
    return render_template('result.html', result=result)

@app.route("/record/")
def record():
    record = Record.query.filter_by(username='wondo').all()
    return render_template('record.html', record=record)

if __name__ == "__main__":
    app.run(debug=True)
