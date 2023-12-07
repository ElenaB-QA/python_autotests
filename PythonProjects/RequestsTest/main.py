import requests

token =  'd0702b7d6dc51c42c70b44844774a9dd'

response_pokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons',
              headers = {'Content-Type': 'application/json',
                         'trainer_token':token}, 
              json = {
    "name": "Google",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(response_pokemons.text)

response_edit_name = requests.put ('https://api.pokemonbattle.me:9104/pokemons',
              headers = {'Content-Type': 'application/json',
                         'trainer_token':token},
                         json = {
    "pokemon_id": "21397",
    "name": "Google2",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(response_edit_name.text)

response_add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
              headers = {'Content-Type': 'application/json',
                         'trainer_token':token},
                         json = {
    "pokemon_id": "21397"
})

print(response_add_pokeball.text)