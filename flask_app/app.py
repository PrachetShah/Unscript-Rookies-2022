from flask import Flask, render_template
from datetime import timedelta
from markupsafe import escape

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "password"

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)