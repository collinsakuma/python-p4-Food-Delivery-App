#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Item, Order

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Deleting records...")
        Item.query.delete()
        User.query.delete()

        print("Creating Items...")

        item_1 = Item(
            name = "Mac n Cheese",
            price = 10,
            category = "pasta",
            img_url = "someimage"
        )

        item_2 = Item(
            name= 'Hamburger',
            price = 8,
            category = 'American',
            img_url = 'aburger'
            
        )

        item_3 = Item(
            name= 'Pizza',
            price = 7,
            category = 'American',
            img_url = 'apizza'
        )

        item_4 = Item(
            name = 'Gnocchi',
            price = 12,
            category = 'pasta',
            img_url = 'agnocchi'
        )

        item_5 = Item(
            name = 'French Fries',
            price = 4,
            category = 'American',
            img_url = 'afry'
        )
        
        user_1 = User(
            username="Collin",
            
            address="1600 Pen Ave",
            img_url="an image"
        )
        user_1.password_hash = user_1.username + 'password'

        user_2 = User(
            username= 'Clayton97',
            
            address='12 Main Str',
            img_url = 'another image'
        )
        user_2.password_hash = user_2.username + 'password'

        

        # Seed code goes here!
        db.session.add_all([item_1, item_2, item_3, item_4, item_5, user_1, user_2])
        db.session.commit()

        print("db seeded")
