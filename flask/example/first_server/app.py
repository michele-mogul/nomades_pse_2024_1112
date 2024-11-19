from flask import Flask, render_template, request

app = Flask(__name__, template_folder="src")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/home")
def home():
  return "Home"

@app.route("/my/private/home")
def home2():
  return "Home"

@app.route("/users")
def users():
  return "Some"

@app.route("/dyn/<name>/<int:age>/<cities>")
def dyn(name: str, age: int, cities: str):
  vars = {
    "age": age,
    "name": name
  }

  cities = cities.split(";")
  print(cities)
  return render_template("jinja_example/variables.html", vars=vars)

@app.route("/dyn2/<int:age>")
def dyn2(age: int):
  return "Major" if age > 17 else " Minor"

@app.route("/for")
def jinja_for():
  fruits = [
    "apple",
    "banana",
    "orange",
    "watermelon",
    "peach",
    "strawberry"
  ]

  return render_template("jinja_example/for.html", fruits=fruits)

@app.route("/if/<int:age>")
def iif(age: int):
  return render_template("jinja_example/if.html", age=age)

@app.route("/safe")
def jinja_safe():
  html = '<script>alert("Hacked!!!")</script>'
  return render_template("jinja_example/safe.html", html=html)

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")
    return f"{uid} -> {pwd}"

  return render_template("login/login.html")

@app.route('/form/files', methods=['GET', 'POST'])
def form_files():
  if request.method == 'POST': # request object has attribute method, which is a string informing the method used in the request
    file = request.files['fileInput']
    file.save(file.filename)
    return 'File uploaded successfully'
  return '''
    <form action="" method="POST" enctype="multipart/form-data">
      <input type="file" name="fileInput">
      <input type="submit" value="Envoyer">
    </form>
  '''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)