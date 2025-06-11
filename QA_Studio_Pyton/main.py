import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '49406796f709a39dfe0c33256d2178fb'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_MAIL",
    "password": "USER_PASSWORD"
}

body_confirm = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_name = {
    "pokemon_id": id,
    "name": "New Name",
    "photo_id": 12
}

body_pokeball = {
    "pokemon_id": id
}

'''requests = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

requests_confirm = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirm)
print(response_confirm.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)

message = response_create.json()['message']
print(message)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.json)

message = response_name.json()['message']
print(message)

response_pokeball = request.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.json)

message = response_pokeball.json()['message']
print(message)