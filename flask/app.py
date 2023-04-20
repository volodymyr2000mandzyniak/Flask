from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@db:3306/admin"
db = SQLAlchemy(app)
app.secret_key='btC2bDn9ZJOGgZbX000i6ahOTibbaE4T'

# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


# db.init_app(app)


with app.app_context():
    from routes.main import *
    from routes.articles import *
    from routes.users import *
    from models import Article, User


    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



