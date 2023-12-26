from flask import Flask
from flask_restful import Api
from routes import Register, Login
from model import db

app = Flask(__name__)
api = Api(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def welcome():
    return 'Welcome to Home'

# Add resources for routes
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(port=4500)
