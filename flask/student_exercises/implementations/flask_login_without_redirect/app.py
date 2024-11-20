import csv
import os

from flask import Flask, render_template, request

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__, template_folder="src")


def read_users():
    """Reads users from the CSV file and returns a list of rows."""
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, "r") as csv_file:
        return list(csv.reader(csv_file, delimiter=","))


def write_user(uid, pwd):
    """Writes a new user to the CSV file."""
    with open(CSV_FILE, "a", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow([uid, pwd])

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login/login.html")
    uid_ = request.form.get("tbx_uid")
    pwd_ = request.form.get("tbx_pwd")
    if uid_ and pwd_:
        users = read_users()
        if any(row and row[0] == uid_ and row[1] == pwd_ for row in users):
            return "Login Success"
        return "Error, User does not exist"
    return "Invalid input", 400


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("login/register.html")
    uid_ = request.form.get("tbx_uid")
    pwd_ = request.form.get("tbx_pwd")
    if uid_ and pwd_:
        users = read_users()
        if any(row and row[0] == uid_ for row in users):
            return "Error, User already exists"
        write_user(uid_, pwd_)
        return "Registration successful"
    return "Invalid input", 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
