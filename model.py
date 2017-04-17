""" datamodel and functions for ladybosses """

from flask_sqlalchemy import SQLAlchemy

# connection to the PostgreSQL database
db = SQLAlchemy()


# ----------- Model definitions ----------- #
class Business(db.Model):
    """businesses to be shown on ladybosses"""

    __tablename__ = "businesses"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150))


class Category(db.Model):
    """categories of the businesses in the db"""

    __tablename__ = "categories"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.Integer, db.ForeignKey("businesses.business_id"),
                         nullable=False)

    businesses = db.relationship("Business", backref=db.backref("businesses"))


# ----------- Helper Functions ----------- #
def connect_to_db(app, db_uri='postgresql:///ladybosses'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # only runs when we run file directly, so we are assuming we want to
    # create tables

    from server import app
    connect_to_db(app)
    print "Connected to DB."
    db.create_all()
    print "tables created"
