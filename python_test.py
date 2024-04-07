import requests
import time
import random

# Replace with your ESP32's IP address and endpoint
url = 'http://172.20.10.12/data'
while True:

    # Replace with the integer value you want to send
    random_num = random.randint(1, 5)
    data = {'value': random_num}

    # Send a POST request with JSON payload
    response = requests.post(url, json=data)

    print(response.text)  # Output the response from the ESP32
    time.sleep(2)
