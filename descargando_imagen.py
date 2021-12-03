import requests
import json

url = 'https://i.imgur.com/C5ZpUTu.jpeg'

response = requests.get(url, stream = True) # Realiza la peticion sin descargar el contenido

with open('image.jpg', 'wb') as file:

    for chunk in response.iter_content(): #Desacarga el contenido poco a poco
        file.write(chunk)

response.close()
