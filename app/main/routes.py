from flask import render_template
from app.main import bp


@bp.route("/")
def index():
    return render_template("main/index2.html")

@bp.route("/about")
def about():
    return render_template("main/about.html")

@bp.route("/questions_and_answers")
def questions_and_answers():
    return render_template("main/questions_and_answers.html")
