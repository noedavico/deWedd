from flask import Blueprint

from .users_routes import users_routes


api = Blueprint("api", __name__)

api.register_blueprint(users_routes, url_prefix='/users')

