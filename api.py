import requests

# Replace with your Hello World API URL
url = "https://dummy-json.mock.beeceptor.com/continents"

try:
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Response from API:", response.text)
    else:
        print(f"API returned status code {response.status_code}: {response.reason}")
except requests.exceptions.RequestException as e:
    print("Error making request:", e)
