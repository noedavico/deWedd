from models.db import db

class Cake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    custom = db.Column(db.Boolean(), nullable=False)
    catalogue = db.Column(db.String(255), nullable=True)
    order_min = db.Column(db.Integer, nullable=True)
    order_max = db.Column(db.Integer, nullable=True)
    delivery = db.Column(db.Boolean(), nullable=True)
    assembly = db.Column(db.Boolean(), nullable=True)
    preparation = db.Column(db.Text, nullable=True)
    type_cake = db.Column(db.Text, nullable=True)
    leadtime = db.Column(db.String(255), nullable=True)

    def __init__(self, provider_id, name, image, custom, catalogue, order_min, order_max, delivery, assembly, preparation, type_cake, leadtime):
        self.provider_id = provider_id
        self.name = name
        self.image = image
        self.custom = custom
        self.catalogue = catalogue
        self.order_min = order_min
        self.order_max = order_max
        self.delivery = delivery
        self.assembly = assembly
        self.preparation = preparation
        self.type_cake = type_cake
        self.leadtime = leadtime

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "name": self.name,
            "image": self.image,
            "custom": self.custom,
            "catalogue": self.catalogue,
            "order_min": self.order_min,
            "order_max": self.order_max,
            "delivery": self.delivery,
            "assembly": self.assembly,
            "preparation": self.preparation,
            "type_cake": self.type_cake,
            "leadtime": self.leadtime,
        }
