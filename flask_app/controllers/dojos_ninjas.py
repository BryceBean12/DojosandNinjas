from flask_app import app


from flask import render_template, redirect, request

# Sample on how we get class from our models
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja



@app.route("/dojos")
def main():
    dojos = Dojo.get_all_rows();
    return render_template("dojos.html", dojos=dojos)

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.insert_row(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def ninjas_dojos(id):
    ninjas = Ninja.get_all_rows_from_dojo(id);
    return render_template("dojo_ninjas.html", ninjas=ninjas)


@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all_rows()
    return render_template("ninjas.html", dojos=dojos)

@app.route("/new_ninja", methods = ["POST"])
def new_ninja():
    print(request.form)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.insert_row(data)
    return redirect("/dojos")