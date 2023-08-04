"""


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Меню</title>
</head>
<body>

<div>
    <a href="{{ url_for('hello1') }}">
      <button type="submit">
          Привет
      </button>
    </a>
</div>

</body>
</html>


app = Flask(__name__, static_folder='static')


Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Меню</title>
</head>
<body>

<div>
    <a href="{{ url_for('hello1') }}">
      <button type="submit">
          Привет
      </button>
    </a>

    <a href="{{ url_for('uploads') }}">
      <button type="submit">
          Изображение
      </button>
    </a>
</div>

</body>
</html>

20:42
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Загруженный файл</title>
</head>
<body>
    <div class="image">
        <img src="static/img/{{ file_name }}" alt="Ваше загруженное изображение" height=300px>
    </div>
</body>
</html>

20:42
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Форма для загрузки файла</title>
</head>
<body>
<h1>Загружаем новый файл на сервер</h1>
<form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Загрузить>
</form>
</body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Меню</title>
</head>
<body>

<div>
    <a href="{{ url_for('hello1') }}">
      <button type="submit">
          Привет
      </button>
    </a>

    <a href="{{ url_for('uploads') }}">
      <button type="submit">
          Изображение
      </button>
    </a>

    <a href="{{ url_for('login') }}">
      <button type="submit">
          Вход
      </button>
    </a>
</div>

</body>
</html>


"""
from glob import escape
from urllib import request

from flask import render_template, Flask

app = Flask(__name__)
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in users.items():
            return 'Вы вошли'
        return f'Неправильный {escape(username)} логин или пароль'
    return render_template('task3.html')

"""Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Меню</title>
</head>
<body>

<div>
    <a href="{{ url_for('hello1') }}">
      <button type="submit">
          Привет
      </button>
    </a>

    <a href="{{ url_for('uploads') }}">
      <button type="submit">
          Изображение
      </button>
    </a>

    <a href="{{ url_for('login') }}">
      <button type="submit">
          Вход
      </button>
    </a>

    <a href="{{ url_for('count') }}">
      <button type="submit">
          Кол-во слов
      </button>
    </a>
</div>

</body>
</html>

21:09
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Подсчет слов</title>
</head>
<body>
    <div>
    <form method=post>
    <textarea name="text" placeholder="Введите текст" rows="5" cols="30"></textarea>
    <input type="submit" value="Отправить">
</form>
</div>
</body>
</html>


"""


@app.route('/count/', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        text = request.form.get('text')
        count = len(text.split())
        return f"Количество слов: {count}"
    return render_template('task4.html')

"""
Задание №5 📌 Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение или деление) и кнопка "Вычислить" 📌 При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Калькулятор</title>
</head>
<body>
    <div>
    <form method=post>
    <input type="number" name='number1'>
    <input type="number" name='number2'>
    <select id="operation" name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
    <input type="submit" value="Вычислить">
</form>
</div>
</body>
</html>
"""
@app.route('/culc/', methods=['GET', 'POST'])
def culc():
    if request.method == 'POST':
        number1 = int(request.form.get('number1'))
        number2 = int(request.form.get('number2'))
        operation = request.form.get('operation')
        if operation == 'add':
            return f"{number1 + number2}"
        elif operation == 'subtract':
            return f"{number1 - number2}"
        elif operation == 'multiply':
            return f"{number1 * number2}"
        elif operation == 'divide':
            return f"{number1 / number2}"
    return render_template('task5.html')
"""
Задание №6 📌 Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить" 📌 При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Возраст</title>
</head>
<body>
    <div>
        <form method=post>
            <input type="text" name='username'>
            <input type="number" name='age'>
            <input type="submit" value="Отправить">
        </form>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ошибка</title>
</head>
<body>
Доступ заперещен
</body>
</html>"""
@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        username = request.form.get('username')
        age = int(request.form.get('age'))
        if age < 18:
            return abort(403)
        return f"{username}, {age} возраст прошел"
    return render_template('task6.html')

@app.errorhandler(403)
def age_age_not(e):
    print(e)
    return render_template('403.html'), 403
"""
Задание №7 📌 Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить" 📌 При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное число и его квадрат.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Квадрат числа</title>
</head>
<body>
    <div>
        <form method=post>
            <input type="number" name='number'>
            <input type="submit" value="Отправить">
        </form>
    </div>
</body>
</html>
"""
@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        result = number**2
        return redirect(url_for('square_result', result=result))
    return render_template('task7.html')

@app.route('/square_result/')
def square_result():
    return request.args.get('result')
"""Задание №8 📌 Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить" 📌 При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет выведено "Привет, {имя}!".
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">

22:06
https://getbootstrap.com/

22:06

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
    <title>Flash</title>
</head>
<body>
<form action="/form" method="post">
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
    {% for category, message in messages %}
    <div class="alert alert-{{ category }}">
        {{ message }}
    </div>
    {% endfor %}
    {% endif %}
    {% endwith %}
    <input type="text" name="name" placeholder="Имя">
    <input type="submit" value="Отправить">
</form>

</body>
</html>
"""
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Hello {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('task8.html')


"""Задание №9 📌 Создать страницу, на которой будет форма для ввода имени и электронной почты 📌 При отправке которой будет создан cookie файл с данными пользователя 📌 Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя. 📌 На странице приветствия должна быть кнопка "Выйти" 📌 При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""