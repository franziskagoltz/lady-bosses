""" datamodel and functions for ladybosses """

from flask_sqlalchemy import SQLAlchemy

# connection to the PostgreSQL database
db = SQLAlchemy()


# ----- Model definitions ----- #
class Business(object):
    """businesses to be shown on ladybosses"""

    __tablename__ = "businesses"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150))


class Category(object):
    """categories of the businesses in the db"""

    __tablename__ = "categories"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.Integer, db.ForeignKey("businesses.business_id"),
                         nullable=False)

    businesses = db.relationship("Business", backref=db.backref("businesses"))
