from flask_sqlalchemy import SQLAlchemy
# SQLAlchemy is an Object-Relational Mapping (ORM) library. It provides a way to interact with relational databases using Python code instead of writing raw SQL queries.

db = SQLAlchemy()

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
