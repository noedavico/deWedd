from models.db import db

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    best_seller = db.Column(db.String(255), nullable=True)
    type_product = db.Column(db.Text, nullable=True)
    vegan = db.Column(db.Boolean(), nullable=True)
    eco = db.Column(db.Boolean(), nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    custom = db.Column(db.Boolean(), nullable=True)
    catalogo = db.Column(db.String(255), nullable=True)
    order_min = db.Column(db.Integer, nullable=True)
    order_max = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, provider_id, title, name, description, best_seller, type_product, vegan, eco, lead_time, custom, catalogo, order_min, order_max, image, price):
        self.provider_id = provider_id
        self.title = title
        self.name = name
        self.description = description
        self.best_seller = best_seller
        self.type_product = type_product
        self.vegan = vegan
        self.eco = eco
        self.lead_time = lead_time
        self.custom = custom
        self.catalogo = catalogo
        self.order_min = order_min
        self.order_max = order_max
        self.image = image
        self.price = price

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "title": self.title,
            "name": self.name,
            "description": self.description,
            "best_seller": self.best_seller,
            "type_product": self.type_product,
            "vegan": self.vegan,
            "eco": self.eco,
            "lead_time": self.lead_time,
            "custom": self.custom,
            "catalogo": self.catalogo,
            "order_min": self.order_min,
            "order_max": self.order_max,
            "image": self.image,
            "price": self.price,
        }
