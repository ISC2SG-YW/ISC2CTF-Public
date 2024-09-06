from flask import Flask, render_template, request, Response, make_response, jsonify
import requests
import time
import uuid
import sys

app = Flask(__name__)
last_polluted = {}
PHP_SERVER = "http://baba-loves-pollution-server:483"
def has_polluted(uuid):
    # Pollution has a cooldown of a day!
    if last_polluted.get(uuid) is None:
        return False
    if time.time() - last_polluted[uuid] > 86400:
        return False
    return True

@app.route("/")
def index():
    
    uuid_cookie = request.cookies.get("uuid")
    if uuid_cookie is None:
        uuid_cookie = str(uuid.uuid4())
    response = requests.get(f"{PHP_SERVER}/get_info.php?uuid={uuid_cookie}")
    data = response.json()
    token = get_token(uuid_cookie)
    resp = make_response(render_template("index.html",pollution=data['pollution_count'], total_pollution=data['total_pollution']))
    resp.set_cookie("uuid", uuid_cookie)
    
    resp.set_cookie("token", token)
    return resp

@app.route("/get_token/<uuid>", methods = ["GET"])
def get_token(uuid):
    # generates a new token for a user
    if has_polluted(uuid):
        return "You have already polluted today!"
    response = requests.get(f"{PHP_SERVER}/get_token.php?uuid={uuid}")
    
    return response.text


@app.route("/pollute", methods = ["POST"])
def pollute():
    data = request.get_data()
    uuid = request.form.get("uuid")
    if has_polluted(uuid):
        return jsonify({"success":False,"error":"You've already polluted today!"})
    last_polluted[uuid] = time.time()
    response = requests.post(f"{PHP_SERVER}/pollute.php", headers={"content-type": request.headers.get("content-type")},data = data)
    return response.text
if __name__ == '__main__':
    app.run()