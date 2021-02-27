"""
The flask application package.
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, make_response
from flask_socketio import SocketIO, emit, send, disconnect


app = Flask(__name__)
db = SQLAlchemy()
socketio = SocketIO(app, logger=True, engineio_logger=True)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ALGORITHM'] = 'HS512'
db.init_app(app)

from .words import words as words_blueprint
app.register_blueprint(words_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)



@socketio.on('connect')
def connect():
    print('Client connected')
    send('Connected')

@socketio.on('disconnect')
def disconnect():
    
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('message', data, broadcast=True)

@socketio.on('rooms')
def room_message(data):
    emit('rooms', data, broadcast=True)