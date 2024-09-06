from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import os

app = Flask(__name__)

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, necessary for running in a container
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (may not be needed for headless mode)
    return chrome_options

class AdminBot:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token
        self.driver = webdriver.Chrome(options=set_chrome_options())
        self.lock = threading.Lock()
            

    def visit_url(self, data):
        self.driver.delete_all_cookies()
        with self.lock:
            self.driver.get(self.base_url)
            self.driver.add_cookie({
                'name': 'auth_token',
                'value': self.auth_token,
                'path': '/',
                'httpOnly': True 
            })
            self.driver.refresh()
            print("Visited the /admin endpoint with authentication.")
            
            self.driver.get(f"{self.base_url}/create?data={data}")
            self.driver.implicitly_wait(10)
            return "Baba does not understand this Graph :c."

    def close(self):
        self.driver.quit()

bot = AdminBot('http://graph-theory-website:3000', os.environ.get('ADMIN_CREDS','admin_creds'))
# configure JSON
@app.route('/visit', methods=['POST'])
def visit():
    # Get the Admin Bot to visit the requested page
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided."}), 400
    try:
        result = bot.visit_url(data)
        return jsonify({"data":result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run( port = 12345)
