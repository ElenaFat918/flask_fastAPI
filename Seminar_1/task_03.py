# Задание №3
# 📌 Написать функцию,
# которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


# @app.route('/')
def index():
    return 'Hello World!'


@app.route('/<int:a> <int:b>')
def hello(a, b):
    return f'{a} + {b}= {a + b}'


if __name__ == "__main__":
    app.run(debug=True)
