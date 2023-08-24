from models.db import db

class Beauty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    genero = db.Column(db.String(100), nullable=True)
    at_home = db.Column(db.Boolean(), nullable=True)
    tipe_serv = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, provider_id, name, title, description, genero, at_home, tipe_serv, category, image, lead_time, price):
        self.provider_id = provider_id
        self.name = name
        self.title = title
        self.description = description
        self.genero = genero
        self.at_home = at_home
        self.tipe_serv = tipe_serv
        self.category = category
        self.image = image
        self.lead_time = lead_time
        self.price = price

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "genero": self.genero,
            "at_home": self.at_home,
            "tipe_serv": self.tipe_serv,
            "category": self.category,
            "image": self.image,
            "lead_time": self.lead_time,
            "price": self.price,
        }
