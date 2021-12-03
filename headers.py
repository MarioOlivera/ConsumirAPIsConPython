import requests
import json

url = 'https://httpbin.org/post'
payload = { 'nombre': 'Mario', 'lenguaje': 'Python' }
headers = { 'Content-Type' : 'application/json' }

server_response = requests.post(url, data = json.dumps(payload), headers = headers)

if server_response.status_code == 200:
    
    #obteniendo los headers de la respuesta
    headers_response = server_response.headers
    server_response = headers_response['Server']

    print("SERVER", server_response)