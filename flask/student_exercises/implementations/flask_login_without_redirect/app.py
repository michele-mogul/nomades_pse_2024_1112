import csv
import hashlib
import os

from flask import Flask, render_template, request

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__, template_folder="src")


def ensure_csv_file_exists():
    """Ensures the CSV file exists with a header row."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["uid", "pwd", "salt"])
            writer.writeheader()


def read_users():
    """Reads users from the CSV file and returns a list of dictionaries."""
    ensure_csv_file_exists()
    with open(CSV_FILE, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def write_user(uid, pwd, salt):
    """Writes a new user to the CSV file."""
    ensure_csv_file_exists()
    with open(CSV_FILE, "a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["uid", "pwd", "salt"])
        writer.writerow({"uid": uid, "pwd": pwd, "salt": salt})

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
        if any(user["uid"] == uid_ and user["pwd"] == hash_pwd(pwd_ + user['salt']) for user in read_users()):
            return "Login Success"
        return "Invalid input", 400
    return "Invalid input", 400

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("login/register.html")
    uid_ = request.form.get("tbx_uid")
    pwd_ = request.form.get("tbx_pwd")
    if uid_ and pwd_:
        if any(user["uid"] == uid_ for user in read_users()):
            return "Invalid input", 400

        salt = os.urandom(32).hex()
        write_user(uid_, hash_pwd(pwd_ + salt), salt)
        return "Registration successful"
    return "Invalid input", 400


def hash_pwd(pwd_):
    return hashlib.sha256(pwd_.encode(encoding='utf-8')).hexdigest()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
