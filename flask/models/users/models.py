from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(350), nullable=True)
    last_name = db.Column(db.String(220), nullable=True)
    email = db.Column(db.String(220), nullable=False, unique=True )
    password = db.Column(db.String(220), nullable=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "first_bane": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
