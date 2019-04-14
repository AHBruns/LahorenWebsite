from flask import Flask
import sqlite3


app = Flask(__name__)


@app.route("/")
def root():
    return "server is live"


if __name__ == "__main__":
    app.run(port=5000)
