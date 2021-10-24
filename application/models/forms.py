"""Form object declaration."""
from flask_wtf import FlaskForm
from flask_wtf.recaptcha.fields import RecaptchaField
from wtforms import StringField, TextField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    """ Sign up for a user account """
    email = StringField(
        'Email',
        [
            DataRequired(message="Please enter a valid email address."),
            Email(message='Not a valid email address.')
        ]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired(message="Please enter a password."),
            Length(min=8,
                   message=('Minimum 8 Characters'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """ Register form """
    name = StringField(
        'Name',
        [
            DataRequired(message="Please enter your name."),
            Length(min=3,
                   message=('Your name is too short.'))
        ]
    )
    email = StringField(
        'Email',
        [
            DataRequired(message="Please enter a valid email address."),
            Email(message='Not a valid email address.')
        ]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired(message="Please enter a password."),
            Length(min=8,
                   message=('Minimum 8 Characters'))
        ]
    )
    confirmPassword = PasswordField(
        'Repeat Password',
        [
            DataRequired(message="Please enter the same password."),
            EqualTo('password',
                    message=('Passwords must match.'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    """ Contact form """
    name = StringField(
        'Name',
        [
            DataRequired(message="Please enter your name."),
            Length(min=3,
                   message=('Your name is too short.'))
        ]
    )
    email = StringField(
        'Email',
        [
            DataRequired(message="Please enter a valid email address."),
            Email(message='Not a valid email address.')
        ]
    )
    body = TextField(
        'Message',
        [
            DataRequired(message="Please type yur message."),
            Length(min=4,
                   message=('Your message is too short.'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')
