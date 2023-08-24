from models.db import db

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    type_music = db.Column(db.Text, nullable=True)
    style = db.Column(db.Text, nullable=True)
    system = db.Column(db.String(255), nullable=True)
    phase_music = db.Column(db.String(100), nullable=True)
    live_music = db.Column(db.Boolean(), nullable=True)
    sound_equipment = db.Column(db.Boolean(), nullable=True)
    assembly = db.Column(db.Boolean(), nullable=True)
    lead_time = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, provider_id, title, description, category, type_music, style, system, phase_music, live_music, sound_equipment, assembly, lead_time, image, price):
        self.provider_id = provider_id
        self.title = title
        self.description = description
        self.category = category
        self.type_music = type_music
        self.style = style
        self.system = system
        self.phase_music = phase_music
        self.live_music = live_music
        self.sound_equipment = sound_equipment
        self.assembly = assembly
        self.lead_time = lead_time
        self.image = image
        self.price = price

    def serialize(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "type_music": self.type_music,
            "style": self.style,
            "system": self.system,
            "phase_music": self.phase_music,
            "live_music": self.live_music,
            "sound_equipment": self.sound_equipment,
            "assembly": self.assembly,
            "lead_time": self.lead_time,
            "image": self.image,
            "price": self.price,
        }
