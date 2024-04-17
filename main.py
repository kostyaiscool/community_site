from flask import Flask, render_template, request
from frame.views import frame
# import sqlite3
#
# app = Flask(__name__)
# def connect_to_data_base():
#     connect_to_db1 = sqlite3.connect('communities_data.db')
#     connect_to_db1.row_factory = sqlite3.Row
#     cursor = connect_to_db1.cursor()
#     return cursor
# def do_a_script(script):
#     cursor = connect_to_data_base()
#     with open(script) as script_file:
#         cursor.executescript(script_file.read())
#
# do_a_script('scratch_2.sql')
app = Flask(__name__)
app.register_blueprint(frame)
app.run(debug=True)