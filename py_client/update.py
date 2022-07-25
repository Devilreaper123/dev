
import requests
endpoint = "http://localhost:4000/api/products/1/update"
data = {
    "title":"Hello world i am new here",
}
get_response = requests.put(endpoint , json=data) # HTTP Request
print(get_response.json())
