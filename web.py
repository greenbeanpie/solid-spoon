#! /usr/python3
# encoding=utf-8
import flask

app = flask.Flask(__name__)


@app.route("/")

method=["POST"]
def index():
    return "Genshin Impact"

app.run()
