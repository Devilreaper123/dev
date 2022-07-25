import requests

endpoint = "http://localhost:4000/api/products/"
data = {
    "title":"This is done",
    "price":32.99
}
get_response = requests.post(endpoint , json = data) # HTTP Request
print(get_response.json())
