from app import app, db
from models import Article
from flask import render_template, request, redirect




@app.errorhandler(404)
def pageNotFount(error):
    return render_template("layouts/page_404.html", title="Page not fount")



@app.route("/all")
def all():
    articles = Article.query.all()
    return render_template("main/all.html", articles=articles)


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
    return redirect("/all")


@app.route("/article/<int:id>/delete")
def article_delete(id):
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return redirect("/all")


@app.route("/search")
def search():
    q = request.args.get("q", "")
    articles = Article.query.filter(Article.title.like("%" + q + "%") | Article.body.like("%" + q + "%")).all()
    return render_template("main/all.html", articles=articles)
