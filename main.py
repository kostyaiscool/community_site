from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
def connect_to_data_base():
    connect_to_db1 = sqlite3.connect('communities_data.db')
    connect_to_db1.row_factory = sqlite3.Row
    cursor = connect_to_db1.cursor()
    return cursor
def do_a_script(script):
    cursor = connect_to_data_base()
    with open(script) as script_file:
        cursor.executescript(script_file.read())

do_a_script('scratch_2.sql')
@app.route('/')
# def page():
#     return '''
#     <h1>fghejdhvdjdhcfgr</h1>
#     <h2>fghejdhvdjdhcfgr</h2>
#     <h3>fghejdhvdjdhcfgr</h3>
#     <h4>fghejdhvdjdhcfgr</h4>
#     <h5>fghejdhvdjdhcfgr</h5>
#     <h6>fghejdhvdjdhcfgr</h6>'''
def main_page():
    cursor = connect_to_data_base()
    cursor.execute('SELECT * from Communities')
    communities = cursor.fetchall()
    return render_template('main_page.html', communities = communities)
@app.route('/community')
def community():
    return render_template('community_page.html')
# @app.route('/<name>')
# def print_name(name):
#     return 'privet, ' + name
@app.route('/test')
def test():
    aboba = request.args.get('name')
    return 'privet' + aboba

app.run(debug=True)