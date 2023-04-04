from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/admin"

db.init_app(app)

with app.app_context():
    from routes.main import *
    from models import Article

    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




