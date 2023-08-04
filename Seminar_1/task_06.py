# Задание №6
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с таблицей,
# содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)

students = [{'name': 'Иван', 'surname': 'Иванов', 'age': 30, 'rate': '4,5'},
            {'name': 'Иван', 'surname': 'Иванов', 'age': 30, 'rate': '4,5'},
            {'name': 'Иван', 'surname': 'Иванов', 'age': 30, 'rate': '4,5'},
            {'name': 'Иван', 'surname': 'Иванов', 'age': 30, 'rate': '4,5'},
            ]
@app.route('/student/')
def get_students():
    return render_template('students.html', students=students)


@app.route('/first_html/')
def first_html():
    return render_template('first_html')


if __name__ == "__main__":
    app.run(debug=True)

