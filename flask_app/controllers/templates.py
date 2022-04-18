from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.template import User


@app.route("/")
def main():
    return render_template("template.html")

@app.route("/sample_post", methods = ["POST"])
def main_post():
    print(request.form) 
    return redirect("/")