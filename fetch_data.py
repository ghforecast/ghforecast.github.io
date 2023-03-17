import requests
import json

def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()

def cache_data(data, cache_file):
    with open(cache_file, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    API_URL = 'https://api.avalanche.org/v2/public/product?type=forecast&center_id=SAC&zone_id=77'
    CACHE_FILE = 'data/data.json'

    data = fetch_data(API_URL)
    cache_data(data, CACHE_FILE)
