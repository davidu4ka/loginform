from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import input_required, EqualTo,Email,DataRequired
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email",validators=[input_required(),Email()])
    password = PasswordField("Password",validators=[input_required()])
    confirm_pass = PasswordField("Confirm Password", validators = [input_required(),EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()