import requests

# Global variable
GLOBAL_URL = "https://example.com/api"  # ✅ Renamed to avoid conflict

def fetch_data(api_url):
    """Fetch data from the given API URL with a timeout."""
    try:
        response = requests.get(api_url, timeout=10)  # ✅ Added timeout
        response.raise_for_status()  # ✅ Added error handling
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")  # ✅ Removed TODO/FIXME, added handling
        return None


class ExampleClass:
    """An example class to illustrate proper formatting."""
    
    def example_method(self):
        """An example method."""
        print("Hello, world!")


# ✅ Ensured two blank lines after class/method definitions
GLOBAL_CONSTANT = 42
