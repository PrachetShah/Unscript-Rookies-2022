from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import timedelta
from markupsafe import escape

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "password"

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form["transaction_id"] == "":
            flash(" Please enter a name ", "info")
            return render_template("home.html")
        username = request.form["transaction_id"]
        print("aaaaa")
        return redirect(url_for("home"))
    else:
        return render_template("home.html")
if __name__ == "__main__":
    app.run(debug = True)