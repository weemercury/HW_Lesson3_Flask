from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from forms_1 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '91ef658ddc76c8a4768e6bef94d6c617822d4eb0c6cc985264e5cda32ed9a098'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/sucsses/')
def sucsses():
    return render_template('sucsses.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        print(username, password)
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
        return redirect(url_for('sucsses'))
    return render_template('register.html', form=form)


if __name__ == '__main__':  
    app.run(debug=True) 