"""server file for ladybosses"""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session, g
from flask_cors import CORS, cross_origin

from Model import connect_to_db, Business

app = Flask(__name__)
CORS(app)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABCDE"


@app.route("/businesses.json")
def get_business_data():
    """return json object with business info"""

    # placeholder function without filters to get all businesses in db
    # so far only used for testing to get data from server to react frontend
    businesses = Business.query.all()

    return jsonify(Business.serialize_business_object(businesses))


if __name__ == "__main__":

    connect_to_db(app)

    app.run(host="0.0.0.0")
