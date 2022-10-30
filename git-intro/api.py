from urllib import response
import requests

response = requests.get("https://randomfox.ca/floof")
forx=response.json()

print(forx['image'])