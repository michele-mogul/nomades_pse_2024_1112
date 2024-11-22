# builtin libraries
import os
import csv
import hashlib

# installed libraries
from flask import Flask, render_template, request, session, redirect, url_for, flash
import firebase_admin
from firebase_admin import credentials, firestore

# custom libraries
from helpers.random_password_generator import generate_password
from helpers.decorators import authenticated

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

cred = credentials.Certificate(os.path.join(CURR_DIR, 'config', "firestore-creds.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__, template_folder="src")
app.config["SECRET_KEY"] = 'djkaoajkfsajkl'

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")

    if uid == "" or pwd == "":
      flash("Please enter valid credentials", "danger")
      return render_template('login/register.html')
    
    user_col_ref = db.collection(u'users')
    users = user_col_ref.stream()
    for user in users:
       user_data: dict = user.to_dict()
       if user_data.get("uid", "") == uid:
         flash(f'User with uid: {uid} already exists in db', "danger")
         return render_template('login/register.html')

    salt: str = generate_password(True, True, False, False, 10)
    h_pwd: str = hashlib.sha256((pwd+salt).encode(encoding='utf-8')).hexdigest() 
    user_col_ref.add({
      "uid": uid,
      "pwd": h_pwd,
      "salt": salt
    })

    session["loggedin"] = True
    return redirect(url_for("private"))
  
  return render_template('login/register.html')

@app.route("/signin", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    uid: str = request.form["tbx_uid"]
    pwd: str = request.form["tbx_pwd"]

    users = db.collection(u'users').stream()
    for user in users:
      user_data: dict = user.to_dict()
      if user_data.get("uid", "") == uid:
        h_pwd = hashlib.sha256((pwd+user_data.get("salt", "")).encode(encoding='utf-8')).hexdigest()
        if user_data.get("pwd", "") == h_pwd:
          session['loggedin'] = True
          flash('Login successful', "success")
          return redirect(url_for("private"))
    flash("Invalid credentials", "danger")

  return render_template("login/login.html")

@app.route("/logout")
def logout():
  # session["loggedin"] = False
  # del session["loggedin"]
  session.clear()
  flash("logout successful", "success")
  return redirect(url_for('login'))

@app.route("/private")
@authenticated
def private():
  return render_template("private/private.html")

@app.route("/private2")
@authenticated
def private2():
  return "I'm a private2 route"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)