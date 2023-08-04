"""
Flashсообщения. функцияflash().Она
принимает сообщение и категорию,к которой это сообщение относится,
и сохраняет его во временном хранилище.
.Чтобы не получать ошибки вида при работе с сессией RuntimeError:
The session is unavailable because no secret key was set.
Set the secret_key on the application to something unique and secret.
необходимо добавить в Flask приложение секретный ключ.
Простейший способ генерации такого ключа,выполнить следующие пару строк кода
"""

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b'9e781488096ff67619389de11d8e54fce4e6a42f3f89532f35125fa78f7079a7'
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Hi!'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы, Форма успешно отправлена будет храниться в <message>, success - <category>
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')



if __name__ == "__main__":
    app.run(debug=True)
