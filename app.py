import os
from flask import Flask, render_template, request, flash, get_flashed_messages
from flask_session import Session
from helpers import SHOP_ITEMS


# Configure application
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Define global variables
app.jinja_env.globals["SHOP_ITEMS"] = SHOP_ITEMS


@app.route("/")
def index():
    return render_template("index.html")
 

if __name__ == "__main__":
    app.run(debug=True)
