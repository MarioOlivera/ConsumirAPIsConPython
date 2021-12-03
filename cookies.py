import requests
import json

url = 'https://httpbin.org/cookies'
cookies = { 'my-cookie': 'true' }

response = requests.get(url, cookies = cookies)

if response.status_code == 200:
    
    cookies = response.cookies #obtengo del diccionario

    print(cookies)

    response_json = json.loads(response.content)

    print("El contenido es: ")
    print(response_json)