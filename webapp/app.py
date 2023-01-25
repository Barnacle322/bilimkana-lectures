from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False      

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

userlist = []


@app.get("/add/<name>")
def index(name: str):
    userlist.append(name.capitalize())
    return "Added"


@app.get("/userlist")
def users():
    return render_template("users.html", userlist=userlist)


if __name__ == "__main__":
    app.run(debug=True)
