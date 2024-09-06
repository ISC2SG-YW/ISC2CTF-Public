from flask import Flask, request, jsonify,render_template, Response, make_response
import sqlite3 
import time
import os
import requests
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getPoints():
    # The online graph is not part of the Challenge. Please don't try to abuse me :c
    conn = sqlite3.connect('online.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT x,y FROM graphs ORDER BY date DESC LIMIT 1000')
    # return ASSOC
    
    points = list(cursor.fetchall())
    conn.close()
    return points

def addPoint(x,y):
    conn = sqlite3.connect('online.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO graphs (x,y,date) VALUES (?,?,?)', (x,y,time.time()))
    conn.commit()
    conn.close()
app = Flask(__name__)

@app.route('/')
def index():
    data = getPoints()
    return render_template('index.html' , data = data)

@app.route('/create')
def create():
    points = request.args.get('data',default = "[]")
    return render_template('create.html', points = points)

@app.route('/add_point', methods=['POST'])
def add_point():
    x = request.form['x']
    y = request.form['y']
    addPoint(x,y)
    return jsonify({'status': 'ok'})

@app.route('/send_baba', methods=['POST'])
def send_baba():
    data = request.form['data']
    print(data, file=os.sys.stderr)
    if not data:
        return jsonify({'status': 'error'})
    response = requests.post("http://graph-theory-admin-bot:12345/visit",json = data)
    data = response.json()
    return jsonify(data)

   
@app.route('/admin',methods = ['GET'])
def admin():
    auth = request.cookies.get('auth_token')
    if auth != os.environ.get('ADMIN_CREDS','admin_creds'):
        return Response("Unauthorized",401)
    return Response("Flag: "+os.environ.get('FLAG','ISC2CTF{test_flag}'))

if __name__ == '__main__':
    app.run(port = 3000)