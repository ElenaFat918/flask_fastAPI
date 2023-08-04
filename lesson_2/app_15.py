"""
Сессии в Flask являются способом сохранения данных между запросами.
"""

from flask import Flask, request, make_response, render_template,session, redirect, url_for

app = Flask(__name__)

app.secret_key =b'9e781488096ff67619389de11d8e54fce4e6a42f3f89532f35125fa78f7079a7'


@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)