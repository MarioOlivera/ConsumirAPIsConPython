import requests
import json

url = 'https://httpbin.org/delete'
payload = { 'nombre' : 'Mario', 'lenguaje': "Python"}
headers = { 'Content-type' : 'application/json'}

server_response = requests.delete(url, data = json.dumps(payload), headers = headers)

if server_response.status_code == 200:

    response_json = json.loads(server_response.content)

    print(response_json)
