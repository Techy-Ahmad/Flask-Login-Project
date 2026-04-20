from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecretkey"
app.permanent_session_lifetime = timedelta(days=7)
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT UNIQUE,
                       password TEXT,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         )
             """)

    # insert admin only if not exists
    cursor.execute("SELECT * FROM users WHERE username = ?", ("Admin",))
    user = cursor.fetchone()

    if not user:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("Admin", generate_password_hash("12345"))
        )

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("login.html")

init_db()
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[0], password):

        session["user"] = username

        # remember me
        if request.form.get("remember"):
            session.permanent = True
        else:
            session.permanent = False

        flash("Login Successful 🎉", "success")
        return redirect(url_for("dashboard"))

    # ❗ ALWAYS return something here
    flash("Invalid Username or Password ❌", "error")
    return redirect(url_for("home"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # check if user already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Username already exists ❌")
            conn.close()
            return redirect(url_for("signup"))

        # insert new user
        hashed_password = generate_password_hash(password)

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        conn.close()

        flash("Account created successfully 🎉")
        return redirect(url_for("home"))

    return render_template("signup.html")
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "info")
    return redirect(url_for("home"))


@app.route("/failure")
def failure():
    return render_template("failure.html")

@app.route("/profile")
def profile():
    if "user" in session:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, username, created_at FROM users WHERE username=?", (session["user"],))
        user = cursor.fetchone()

        conn.close()

        return render_template("profile.html", user=user)

    return redirect(url_for("home"))

@app.route("/edit-profile", methods=["GET", "POST"])
def edit_profile():
    if "user" not in session:
        return redirect(url_for("home"))

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    if request.method == "POST":
        new_username = request.form["username"]

        try:
            cursor.execute(
                "UPDATE users SET username=? WHERE username=?",
                (new_username, session["user"])
            )
            conn.commit()

            # update session
            session["user"] = new_username
            flash("Profile updated successfully ✅", "success")

        except:
            flash("Username already exists ❌", "error")

        conn.close()
        return redirect(url_for("profile"))

    conn.close()
    return render_template("edit_profile.html", user=session["user"])

@app.route("/delete-account", methods=["GET", "POST"])
def delete_account():
    if "user" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        confirm_text = request.form.get("confirm")

        if confirm_text != "DELETE":
            flash("You must type DELETE to confirm ❌", "error")
            return redirect(url_for("profile"))

        username = session["user"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        conn.close()

        session.pop("user", None)

        flash("Account deleted successfully 🗑️", "info")
        return redirect(url_for("home"))

    return render_template("delete_account.html")

if __name__ == "__main__":
    app.run(debug=True)
