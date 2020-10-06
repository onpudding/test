from flask import Flask,render_templeate
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_templeate("index.html")
