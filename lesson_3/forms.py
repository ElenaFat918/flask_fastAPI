from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


"""
определен классLoginForm,который наследуется от FlaskForm. 
Внутри класса определены два поля:username и password.
Поле username является строковым полем,а поле password—полем для ввода пароля.
Оба поля обязательны для заполнения,так как им передан валидатор DataRequired.
"""


class RegisterForm(FlaskForm):
    ame = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    ])


"""
определен класс RegisterForm,который наследуется от FlaskForm.
Внутри класса определены три поля:name,age и gender.
Поле name является строковым полем,поле age—числовым,а поле gender—выпадающим списком.
В списке выбора есть две опции:male и female.
"""


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    conﬁrm_password = PasswordField('ConﬁrmPassword', validators=[DataRequired(), EqualTo('password')])


"""
определен класс RegistrationForm,который наследуется от FlaskForm.
Внутри класса определены три поля: email, password и conﬁrm_password. 
Поле email проверяется на наличие данных и на соответствие формату email.
Поле password проверяется на наличие данных и на минимальную длину (6символов). 
Поле conﬁrm_password проверяется на наличие данных и на соответствие значению поля password.
"""
