from models.db import db

class Animation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    type_animation = db.Column(db.Text, nullable=True) 
    services = db.Column(db.Text, nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, provider_id, title, name, description, type_animation, services, lead_time, image, price):
        self.provider_id = provider_id
        self.title = title
        self.name = name
        self.description = description
        self.type_animation = type_animation
        self.services = services
        self.lead_time = lead_time
        self.image = image
        self.price = price

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "title": self.title,
            "name": self.name,
            "description": self.description,
            "type_animation": self.type_animation,
            "services": self.services,
            "lead_time": self.lead_time,
            "image": self.image,
            "price": self.price,
        }
