#! /usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", data="blub")

@app.route("/raiden")
def test():
    return render_template("test.html", data="blub")

if __name__ == "__main__":
    app.run()