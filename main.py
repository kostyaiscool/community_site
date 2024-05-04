from flask_login import LoginManager

from init_db import db
from flask import Flask

from frame.views import frame
from users.models import User
from users.views import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///qust.db'
app.config['SECRET_KEY'] = 'Shkolnik iz doti bezmozgliy'
app.register_blueprint(frame)
app.register_blueprint(auth)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


db.init_app(app)
login_manager.init_app(app)

with app.app_context():

    db.create_all()



app.run(debug=True)
