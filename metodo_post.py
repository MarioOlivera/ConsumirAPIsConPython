import requests
import json

'''
SI ENVIAMOS PARAMS:

con parametro json=payload va a data
con parametro data va a from, pero debemos encargarnos de serializarlo json.dumps(payload)
'''

url = 'https://httpbin.org/post'
payload = { 'nombre': "Mario", 'lenguage': 'Python'} # usando diccionario
response = requests.post(url, data= json.dumps(payload))

if response.status_code == 200:

    response_json = json.loads(response.content)
    print(response_json)