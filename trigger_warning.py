import requests

# Define a constant for the base URL
BASE_URL = "https://example.com/api"

def fetch_data(endpoint):
    """
    Fetches data from the given API endpoint with a timeout.

    Args:
        endpoint (str): The API endpoint to fetch data from.

    Returns:
        dict: The response JSON if the request is successful, otherwise None.
    """
    full_url = f"{BASE_URL}/{endpoint}"  # Avoids redefining 'url'
    
    try:
        response = requests.get(full_url, timeout=10)  # Added timeout
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")  # Proper error handling
        return None


class SomeClass:
    """Example class with a method."""

    def some_method(self):
        """An example method."""
        print("This is a method.")


# Ensure correct formatting: 2 blank lines after class/method definitions
if __name__ == "__main__":

    data = fetch_data("data")
    if data:
        print("Data fetched successfully!")
