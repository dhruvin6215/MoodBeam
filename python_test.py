import requests

# Replace with your ESP32's IP address and endpoint
url = 'http://ESP32_IP_ADDRESS/data'

# Replace with the integer value you want to send
data = {'value': 123}

# Send a POST request with JSON payload
response = requests.post(url, json=data)

print(response.text)  # Output the response from the ESP32
