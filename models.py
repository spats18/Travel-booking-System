# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from flask_login import UserMixin
from main import  login_manager
from main import db
from datetime import date

@login_manager.user_loader
def load_user(c_id):
    return customer.query.get(int(c_id))
 
class customer(db.Model,UserMixin):
    _tablename_ = 'customer'
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(50), nullable = False)
    c_email = db.Column(db.String(100),  unique= True, nullable = False)
    c_password = db.Column(db.String(255), nullable = False)
    c_age = db.Column(db.Integer, nullable = False)
    c_address = db.Column(db.String(255))
    c_contact = db.Column(db.String(255))
    CheckConstraint("c_age>0", name = "ageCheck")
    def __init__(self, c_name, c_email, c_password, c_age, c_address=None, c_contact=None):
        self.c_name = c_name
        self.c_email = c_email
        self.c_password = c_password
        self.c_age = c_age
        self.c_address = c_address
        self.c_contact = c_contact
    
    def get_id(self):
        return (self.c_id)
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return True
    def is_active(self):
        return True


class hotel(db.Model,UserMixin):
    _tablename_ = 'hotel'
    h_id = db.Column(db.Integer, primary_key=True)
    h_name = db.Column(db.String(50), nullable = False)
    h_address = db.Column(db.String(255), unique= True, nullable = False)
    h_city = db.Column(db.String(255), nullable = False)
    h_email = db.Column(db.String(255),  unique= True, nullable = False)
    h_contact = db.Column(db.String(255))
    h_charges_per_night = db.Column(db.Float(25), nullable = False)
    h_rating = db.Column(db.Float(25))

    def __init__(self, h_name, h_address, h_city, h_email, h_charges_per_night, h_contact=None,h_rating=None):
        self.h_name = h_name
        self.h_address = h_address
        self.h_city = h_city
        self.h_email = h_email
        self.h_contact = h_contact
        self.h_charges_per_night = h_charges_per_night
        self.h_rating = h_rating

class car_rental(db.Model,UserMixin):
    _tablename_ = 'car_rental'
    cr_id = db.Column(db.Integer, primary_key=True)
    cr_name = db.Column(db.String(50), nullable = False)
    cr_address = db.Column(db.String(100), unique= True, nullable = False)
    cr_city = db.Column(db.String(255), nullable = False)
    cr_email = db.Column(db.String(255),  unique= True, nullable = False)
    cr_contact = db.Column(db.String(255))
    cr_charges_per_day = db.Column(db.Float(25))
    cr_rating = db.Column(db.Float(25))

    def __init__(self, cr_name, cr_address, cr_city, cr_email, cr_charges_per_day=None, cr_contact=None,cr_rating=None):
        self.cr_name = cr_name
        self.cr_address = cr_address
        self.cr_city = cr_city
        self.cr_email = cr_email
        self.cr_contact = cr_contact
        self.cr_charges_per_day = cr_charges_per_day
        self.cr_rating = cr_rating

class bookings(db.Model):
    _tablename_ = 'bookings'
    b_id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, db.ForeignKey('hotel.h_id'), nullable = False)
    cr_id = db.Column(db.Integer, db.ForeignKey('car_rental.cr_id'))
    b_start_date = db.Column(db.DateTime, nullable = False)
    b_end_date = db.Column(db.DateTime, nullable = False)
    b_booking_date = db.Column(db.DateTime, nullable = False)
    b_amount_paid = db.Column(db.Float(25))
    b_tour_package = db.Column(db.String(255))
    CheckConstraint("b_end_date > b_start_date", name = "dateCheck")

    def __init__(self, h_id, cr_id, b_start_date, b_end_date, b_booking_date=date.today().strftime("%Y-%m-%d"), b_amount_paid=None, b_tour_package=None):
        self.h_id = h_id
        self.cr_id = cr_id
        self.b_start_date = b_start_date
        self.b_end_date = b_end_date
        self.b_booking_date = b_booking_date
        self.b_amount_paid = b_amount_paid
        self.b_tour_package = b_tour_package

class booked_trips(db.Model):
    _tablename_ = 'booked_trips'
    b_id = db.Column(db.Integer, db.ForeignKey('bookings.b_id'), primary_key = True)
    c_id = db.Column(db.Integer, db.ForeignKey('customer.c_id'), primary_key = True)
    bookings = db.relationship("bookings")
    customer = db.relationship("customer")

    def __init__(self, b_id, c_id):
        self.b_id = b_id
        self.c_id = c_id
   
class tours(db.Model):
    _tablename_ = 'tours'
    h_id = db.Column(db.Integer, db.ForeignKey('hotel.h_id'), primary_key = True, unique= True, nullable = False)
    cr_id = db.Column(db.Integer, db.ForeignKey('car_rental.cr_id'), primary_key = True, unique= True, nullable = False)
    t_days  = db.Column(db.Integer)
    t_nights  = db.Column(db.Integer)
    t_original_price = db.Column(db.Float(25))
    t_discount_percent = db.Column(db.Float(25))
    t_city = db.Column(db.String(255), nullable = False)
    t_package_name = db.Column(db.String(255), nullable = False)
    hotels = db.relationship("hotel")
    carRental = db.relationship("car_rental")

    def __init__(self, h_id, cr_id, t_days, t_nights, t_original_price, t_discount_percent, t_city, t_package_name):
        self.h_id = h_id
        self.cr_id = cr_id
        self.t_days = t_days
        self.t_nights = t_nights
        self.t_original_price = t_original_price
        self.t_discount_percent = t_discount_percent
        self.t_city = t_city
        self.t_package_name = t_package_name
       
        