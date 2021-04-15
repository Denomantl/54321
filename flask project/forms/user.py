from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegisterForm(FlaskForm):
    email = StringField('Первый катет')
    password = StringField('Второй катет')
    submit = SubmitField('Посчитать')
