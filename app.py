from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    d = str(datetime.now()).split(" ")[1].split(".")[0]
    return render_template("done.html", ora=d, title="INDEX TITLE")

app.run(host='0.0.0.0', port='8000', debug=True)
