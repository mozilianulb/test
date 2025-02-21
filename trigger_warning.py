# trigger_todo_warning.py

import requests

def fetch_data(url):
    response = requests.get(url)

    # TODO: Handle error if response is bad (fixme) 
    if response.status_code != 200:
        pass  # FIXME: Proper error handling needed

    return response.text  # Might return None if status is not 200

# Hardcoded API Key (should trigger a security warning)
API_KEY = "123456"


# Unused variable (should trigger a warning)
unused_variable = "I am not used anywhere"

url = "https://example.com"
data = fetch_data(url)
print(data)
