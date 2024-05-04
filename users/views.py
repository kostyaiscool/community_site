from flask import render_template, redirect, url_for, abort, request, flash, Blueprint
from flask_login import login_user, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from init_db import db
from users.forms import LoginForm, RegistrationForm
from users.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('frame.main_page'))
        else:
            return abort(401)



    return render_template('users/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
    #     print(request.form)
    # if form.validate_on_submit():
        email = request.form.get('email')
        name = request.form.get('name')
        age = request.form.get('age')
        password = request.form.get('password')
        if email and name and age and password:
            hashed_password = generate_password_hash(password)
            user = User(name=name, age=age, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            return abort(5492, {'error': 'Вас взломали, ТРИСТА ПОЛНЫЙ ВЕК ТРАКТОРИСТА'})
    return render_template('users/register.html', title='Register', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    pass