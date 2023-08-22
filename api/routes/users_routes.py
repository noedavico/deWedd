from flask import Blueprint, request

from controllers.users_controllers import get, post

users_routes = Blueprint("users", __name__)

@users_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return get()
    if request.method == 'POST':
        return post()
