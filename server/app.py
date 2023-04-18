#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import *
from models import User, Item, Order

# Views go here!
class Signup(Resource):

    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        address = request_json.get('address')
        img_url = request_json.get('img_url')

        user = User(
            username=username,
            address=address,
            img_url=img_url
        )

        user.password_hash = password

        try:
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return make_response(user.to_dict(), 201)
        except IntegrityError:
            return make_response({"error":"422 Unprocessable Entity"}, 422)
        
api.add_resource(Signup, '/signup')

class CheckSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            return make_response(user.to_dict(), 200)
        except:
            return make_response({"error": "Unauthorized"}, 401)
        
api.add_resource(CheckSession, '/check_session')

class Login(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        user = User.query.filter(User.username == username).first()
        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
        return make_response({"error": "401 Unauthroized"},401)
    
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return make_response({"message": "Logout Sucessful"}, 204)
        return make_response({"error": "401 Unauthorized"}, 401)

api.add_resource(Logout, '/logout')

class Items(Resource):

    def get(self):
        items = [item.to_dict() for item in Item.query.all()]
        return make_response(items, 200)
api.add_resource(Items, '/items')

class Users(Resource):

    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)
api.add_resource(Users, '/users')

class OrderById(Resource):
    def get(self, order_id):
        order = Order.query.get_or_404(order_id)
        return make_response(order.to_dict(), 200)

    def post(self, order_id):
        order = Order.query.get(order_id)
        if order is None:
            order = Order(id=order_id)
            db.session.add(order)
            db.session.commit()
        return make_response(order.to_dict(), 201)

    def patch(self, order_id):
        order = Order.query.get_or_404(order_id)
        data = request.get_json()
        if data.get('user_id'):
            order.user_id = data['user_id']
        if data.get('item_id'):
            order.item_id = data['item_id']
        db.session.commit()
        return make_response(order.to_dict(), 200)

    def delete(self, order_id):
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return make_response('', 204)

class Orders(Resource):
    def get(self):
        orders = [order.to_dict() for order in Order.query.all()]
        return make_response(orders, 200)

api.add_resource(OrderById, '/orders/<int:order_id>')
api.add_resource(Orders, '/orders')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
