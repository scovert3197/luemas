from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    firstName = StringField('First name', validators=[DataRequired("Please enter your first name")])
    lastName = StringField('Last name', validators=[DataRequired("Incorrect last name")])
    email = StringField('Email', validators=[DataRequired("Email in wrong format"), Email("Please enter your email address")])
    password = PasswordField('Password', validators=[DataRequired("Somethings wrong with your password"), Length(min=6, message="Password must be greater than 6 characters")])
    submit = SubmitField('Submit')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter email to sign in"), Email("Please enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign In")