from sqlalchemy import Column, String

from app import db


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rgb = Column(String)
    color = Column(String)
