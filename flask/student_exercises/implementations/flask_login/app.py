import os
import csv
import hashlib

# TODO import session, redirect, url_for
from flask import Flask, render_template, request

from helpers.random_password_generator import generate_password

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__, template_folder="src")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")

    if uid == "" or pwd == "":
      # TODO: use flashed messages instead of returns
      return "Please enter a valid credentials"
    
    if os.path.exists(CSV_FILE):
      with open(CSV_FILE, "r") as f:
        users = csv.DictReader(f)
        for user in users:
          if user["uid"] == uid:
           # TODO: use flashed messages instead of returns 
            return "UID already in file"
    else:
      with open(CSV_FILE, "w") as f:
        f.write("uid,pwd,salt\n")    

    with open(CSV_FILE, "a") as f:
      writer = csv.DictWriter(f, fieldnames=["uid", "pwd", "salt"])
      salt: str = generate_password(True, True, False, False, 10)
      h_pwd: str = hashlib.sha256((pwd+salt).encode(encoding='utf-8')).hexdigest()
      writer.writerow({"uid": uid, "pwd": h_pwd, "salt": salt})
# TODO: use flashed messages instead of returns
    return "user sucessfully registered"
  
  return render_template('login/register.html')

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    uid: str = request.form["tbx_uid"]
    pwd: str = request.form["tbx_pwd"]

    with open(CSV_FILE) as f:
      users = csv.DictReader(f)

      for user in users:
        if user["uid"] == uid:
          h_pwd = hashlib.sha256((pwd+user["salt"]).encode(encoding='utf-8')).hexdigest()
          if user["pwd"] == h_pwd:
            # TODO: use flashed messages instead of returns
            return "login successfull"
      return "Invalid credentials"

  return render_template("login/login.html")

# TODO: create the logout route
# TODO: create a new private route accessible only when logged in (use session to store the information for the login)
# TODO: Create a decorator to check if the user is logged in or not (first use the if statement and change it afterwards by the decorator)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)