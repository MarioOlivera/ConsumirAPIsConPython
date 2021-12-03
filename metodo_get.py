import requests
import json

url = 'https://httpbin.org/get'

args = { 'nombre': "Mario", 'lenguage': 'Python'} # usando diccionario

response = requests.get(url, params=args)

if response.status_code == 200:
    '''
    response_json = response.json() # diccionario
    
    print("RESPUESTA",response_json)
    '''

    response_json = json.loads(response.text)
    print("RESPUESTA",response_json)