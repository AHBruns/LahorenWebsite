from flask import Flask, render_template
import jinja2
import sqlite3


app = Flask(__name__)


@app.route("/")
def root():
    return render_template("root.html")


@app.route("/error_4xx")
def error_4xx():
    return render_template("noncontent/error_4XX.html")


@app.route("/error_5xx")
def error_5xx():
    return render_template("noncontent/error_5XX.html")


@app.route("/wip")
def wip():
    return render_template("noncontent/wip.html")


if __name__ == "__main__":
    app.run(port=5000)
