import requests
import json
import time
from datetime import datetime


# Power BI API URL and key
coincap_url = "https://api.coincap.io/v2/assets/bitcoin"
power_bi_api_url = "https://api.powerbi.com/beta/<workspace_id>/datasets/<dataset_id>/rows?key=<your_api_key>"

def generate_data():

    response = requests.get(coincap_url)

    if response.status_code == 200:
        data = response.json()
        price = float(data['data']['priceUsd'])

        json_data = [{
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            "price": price
        }]

        headers = {"Content-Type": "application/json"}
        powerbi_response = requests.post(power_bi_api_url
        

