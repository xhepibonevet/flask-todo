from flask import Flask, render_template, request
from datetime import datetime
import os

from utils import write_file, read_file, transfer_line, lines_to_dict

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
    todos = lines_to_dict(read_file(f="todo"))
    return render_template("todo.html", todos=todos)


@app.route("/done", methods=["GET", "POST"])
def done():
    if request.method == "POST":
        transfer_done = dict(request.form)
        for t in transfer_done:
            transfer_line(f"{t}:{transfer_done[t]}".strip())

    dones = lines_to_dict(read_file(f="done"))
    return render_template("done.html", dones=dones)



app.run(host='0.0.0.0', port='8000', debug=True)
