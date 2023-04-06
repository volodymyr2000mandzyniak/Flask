from app import app, db
from models import Article
from flask import render_template, request, redirect


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

@app.route("/article_create")
def article_create():
    return render_template("main/article_form.html")

@app.route("/article", methods=["POST"])
def article_save():
    data = request.form
    article = Article(title=data.get("title"), body=data.get("body"))
    db.session.add(article)
    db.session.commit()
    return redirect("/all")


@app.route("/article/<int:id>/edit")
def article_edit(id):
    article = Article.query.get(id)
    return render_template("main/article_form.html", article=article)


@app.route("/article/<int:id>/update", methods=["POST"])
def article_update(id):
    article = Article.query.get(id)
    article.title = request.form.get("title")
    article.body = request.form.get("body")
    db.session.add(article)
    db.session.commit()
    return  redirect("/all")

@app.route("/article/<int:id>/delete")
def article_delete(id):
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return redirect("/all")

