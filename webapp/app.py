from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    grade = db.Column(db.String(3), nullable=False)


@app.get("/add/<name>")
def index(name: str):
    student = Student(name=name, age=18, grade="11A")

    db.session.add(student)
    db.session.commit()
    return "Added"


@app.get("/userlist")
def users():
    return render_template("users.html")


if __name__ == "__main__":
    app.run(debug=True)
