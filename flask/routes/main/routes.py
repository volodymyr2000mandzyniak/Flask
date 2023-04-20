from app import app, db
from models import Article
from flask import render_template, request, redirect


@app.route("/")
def index():
    return render_template("main/index.html")
