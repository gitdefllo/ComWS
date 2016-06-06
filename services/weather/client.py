#######################
# Client Authentication
#######################
import os
import json
import requests
import weather

# constantes de l'adresse serveur
host    = 'nodejsauth.azurewebsites.net'
port    = '1337'
headers = {'content-type':'application/json'}

# methode d'authentification
def authenticate(login, password):
    print("-------------")
    print("REST / JSON")
    print("-------------")

    # appel de la methode post 'authenticate' du serveur
    url = 'http://'+host+':'+port
    response = requests.post(url + '/authenticate', 
        data = json.dumps({ 
            "login": login,
            "password": password
        }), 
        headers = headers)
    print(response.text + "\n")

    # si le serveur repond {'success'='true'}
    if response.status_code == 200 and response.json()['success'] == True:
        # appel du fichier externe 'weather.py'
    	weather.init("Lyon", "France")

# execution du programme
authenticate("User1", "123")