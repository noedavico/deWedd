from models.db import db

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    type_vehicle = db.Column(db.Text, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    leet = db.Column(db.String(100), nullable=True)
    time_for = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    
    def __init__(self, provider_id, title, name, description, type_vehicle, capacity, leet, time_for, price, lead_time, image):
        self.provider_id = provider_id
        self.title = title
        self.name = name
        self.description = description
        self.type_vehicle = type_vehicle
        self.capacity = capacity
        self.leet = leet
        self.time_for = time_for
        self.price = price
        self.lead_time = lead_time
        self.image = image


    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "title": self.title,
            "name": self.name,
            "description": self.description,
            "type_vehicle": self.type_vehicle,
            "capacity": self.capacity,
            "leet": self.leet,
            "time_for": self.time_for,
            "price": self.price,
            "lead_time": self.lead_time,
            "image": self.image,
        }
