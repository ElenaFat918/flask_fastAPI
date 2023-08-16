"""
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля
"Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""

from flask import Flask, redirect, render_template, request, url_for, make_response

from models import db, User
from forms import RegisterForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = b'ea678bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'

csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


# @app.route('/', methods=['GET', 'POST'])
# def set_cookie():
#     if request.method == 'POST':
#         context = {
#             'name': request.form.get('name'),
#             'email': request.form.get('email')
#         }
#         response = redirect(url_for('main', name=context['name']))
#         response.headers['new_head'] = 'New value'
#         response.set_cookie('name', context['name'])
#         response.set_cookie('email', context['email'])
#         return response
#     context = {'title': ' cookies'}
#     return render_template('form.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data

        # получить user из БД по name и email
        # можно через filter-by (только AND ???? )
        existing_user = User.query.filter(
            (User.name == name) | (User.surname == surname) | (User.email == email)).first()

        # если user существует
        if existing_user:
            error_msg = 'Username or email already exists.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Registered success!'
    return render_template('register.html', form=form)


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name, email = request.cookies.get('name'), request.cookies.get('email')
    return f"Значение cookie: {name, email}"


@app.route('/logout/')
def logout():
    context = {'title': 'cookies'}
    response = make_response(render_template('form.html', **context))
    response.set_cookie(*request.cookies, expires=0)
    # return response
    return redirect(url_for('set_cookie'))


@app.route('/')
def main():
    context = {'title': 'Основная'}
    return render_template('main.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    clothes_items = [
        {
            'text': 'Блуза DORIZORI, повседневный стиль, короткий рукав, полупрозрачная, однотонная, размер One Size, бежевый',
            'image': 'dorizori.jpg'
        },
        {
            'text': 'Брюки Dilvin демисезонные, прямой силуэт, классический стиль, карманы, стрелки, размер 40 (46RU), мультиколор',
            'image': 'dilvin.jpg'
        },
        {
            'text': 'Юбка-карандаш RAPOSA, миди, карманы, размер 42, серый',
            'image': 'raposa.jpg'
        },
    ]
    return render_template('clothes.html', **context, clothes=clothes_items)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    shoes_items = [
        {
            'text': 'Босоножки Эконика, натуральная кожа, размер 39, зеленый',
            'image': 'ekonika.jpg'
        },
        {
            'text': 'Босоножки Tamaris, натуральная кожа, размер 38, черный',
            'image': 'tamaris.jpg'
        },
        {
            'text': 'Кеды s.Oliver, летние, повседневные, размер 38, белый',
            'image': 's_oliver.jpg'
        },
    ]
    return render_template('shoes.html', **context, shoes=shoes_items)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    jacket_items = [
        {
            'text': 'Ветровка Marc O Polo демисезонная, удлиненная, несъемный капюшон, карманы, размер 40, зеленый',
            'image': 'marc_o_polo.jpg'
        },
        {
            'text': 'Куртка Helly Hansen, удлиненная, несъемный капюшон, карманы, водонепроницаемая, размер XS, голубой',
            'image': 'helly_hansen.jpg'
        },
        {
            'text': 'Ветровка FLY демисезонная, укороченная, силуэт свободный, пояс/ремень, карманы, подкладка, размер 48, зеленый',
            'image': 'fly.jpg'
        },
    ]
    return render_template('jackets.html', **context, jackets=jacket_items)


if __name__ == "__main__":
    app.run(debug=True)
