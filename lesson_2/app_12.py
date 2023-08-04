"""
Категории сообщений в flash позволяют различать типы сообщенийи выводить их по-разному.
Категория по умолчанию message.
Новторым аргументом можно передавать и другие категории,например warning,success и другие.
"""

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b'9e781488096ff67619389de11d8e54fce4e6a42f3f89532f35125fa78f7079a7'


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
