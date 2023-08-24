from models.db import db

class Outfit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    category = db.Column(db.Text, nullable=True)
    tipe_outfit = db.Column(db.Text, nullable=True)
    outlet = db.Column(db.Text, nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, provider_id, title, description, gender, category, tipe_outfit, outlet, lead_time, image, price):
        self.provider_id = provider_id
        self.title = title
        self.description = description
        self.gender = gender
        self.category = category
        self.tipe_outfit = tipe_outfit
        self.outlet = outlet
        self.lead_time = lead_time
        self.image = image
        self.price = price

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "title": self.title,
            "description": self.description,
            "gender": self.gender,
            "category": self.category,
            "tipe_outfit": self.tipe_outfit,
            "outlet": self.outlet,
            "lead_time": self.lead_time,
            "image": self.image,
            "price": self.price,
        }
