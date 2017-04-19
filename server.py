"""server file for ladybosses"""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session, g
from Model import connect_to_db

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABCDE"


@app.route("/businesses.json")
def get_business_data():
    """return json object with business info"""

    # data = {"data": "hello there this is the data"}

    return jsonify({"data": "hello there this is the data"})


if __name__ == "__main__":

    connect_to_db(app, "postgresql:///ladybosses")

    app.run(host="0.0.0.0")
