import requests  # Unused import (should trigger a warning)

def fetch_data(url):
    response = requests.get(url)
    
    # TODO: This is an unfinished function (Prospector should flag this)
    # FIXME: Handle non-200 status codes properly
    
    if response.status_code != 200:
        pass  # FIXME: No proper error handling;

    # Intentional issue: Unused variable (Prospector should flag this)
    data = response.text  

    return data  # Might return None if status is not 200

# Security issue: Hardcoded API Key
API_KEY = "123456"

url = "https://example.com"
data = fetch_data(url)
print(data)
