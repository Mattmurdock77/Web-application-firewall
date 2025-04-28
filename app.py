from flask import Flask
from waf import check_request

# Initialize the Flask app
app = Flask(__name__)

# Attach the WAF middleware
app.before_request(check_request)

# Define routes
@app.route('/')
def home():
    return 'Welcome to the Flask Web Application Firewall!'

if __name__ == '__main__':
    app.run(debug=True)
