from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "Admin" and password == "12345":
        return redirect(url_for("success"))
    else:
        return redirect(url_for("fail"))
@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/fail")
def fail():
    return render_template("failure.html")


if __name__ == "__main__":
    app.run(debug=True)
