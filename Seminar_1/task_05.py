# Задание №5 📌 Написать функцию,
# которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница"
# и абзацем "Привет, мир!".


from flask import Flask

html = """
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>
"""
app = Flask(__name__)


@app.route('/hello/')
def hello1():
    return html


if __name__ == "__main__":
    app.run(debug=True)
