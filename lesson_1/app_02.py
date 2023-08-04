from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nike():
    return 'Привет, Ниеолай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'


if __name__ == "__main__":
    app.run()
