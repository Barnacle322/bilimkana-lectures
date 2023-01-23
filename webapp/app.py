from flask import Flask, render_template

app = Flask(__name__)

userlist = []


@app.get("/add/<name>")
def index(name: str):
    userlist.append(name.capitalize())
    return "Added"


@app.get("/userlist")
def users():
    return render_template("users.html", userlist=userlist)
