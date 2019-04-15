from flask import Flask, render_template, request, flash, redirect, session, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os
import sqlite3
import random
import hashlib


UPLOAD_FOLDER = '/Users/alex.bruns/LahorenWebsite/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/login', methods=["GET", "POST"])
def do_admin_login():
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("""SELECT * FROM Admins""")
    admins = c.fetchall()
    conn.close()
    pairs = dict()
    for admin in admins:
        pairs[admin[0]] = admin[1]
    if request.method == "GET":
        return render_template("login.html")
    if request.form['username'] in pairs.keys() and request.form['password'] == pairs[request.form['username']]:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    if "url" in session:
        return redirect(session["url"])
    return redirect("/")


@app.route("/")
def root():
    session['url'] = url_for("root")
    return render_template("root.html")


@app.route("/downloads")
def downloads():
    session['url'] = url_for("downloads")
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("""SELECT * FROM Uploads""")
    fns = c.fetchall()
    conn.close()
    dls = []
    for fn in fns:
        dls.append({
            "link": "uploads/"+fn[0],
            "title": fn[0][67:]
        })
    return render_template(
        "downloads.html",
        dls=dls
    )


def allowed_file(filename):
    return '.' in filename \
           and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload():
    session['url'] = url_for("upload")
    if not session.get('logged_in'):
        return redirect("/login")
    if request.method == "GET":
        return render_template("upload.html")
    else:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            h = hashlib.sha256()
            h.update(str(random.getrandbits(100)).encode("utf-8"))
            filename = h.hexdigest() + "___" + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            conn = sqlite3.connect("db.sqlite3")
            c = conn.cursor()
            c.execute("""INSERT INTO Uploads VALUES (?)""", (filename,))
            conn.commit()
            conn.close()
            return "done"


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


@app.route("/static/assets/<filename>")
def assets(filename):
    return send_from_directory('static/assets', filename)


@app.route("/error_4xx")
def error_4xx():
    return render_template("noncontent/error_4XX.html")


@app.route("/error_5xx")
def error_5xx():
    return render_template("noncontent/error_5XX.html")


@app.route("/wip")
def wip():
    return render_template("noncontent/wip.html")


@app.route("/test")
def test():
    return "test"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(port=5000)
