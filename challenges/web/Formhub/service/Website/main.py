from flask import Flask, request, redirect, session , render_template, Response, make_response, jsonify
from urllib.parse import urlparse
from utils import *
import requests
import os 
CHALL_DOMAIN = "formhub-website:5000"
ADMIN_BOT_URL = "http://formhub-admin-bot:420/visit"
app = Flask(__name__)
# randomly generated secret key
app.secret_key = os.environ.get('SECRET_KEY', 'secret_key')

def loginAsAdmin(uuid):
    conn = connect(uuid)
    cursor = conn.cursor()
    cursor.execute("SELECT `username`,`userId` FROM users WHERE `userId` = 1")
    data = cursor.fetchone()
    conn.close()
    if data:
        session['userId'] = data[1]
        session['username'] = data[0]
        session['uuid'] = uuid
        return True
    return False
    
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        success, data = getUserIfExists(user,password)
        if success:
            session['username'] = data[2]
            session['uuid'] = data[1]
            session['userId'] = data[0]
            return redirect('/welcome')
        else:
            return redirect(f'/login?error={data[0]}')
    else:
        users = get_number_users()
        error = request.args.get('error')
        if error:
            return render_template('login.html', error=error, users = users)
        else:
            return render_template('login.html', users = users)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        success, data = create_user(user,password)
        if success:
            session['username'] = data[2]
            session['uuid'] = data[1]
            session['userId'] = data[0]
            return redirect('/welcome')
        else:
            return redirect(f'/signup?error={data[0]}')
    else:
        error = request.args.get('error')
        users = get_number_users()
        if error:
            return render_template('signup.html', error=error, users = users)
        else:
            return render_template('signup.html', users = users)


@app.route('/forms', methods=['GET'])
def forms(formId = None):
    if 'username' not in session:
        return redirect('/login')
    uuid = session['uuid']
    formsData = getForms(uuid)
    return render_template('forms.html', forms=formsData)

@app.route('/create_form', methods=['GET','POST'])
def create_form():
    if 'username' not in session:
        return redirect('/login')
    if request.method == 'GET':
        return render_template('create_form.html')
    else:
        uuid = session['uuid']
        formName = request.form['formName']
        formLink = request.form['formLink']
        formDescription = request.form['formDescription']
        userId = session['userId']
        conn = connect(uuid)
        cursor = conn.cursor()
        cursor.executescript(f"INSERT INTO forms (formName,formLink,creatorId,formDescription) VALUES ('{formName}','{formLink}','{userId}','{formDescription}')")
        conn.commit()
        conn.close()
        return redirect('/forms')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    return render_template('welcome.html',username=username)

@app.route('/report',methods = ['POST'])
def report():
    if 'username' not in session:
        return redirect('/login')
    url = request.form['url']
    userId = session['userId']
    print("Test")
    if not urlparse(url).netloc == CHALL_DOMAIN:
        return jsonify({"error":"Invalid URL"}),400
    
    if "forms" not in url:
        url = url + "/forms"
    print("URL",url)
    r = requests.post(ADMIN_BOT_URL,data = {"url":url,"userId":userId})
    return r.json()
    
@app.route('/admin',methods = ['GET'])
def admin():
    auth = request.cookies.get('auth_token')
    if auth != os.environ.get('ADMIN_CREDS','admin_creds'):
        return Response("Unauthorized",401)
    userId = request.cookies.get('userId')
    success, data = getUserByUserId(userId)
    if not success:
        return Response("User not found",404)
    userId,uuid,username = data
    if not loginAsAdmin(uuid):
        return Response("Unauthorized",401)
    response = make_response()
    response.set_cookie('flag',os.environ.get('FLAG','ISC2CTF{test_flag}'))
    return response 
    

if __name__ == '__main__':
    app.run(debug=True)