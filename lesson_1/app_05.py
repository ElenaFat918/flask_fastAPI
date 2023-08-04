from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Лена</h1>
<p>Я только начинаю создавать сайты на Flask<br/>Посмотри на мой сайт.</p>
"""
@app.route('/')
def index():
    return 'Hi!'


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал',
            'Хитрый знает он язык',
            'Он к другому не привык',
            ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt


if __name__ == "__main__":
    app.run()
