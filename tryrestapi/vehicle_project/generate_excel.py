import requests
import pandas as pd
from datetime import datetime
import argparse

LOGIN_URL = "https://api.baubuddy.de/index.php/login"
DATA_URL = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
API_KEY = "QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz"  
USERNAME = "365"
PASSWORD = "1"

def get_access_token():
    headers = {
        "Authorization": f"Basic {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(LOGIN_URL, json=payload, headers=headers)
    response_data = response.json()
    return response_data['oauth']['access_token']

def fetch_data(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(DATA_URL, headers=headers)
    return response.json()

def save_to_excel(data, file_name, colored):
    df = pd.DataFrame(data)
    

    if colored:
        df.style.applymap(lambda x: 'background-color: yellow' if pd.to_datetime(x, errors='coerce') < pd.Timestamp.now() else '', subset=['hu'])
    
    df.to_excel(file_name, index=False)

def main():
    parser = argparse.ArgumentParser(description="Process vehicle data.")
    parser.add_argument('-c', '--colored', action='store_true', help="Color the Excel output.")
    args = parser.parse_args()

    access_token = get_access_token()
    
    data = fetch_data(access_token)
    
    today = datetime.now().strftime('%Y-%m-%d')
    file_name = f'vehicles_{today}.xlsx'
    
    save_to_excel(data, file_name, args.colored)

if __name__ == "__main__":
    main()

