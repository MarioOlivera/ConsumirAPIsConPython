import requests
import json

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form/', offset = 0):
    
    args = { 'offset' : offset}

    response = requests.get(url, params = args)

    if response.status_code == 200:

        payload = response.json()

        # obtengo 'results' del diccionario, en caso de no existir la posicion devuelvo diccionario vacio
        results = payload.get('results', []) 

        if results:

            for pokemon in results:
                name = pokemon['name']

                print(name)

        next_page = input("¿Continuar listando? [Y/N]").lower()

        if next_page == 'y':
            get_pokemons(offset = offset+20 )


get_pokemons()


