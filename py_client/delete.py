
import requests
product_id = input("What is the product ID you want to delete?")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not Valid')
if product_id:
    product_id = int(product_id)
    endpoint = f"http://localhost:4000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint) # HTTP Request
    print(get_response.status_code , get_response.status_code == 204)
