from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Environment variables for API keys
TIKTOK_API_KEY = os.getenv('TIKTOK_API_KEY')
INSTAGRAM_API_KEY = os.getenv('INSTAGRAM_API_KEY')
GOOGLE_ADS_API_KEY = os.getenv('GOOGLE_ADS_API_KEY')

@app.route('/metrics/tiktok', methods=['GET'])
def get_tiktok_metrics():
    # Implementasi panggilan ke API TikTok di sini
    # Contoh panggilan API ke TikTok
    response = requests.get('https://api.tiktok.com/v1/metrics', headers={'Authorization': f'Bearer {TIKTOK_API_KEY}'})
    data = response.json()
    return jsonify(data)

@app.route('/metrics/instagram', methods=['GET'])
def get_instagram_metrics():
    # Implementasi panggilan ke API Instagram di sini
    # Contoh panggilan API ke Instagram
    response = requests.get('https://graph.instagram.com/v1/metrics', headers={'Authorization': f'Bearer {INSTAGRAM_API_KEY}'})
    data = response.json()
    return jsonify(data)

@app.route('/metrics/google_ads', methods=['GET'])
def get_google_ads_metrics():
    # Implementasi panggilan ke API Google Ads di sini
    # Contoh panggilan API ke Google Ads
    response = requests.get('https://googleads.googleapis.com/v1/metrics', headers={'Authorization': f'Bearer {GOOGLE_ADS_API_KEY}'})
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
