from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


"""
определен маршрут /login, который обрабатывает GET и POST запросы.
В представлении создается объект LoginForm,
который передается в шаблон login.html с помощью функции render_template.
Если метод запроса POST и данные формы проходят валидацию,то выполняется
обработка данных из формы. Шаблон login.html должен содержать 
тег form с указанием метода и адреса для отправки данных формы,
а также поля формы с помощью тегов input. 
"""


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)


"""
определен маршрут /register, который обрабатывает GET и POST запросы.
В представлении создается объект RegistrationForm, который передается в шаблон register.html
с помощью функции render_template.
Если метод запроса POST и данные формы проходят валидацию,
то выполняется обработка данных из формы. 
Данные из полей формы можно получить с помощью свойств data объекта формы. 
Например, для поля email можно получить значение следующим образом: form.email.data.
"""

if __name__ == "__main__":
    app.run(debug=True)
