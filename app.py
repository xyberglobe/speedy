from flask import Flask, jsonify
from flask_cors import CORS
import speedtest

app = Flask(__name__)
CORS(app)

# Speed Test Function
def run_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000      # Mbps
        ping = st.results.ping  # Ping in milliseconds

        server_info = st.get_best_server()
        server_location = f"{server_info['name']} ({server_info['country']})"

        return download_speed, upload_speed, ping, server_location
    except Exception as e:
        return str(e), None, None, None

@app.route('/test_speed')
def test_speed():
    try:
        download_speed, upload_speed, ping, server_location = run_speed_test()
        
        if download_speed is None:
            return jsonify({'error': 'Could not fetch speed data'}), 500

        return jsonify({
            'download_speed': round(download_speed, 2),
            'upload_speed': round(upload_speed, 2),
            'ping': ping,
            'server_location': server_location
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
