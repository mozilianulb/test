import requests

def fetch_data(url):
    response = requests.get(url)

    # TODO: handle error if response bad (fixme) - This should trigger a warning
    if response.status_code != 200:
        pass  # FIXME: This should handle errors properly

    # Prospector will flag this: Unused variable
    data = response.text  

    return data  # Might return None if status is not 200

# Prospector security issue: Hardcoded API Key
API_KEY = "123456"

url = "https://example.com"
data = fetch_data(url)
print(data)

