from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    grade = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f"Student('{self.name}', '{self.age}', '{self.grade}')"


@app.get("/")
def index():
    return redirect(url_for("users"))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        grade = request.form["grade"]

        student = Student(name=name, age=age, grade=grade)

        db.session.add(student)
        db.session.commit()

    return render_template("add.html")


@app.get("/users")
def users():
    students = db.session.query(Student).all()
    return render_template("users.html", students=students)


@app.get("/delete/<int:id>")
def delete(id: int):
    student = db.session.query(Student).filter(Student.id == id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("users"))


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id: int):
    student = db.session.query(Student).filter(Student.id == id).first()

    if request.method == "POST":
        student.name = request.form["name"]
        student.age = request.form["age"]
        student.grade = request.form["grade"]

        db.session.commit()
        return redirect(url_for("users"))

    return render_template("update.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)
