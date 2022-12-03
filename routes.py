from forms import *
from models import *
from flask import Flask, render_template, request, url_for, flash, redirect
# import postgresql
from main import db, app
from flask_login import login_user, current_user, logout_user, login_required
from flask_caching import Cache

cache = Cache(app)
# db.init_app(app=app)

#Change login required process
login_manager.login_view = "/home"
login_manager.login_message = "User needs to be logged in to view this page"
login_manager.login_message_category = "warning"

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@cache.cached(timeout=50)
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if request.form:
        customer_obj = customer.query.filter_by(c_email=form.email.data).first()
        print(customer_obj)
        if form.email.data and form.password.data:
            login_user(customer_obj)
            return redirect('/booking')
        elif customer_obj is None or (customer_obj.password != form.password.data):
            flash('Incorrect credentials.')
            return redirect('/login')
        else:
            login_user(customer_obj)
            return redirect(url_for('user1'))
    return render_template('login.html', title='Login', form=form)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/signup', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.form:
        obj = customer(c_name=form.name.data, c_email=form.email.data, c_password=form.confirm_password.data,
                       c_age=form.age.data, c_address=form.address.data, c_contact=form.contact.data)
        db.session.add(obj)
        db.session.commit()
        flash('Account created successfully!!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Register', form=form)


@app.route('/booking', methods=['GET', 'POST'])
@login_required
def booking():
    form = BookingForm()
    if request.form:
        user = current_user
        h_obj = hotel.query.filter_by(h_name=form.h_name.data).first()
        cr_obj = car_rental.query.filter_by(cr_name=form.cr_name.data).first()
        days = (form.b_end_date.data - form.b_start_date.data).days
        amount = (h_obj.h_charges_per_night * days) + (cr_obj.cr_charges_per_day * days)
        obj = bookings(h_id=h_obj.h_id, cr_id=cr_obj.cr_id, b_start_date=form.b_start_date.data,b_end_date=form.b_end_date.data, b_amount_paid=amount)
        db.session.add(obj)
        db.session.commit()
        obj2 = booked_trips(c_id=user.c_id, b_id=obj.b_id)
        db.session.add(obj2)
        db.session.commit()
        flash('Trip booked!!!', 'success')
        return redirect(url_for('home'))
    return render_template('bookings.html', title='Trip', form=form)

@app.route("/logout")
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))


@app.route("/currentbookings")
@login_required
def currentbookings():
    user = current_user
    table1 = db.session.query(customer.c_name, customer.c_email,
                              hotel.h_name, bookings.b_amount_paid).select_from(customer).join(booked_trips
                                                                                               ).join(bookings).join(hotel). \
        filter(
        customer.c_id == booked_trips.c_id
    ).filter(
        booked_trips.b_id == bookings.b_id
    ).filter(
        bookings.h_id == hotel.h_id
    ).filter(
        customer.c_name == user.c_name).all()

    return render_template('currentbookings.html', table1=table1)
