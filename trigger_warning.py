import requests

# Use a different name to avoid redefinition
GLOBAL_URL = "https://example.com/api"

def fetch_data(api_url):
    """Fetch data from the given API URL with a timeout."""
    try:
        response = requests.get(api_url, timeout=10)  # ✅ Added timeout
        response.raise_for_status()  # ✅ Proper error handling
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")  # ✅ Replace TODO/FIXME with actual handling
        return None


class ExampleClass:
    """An example class to illustrate the fix."""
    
    def example_method(self):
        """An example method."""
        print("Hello, world!")


# Ensure 2 blank lines after class/method definitions
GLOBAL_CONSTANT = 42  # ✅ Fix: Ensured 2 blank lines after the class
