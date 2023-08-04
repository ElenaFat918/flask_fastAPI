"""
Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
 где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти»,
при нажатии на которую будет удалён cookie-файл с данными пользователя
 и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, flash, redirect, render_template, request, url_for, make_response, session

app = Flask(__name__)

app.secret_key = b'9e781908096ff64567389de11d8e54fce4e6a42f3f89532f35125fa78f7079a7'


@app.route('/', methods=['GET', 'POST'])
def set_cookie():
    if request.method == 'POST':
        context = {
            'name': request.form.get('name'),
            'email': request.form.get('email')
        }
        response = redirect(url_for('main', name=context['name']))
        response.headers['new_head'] = 'New value'
        response.set_cookie('name', context['name'])
        response.set_cookie('email', context['email'])
        return response
    context = {'title': ' cookies'}
    return render_template('form.html', **context)


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


@app.route('/main')
def main():
    context = {'title': 'Главная'}

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
