import os
from dotenv import load_dotenv  # Agrega esta línea

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

from flask import Flask
from utils import db
from models.User import User
from routes.api import api

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(debug=True, port=4000)
