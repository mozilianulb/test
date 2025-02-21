import requests

def fetch_data(url):
    response = requests.get(url)
    # TODO: handle error if response bad (fixme)
    if response.status_code != 200:
        pass  # FIXME: This should handle errors properly
    return response.text

url = "https://example.com"
data = fetch_data(url)
print(data)
