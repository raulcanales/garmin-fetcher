from flask import Flask, jsonify
from garminconnect import Garmin

app = Flask(__name__)

# Garmin credentials (use environment variables for security)
import os
GARMIN_EMAIL = os.getenv("GARMIN_EMAIL", "your-email@example.com")
GARMIN_PASSWORD = os.getenv("GARMIN_PASSWORD", "your-password")

# Login to Garmin
client = Garmin(GARMIN_EMAIL, GARMIN_PASSWORD)
client.login()

@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        data = {
            "steps": client.get_steps_data("today"),
            "sleep": client.get_sleep_data("today"),
            "stress": client.get_stress_data("today"),
            "body_battery": client.get_body_battery_data("today"),
            "workouts": client.get_activities(10)
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
