from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

BASE_DIR = os.getcwd()

@app.route("/", methods=["GET", "POST"])
def index():
    d = str(datetime.now()).split(" ")[1].split(".")[0]
    return render_template("index.html", title="Base")


@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        new_todo = dict(request.form)
        title = new_todo["title"]
        description = new_todo["description"]

        f = open(BASE_DIR + "\\data\\todo.txt", "w")
        f.write(f"{title}:{description}\n")
        f.close()


    with open(BASE_DIR + "\\data\\todo.txt", "r") as f:
        lines = f.readlines()
    
    todos = []
    for line in lines:
        todos.append({
            "title": line.split(":")[0],
            "description": line.split(":")[1].replace("\n", "")
        })

    return render_template("todo.html", todos=todos)


app.run(host='0.0.0.0', port='8000', debug=True)
