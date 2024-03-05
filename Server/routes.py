from flask import request
from flask_restful import Resource
from model import db, UserModel

class Register(Resource):
    def post(self):
        user_detail = request.json
        try:
            new_user = UserModel(**user_detail)
            db.session.add(new_user)
            db.session.commit()
            return {"msg": "User Registered"}, 201
        except Exception as e:
            return {"msg": "Something went wrong", "error": str(e)}, 500

class Login(Resource):
    def post(self):
        credentials = request.json
        try:
            user = UserModel.query.filter_by(email=credentials['email'], password=credentials['password']).first()
            if user:
                return {"msg": "Login Successful"}, 201
            return {"msg": "Wrong Credentials"}, 401
        except Exception as e:
            return {"msg": "Something went wrong", "error": str(e)}, 500

# flask_restful simplifies the development of RESTful APIs