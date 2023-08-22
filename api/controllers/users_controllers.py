from flask import jsonify, request

from utils import db
from models import User

def get():
    query = db.select(User).order_by(User.username)
    users = db.session.execute(query).scalars()
    users = [user.serialize_with_projects() for user in users]
    return jsonify(users), 200

def post():
    user = User(**request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201