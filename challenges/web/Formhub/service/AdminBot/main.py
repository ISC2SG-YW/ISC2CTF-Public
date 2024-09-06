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
        
    def authenticate_and_visit_admin(self,userId):
        with self.lock:
            admin_url = f"{self.base_url}/admin"
            self.driver.get(admin_url)

            self.driver.add_cookie({
                'name': 'auth_token',
                'value': self.auth_token,
                'path': '/',
                'httpOnly': True 
            })
            self.driver.add_cookie({
                'name': 'userId',
                'value': userId
            })
            # Refresh the page after setting the cookie
            self.driver.refresh()
            print("Visited the /admin endpoint with authentication.")

    def visit_url(self, url,userId):
        self.driver.delete_all_cookies()
        self.authenticate_and_visit_admin(userId)
        with self.lock:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            return self.driver.title, self.driver.page_source

    def close(self):
        self.driver.quit()

bot = AdminBot('http://formhub-website:5000', os.environ.get('ADMIN_CREDS','admin_creds'))
@app.route('/visit', methods=['POST'])
def visit():
    # Get the Admin Bot to visit the requested page
    url = request.form.get('url')
    userId = request.form.get('userId')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    try:
        title, page_source = bot.visit_url(url,userId)
        return jsonify({"title": title, "page_source": page_source}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run( port = 420)
