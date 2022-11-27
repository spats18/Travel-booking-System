from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import *


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired(), Length(max=50)])
    contact = StringField('Contact', validators=[DataRequired(), Length(10)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class BookingForm(FlaskForm):
    h_name = StringField('Hotel', validators=[DataRequired(), Length(min=2, max=20)])
    cr_name = StringField('Car Rental', validators=[DataRequired(), Length(min=2, max=20)])
    b_start_date = DateField('From Date', validators=[DataRequired()], format="%Y-%m-%d")
    b_end_date = DateField('To Date', validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField('Book')
