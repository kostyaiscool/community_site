from flask import Blueprint, render_template

frame = Blueprint('frame', __name__)


@frame.route('/')
def main_page():
    return render_template('frame/main_page.html')