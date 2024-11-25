import os
from functools import wraps

from flask import Flask, render_template, request, session, redirect, flash

from helpers.db_wrapper import read_users, write_user, user_exists, delete_user
from helpers.password import hash_pwd

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__, template_folder="src")
app.config["SECRET_KEY"] = "secret"


def persist_login(uid_):
    session["current_user"] = uid_
    session['logged_in'] = True


def authenticated(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        if not session.get('logged_in', False):
            return redirect("/")
        return func(*args, **kwargs)

    return inner_func


@app.route("/")
def index():
    return render_template("index.html", current_user=session.get('current_user', None),
                           logged_in=session.get('logged_in', False))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login/login.html", current_user=session.get('current_user', None),
                               logged_in=session.get('logged_in', False))
    uid_ = request.form.get("tbx_uid")
    pwd_ = request.form.get("tbx_pwd")
    if uid_ and pwd_:
        if any(user["uid"] == uid_ and user["pwd"] == hash_pwd(pwd_ + user['salt']) for user in read_users()):
            persist_login(uid_)
            flash("Success", "success")
            return redirect('/private')
        flash("Invalid user or password", "warning")
        return redirect('/login')
    flash("Invalid input", "warning")
    return redirect('/login')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("login/register.html", current_user=session.get('current_user', None),
                               logged_in=session.get('logged_in', False))
    uid_ = request.form.get("tbx_uid")
    pwd_ = request.form.get("tbx_pwd")
    if uid_ and pwd_:
        if user_exists(uid_):
            flash("User already exists", "warning")
            return redirect("/register")

        salt = os.urandom(32).hex()
        write_user(uid_, hash_pwd(pwd_ + salt), salt)
        persist_login(uid_)
        flash("Success", "success")
        return redirect('/private')
    flash("Invalid Input", "warning")
    return redirect("/register")


@app.route("/logout", methods=["GET"])
@authenticated
def logout():
    session.clear()
    flash("You have been logged out", "success")
    return redirect("/")


@app.route("/private")
@authenticated
def private():
    return render_template('private/index.html', current_user=session.get('current_user', None))


@app.route("/delete")
@authenticated
def delete():
    delete_user(session.get('current_user'))
    return logout()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
