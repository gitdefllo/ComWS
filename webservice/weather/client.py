#######################
# Client Authentication
#######################
import os
import json
import requests
import weather

# constantes de l'adresse serveur
host    = 'authorizationservice.azurewebsites.net'
headers = {'content-type':'application/x-www-form-urlencoded'}

# methode d'authentification
def authenticate(username, password, grant_type, client_id):
    print("-------------")
    print("REST / JSON")
    print("-------------")

    # appel de la methode post 'authenticate' du serveur
    url = 'https://' + host
    response = requests.post(url + '/oauth2/token', 
        data = { 
            "username": username,
            "password": password,
            "grant_type": grant_type,
            "client_id": client_id,
        }, 
        headers = headers)
    print(response.text + "\n")

    # si le serveur repond {'success'='true'}
    if response.status_code == 200:
        # appel du fichier externe 'weather.py'
        weather.init("Lyon", "France")

# execution du programme
authenticate("badreddine.dlaila@gfi.fr", "P@ssword123!", "password", "099153c2625149bc8ecb3e85e03f0022")
