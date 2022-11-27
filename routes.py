from forms import *
from models import *
from flask import Flask, render_template, request, url_for, flash, redirect
#import postgresql
from main import db, app

from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()

    if request.form:
        customer_obj = customer.query.filter_by(
            c_email=form.email.data).first()
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
    print('Madame')
    return render_template('about.html')

# from models import Customer, Trips, Offers


@app.route('/signup', methods=["GET", "POST"])
def register():
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
def booking():
    form = BookingForm()
    if request.form:
        user = current_user
        h_obj = hotel.query.filter_by(h_name=form.h_name.data).first()
        cr_obj = car_rental.query.filter_by(cr_name=form.cr_name.data).first()
        days = (form.b_end_date.data - form.b_start_date.data).days
        amount = (h_obj.h_charges_per_night * days) + \
            (cr_obj.cr_charges_per_day * days)
        obj = bookings(h_id=h_obj.h_id, cr_id=cr_obj.cr_id, b_start_date=form.b_start_date.data,
                       b_end_date=form.b_end_date.data, b_amount_paid=amount)
        db.session.add(obj)
        db.session.commit()
        obj2 = booked_trips(c_id=user.c_id, b_id=obj.b_id)
        db.session.add(obj2)
        db.session.commit()
        flash('Trip booked!!!', 'success')
        return redirect(url_for('home'))
    return render_template('bookings.html', title='Trip', form=form)

# from tables import CustomerTable, TripsTable, OffersTable, PackagesTable
# @app.route('/templates/items', methods = ['GET','POST'])
# @login_required
# def display():
#     items = []
#     items = Customer.query.all()
#     table1 = CustomerTable(items)
#     items2 = []
#     items2 = Trips.query.all()
#     table2 = TripsTable(items2)
#     items3 = []
#     items3 = Offers.query.all()
#     table3 = OffersTable(items3)
#     items4 = []
#     items4 = Packages.query.all()
#     table4 = PackagesTable(items4)
#     table1.border = True
#     table2.border = True
#     table3.border = True
#     table4.border = True
#     return render_template('items.html', table1 = table1, table2 = table2, table3 = table3, table4 = table4)


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


# @app.route('/edit_cust/<int:id>', methods = ['GET','POST'])
# @login_required
# def edit1(id):
#     c1 = Customer.query.get_or_404(id)
#     form = Cust_editForm()

#     if request.form:
#         c1.name = form.name.data
#         c1.contact = form.contact.data
#         c1.address = form.address.data
#         c1.email = form.email.data
#         db.session.commit()
#         flash('You have successfully edited the data.','success')
#         return redirect(url_for('display'))
#     form.name.data = c1.name
#     form.contact.data = c1.contact
#     form.address.data = c1.address
#     form.email.data = c1.email
#     return render_template('edit1.html', action =  "Edit", title = 'Edit Offer', form = form)

# @app.route('/user', methods = ['GET', 'POST'])
# @login_required
# def user1():
#     return render_template('user.html')

# @app.route('/contactus', methods = ['GET', 'POST'])
# @login_required
# def contact():
#     return render_template('contact.html')
