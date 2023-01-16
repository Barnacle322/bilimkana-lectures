from flask import Flask

app = Flask(__name__)

userlist = []


@app.get("/add/<name>")
def index(name):
    userlist.append(name)
    return "Added"

@app.get("/userlist")
def users():
    return userlist