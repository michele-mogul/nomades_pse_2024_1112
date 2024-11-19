import os
from flask import Flask, render_template, request

CURR_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__, template_folder="src")

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)