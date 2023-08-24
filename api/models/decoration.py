from models.db import db

class Decoration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    type_decoration = db.Column(db.Text, nullable=True)
    rent_sale = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)
    other = db.Column(db.String(255), nullable=True)
    assembly = db.Column(db.Boolean(), nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(255), nullable=True)

    def __init__(self, provider_id, name, title, description, category, type_decoration, rent_sale, price, other, assembly, lead_time, image):
        self.provider_id = provider_id
        self.name = name
        self.title = title
        self.description = description
        self.category = category
        self.type_decoration = type_decoration
        self.rent_sale = rent_sale
        self.price = price
        self.other = other
        self.assembly = assembly
        self.lead_time = lead_time
        self.image = image

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "type_decoration": self.type_decoration,
            "rent_sale": self.rent_sale,
            "price": self.price,
            "other": self.other,
            "assembly": self.assembly,
            "lead_time": self.lead_time,
            "image": self.image,
        }
