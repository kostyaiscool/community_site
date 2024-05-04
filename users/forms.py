from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.fields.datetime import DateTimeField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired(), Length(min=4, max=512)])
    email = EmailField('email', validators=[DataRequired(), Email()])


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = DateTimeField('age', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=4, max=512)])
    email = EmailField('email', validators=[DataRequired(), Email()])
