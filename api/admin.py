import os
from flask_admin import Admin
from models.index import db, User, Beauty, Cake, Gift, Wedding_car, Transport, Animation, Outfit, Music, Decoration
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='DeWedd', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session)),
    admin.add_view(ModelView(Cake, db.session)),
    admin.add_view(ModelView(Beauty, db.session)),
    admin.add_view(ModelView(Gift, db.session)),
    admin.add_view(ModelView(Wedding_car, db.session)),
    admin.add_view(ModelView(Transport, db.session)),
    admin.add_view(ModelView(Animation, db.session)),
    admin.add_view(ModelView(Outfit, db.session)),
    admin.add_view(ModelView(Music, db.session)),
    admin.add_view(ModelView(Decoration, db.session)),