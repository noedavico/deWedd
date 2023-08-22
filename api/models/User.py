from utils import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    # created_at = db.Column(db.DateTime,
    #                         default=db.func.current_timestamp())
    # updated_at = db.Column(db.DateTime,
    #                         default=db.func.current_timestamp(),
    #                         onupdate=db.func.current_timestamp())
    projects = db.relationship('Project',
                                secondary='user_project',
                                backref='users')

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }
    
    def serialize_with_projects(self):
        return {
            "id": self.id,
            "username": self.username,
            "projects": [project.serialize() for project in self.projects]
        }