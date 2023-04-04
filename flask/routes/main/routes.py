from app import app
from models import Article
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template("main/index.html")

@app.route("/all")
def all():
    article = Article.query.all()
    return render_template("main/all.html", articles=article)

@app.route("/article/<int:id>")
def article_details(id):
    article = Article.query.get(id)
    return render_template("main/article_detail.html", article=article)


@app.route("/calc/<int:x>/<int:y>")
def calc(x, y):
    return render_template("main/calc.html", x=x, y=y, sum=x + y)


@app.route("/calc/<int:x>/<int:y>/-")
def calc_minus(x, y):
    return render_template("main/calc_minus.html", x=x, y=y, sum=x - y)





