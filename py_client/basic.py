
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:4000/api/" #http://127.0.0.1:4000/ 

get_response = requests.get(endpoint,json={"query": "Hello world"}) # HTTP Request
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
print(get_response.json())
# print(get_response.status_code)
# print(get_response.headers)