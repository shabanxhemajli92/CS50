import requests


# dictionary = {
#     "next": "a link",
#     "results": [
#         {"name": "A", "items": ["Shaban"]},
#         {"name": "B", "items": ["Peer"]},
#         {"name": "C", "items": ["Jacques"]},
#         {"name": "D", "items": ["Muhannad"]},
#     ]
# }

# for r in dictionary['results']:
#     print(r["items"][0])

# for r in dictionary["results"]:
#     file = open("pokemon.txt","a")
#     file.write(f"{r['name']}\n")
#     file.close()

base_url='https://pokeapi.co/api/v2/pokemon'
response = requests.get(base_url)

data=response.json()
print(response.json())
for r in data["results"]:
    print(r["name"])

for r in data["results"]:
    file = open("pokemon.txt","a")
    file.write(f"{r['name']}\n")
    file.close()

BASE_URL = 'https://pokeapi.co/api/v2/pokemon'

def fetch_pokemons(url):
    response = requests.get(url)
    data = response.json()
    file = open('pokemon.txt', 'a')
    for result in data['results']:    
        file.write(f"{result['name']}\n")
    file.close()

    # if data.get('next', None): # true -> existing string
    if data['next']: # key error 
        fetch_pokemons(data['next'])    

    # we have to call "fetch_pokemons(next)"

# call the function
fetch_pokemons(BASE_URL)  