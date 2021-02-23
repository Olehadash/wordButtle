from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from .model import User, Rooms, db
from flask_socketio import SocketIO, emit, send
from . import socketio
import time

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login_post():

    Name = request.form.get('Name')
    DeviceID = request.form.get('DeviceID')

    user = User.query.filter_by(Name=Name).first()

    if not user:
        new_user = User(Name = Name, DeviceID = DeviceID)
        db.session.add(new_user)
        db.session.commit()
        return 'USER CREATED'

    if user.DeviceID != DeviceID:
        return 'USER EXIST'

    return 'USER ENTERED'

@auth.route('/createroom', methods=['POST'])
def createroom():
    Name = request.form.get('Name')
    CreatorName = request.form.get('CreatorName')

    room = Rooms(Name=Name, CreatorName=CreatorName, ConnectorName="-", isShown=0)
    db.session.add(room)
    db.session.commit()

    time.sleep(2)

    r = Rooms.query.all()

    return jsonify(rooms = [i.serialize for i in r]),200

@auth.route('/deleteroom', methods=['POST'])
def deleteroom():
    Name = request.form.get('Name')
    CreatorName = request.form.get('CreatorName')

    room = Rooms.query.filter_by(Name=Name).first()
    db.session.delete(room)
    db.session.commit()

    time.sleep(2)

    r = Rooms.query.all()

    return jsonify(rooms = [i.serialize for i in r]),200


@auth.route('/connectroom', methods=['POST'])
def connectroom():
    Name = request.form.get('Name')
    CreatorName = request.form.get('CreatorName')
    ConnectorName = request.form.get('ConnectorName')

    room = Rooms.query.join(Rooms.Name).filter(Rooms.Name == Name, Rooms.CreatorName == CreatorName, Rooms.isShown == 0)
    if not room:
        return 'NO ROOM'
    if room.isShown == 1:
        return 'NO ROOM'
    room.ConnectorName = ConnectorName;
    room.isShown = 1
    db.session.commit()

    time.sleep(2)

    r = Rooms.query.all()

    return jsonify(rooms = [i.serialize for i in r]),200