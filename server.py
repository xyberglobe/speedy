from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/test_speed', methods=['GET'])
def test_speed():
    # Simulate speed test results
    download_speed = round(random.uniform(10, 100), 2)  # Random download speed between 10 and 100 Mbps
    upload_speed = round(random.uniform(5, 50), 2)      # Random upload speed between 5 and 50 Mbps
    ping = random.randint(10, 100)                     # Random ping between 10 and 100 ms

    return jsonify({
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "ping": ping
    })

if __name__ == '__main__':
    app.run(debug=True)

