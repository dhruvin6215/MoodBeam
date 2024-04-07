import requests

# Replace with your ESP32's IP address and endpoint
url = 'http://172.20.10.12/data'

# Replace with the integer value you want to send
data = {'value': 1}

# Send a POST request with JSON payload
response = requests.post(url, json=data)

print(response.text)  # Output the response from the ESP32
