from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-created_at', '-updated_at', '-orders', '-items')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    address = db.Column(db.String)
    img_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = db.relationship('Order', backref='user')
    items = association_proxy('orders', 'item')

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'<User {self.username}>'
    
class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    serialize_rules = ('-created_at', '-updated_at', '-orders', '-users')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    category = db.Column(db.String)
    img_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    orders = db.relationship('Order', backref='item')
    users = association_proxy('orders', 'user')

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    serialize_rules = ('-created_at', '-updated_at', '-items','-users')

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quantity = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

