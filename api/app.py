import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from dotenv import load_dotenv  # Agrega esta línea
from flask_admin import Admin
from admin import setup_admin
from flask_admin.contrib.sqla import ModelView
from flask import Flask
from models.index import db, User
from domain.user.route import user_route


load_dotenv()


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

with app.app_context():
    db.create_all()



@app.route('/')
def index():
    return 'Hola mundo'

user = user_route(app)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
