
import requests
endpoint = "http://localhost:4000/api/products/7777777"
get_response = requests.get(endpoint) # HTTP Request
print(get_response.json())
