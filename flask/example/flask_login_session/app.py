import os
import csv
import hashlib

from flask import Flask, render_template, request, session, redirect, url_for, flash

from helpers.random_password_generator import generate_password

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__, template_folder="src")
app.config["SECRET_KEY"] = 'some secret'

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")

    if uid == "" or pwd == "":
      flash("Please enter a valid credentials", "danger")
      flash("The uid can't be empty", "warning")
      flash("The pwd can't be empty", "warning")
      return render_template('login/register.html')

    
    # TODO check if file exists and if user exisits in file
    if os.path.exists(CSV_FILE):
      with open(CSV_FILE, "r") as f:
        users = csv.DictReader(f)
        for user in users:
          if user["uid"] == uid:
            return "UID already in file"
    else:
      with open(CSV_FILE, "w") as f:
        f.write("uid,pwd,salt\n")    

    # TODO insert user in csv file
    with open(CSV_FILE, "a") as f:
      writer = csv.DictWriter(f, fieldnames=["uid", "pwd", "salt"])
      salt: str = generate_password(True, True, False, False, 10)
      h_pwd: str = hashlib.sha256((pwd+salt).encode(encoding='utf-8')).hexdigest()
      writer.writerow({"uid": uid, "pwd": h_pwd, "salt": salt})

    # TODO return the string 'user sucessfully registered'
    session["loggedin"] = True
    return "user sucessfully registered"
  
  return render_template('login/register.html')

@app.route("/signin", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    uid: str = request.form["tbx_uid"]
    pwd: str = request.form["tbx_pwd"]

    # TODO open csv file
    with open(CSV_FILE) as f:
      # TODO get the uid and password for the matching uid
      users = csv.DictReader(f)

      for user in users:
        if user["uid"] == uid:
          # TODO check if passwords match
          h_pwd = hashlib.sha256((pwd+user["salt"]).encode(encoding='utf-8')).hexdigest()
          if user["pwd"] == h_pwd:
            # TODO return "login successfull"
            session["loggedin"] = True
            return "login successfull"
      return "Invalid credentials"

  return render_template("login/login.html")

@app.route("/logout")
def logout():
  # session["loggedin"] = False
  # del session["loggedin"]
  session.clear()
  flash("logout successful", "success")
  return redirect(url_for('login'))

@app.route("/private")
def private():
  # if not ('loggedin' in session and session["loggedin"]):
  if not session.get('loggedin', False):
    return redirect(url_for('login'))
  
  return "I'm a private route"


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)