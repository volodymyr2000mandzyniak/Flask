from app import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    #category_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }


