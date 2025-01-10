import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# ini yang sqlite3 nya (gak perlu? keanya)
# dbs=sqlite3.connect("new-books-collection.db.")
# cursor = dbs.cursor()

# ini yang sqlalchemynya
class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Autoincrement ID
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    # id: Mapped[int] = mapped_column(primary_key=True)
    # title: Mapped[str] = mapped_column(unique=True)
    # author: Mapped[str]
    # rating: Mapped[float]

with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Books(id=5, title="Harrys Potir", author="Johannes Karl", rating=9.2)
    db.session.add(new_book)  # Menambah objek ke session
    db.session.commit() 