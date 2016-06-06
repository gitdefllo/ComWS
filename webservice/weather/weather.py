################
# Client Weather
################
from lxml import etree
from StringIO import StringIO
from suds.client import Client
import msvcrt as msvcrt

# methode de recuperation des donnees meteo du service externe
def getWeather(city, country):
    # creation du client depuis l'url du service
    client = Client('http://www.webservicex.net/globalweather.asmx?wsdl')
    # appel de la methode du service avec les parametres
    datas = client.service.GetWeather(
        CityName = city,
        CountryName = country
    )
    # print(datas)
    # print("-------------")

    # iteration des donnees recues et affichage
    context = etree.iterparse(StringIO(datas.encode("utf16")))
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print elem.tag + " => " + text

# methode de recuperation d'un ville parmi une liste
def getSingleCity(cities, country):
    # initialisation des variables
    index = 0
    err = 0

    # attente de l'input de l'utilisateur
    print("Selectionnez votre ville (chiffre d'index du tableau): ")
    try:
        index = int(msvcrt.getch())
    except ValueError:
        err = 1

    # verification de l'input et de sa valeur
    if index < 0 or index > len(cities):
        err = 1

    # s'il y a une erreur, appel recursif de la methode parente
    if err == 1:
        print("Ce n'est pas un index valide. Veuillez reessayer...\n")
        getSingleCity(cities, country)
        return

    # appel de la methode pour recuperer la meteo d'une ville choisie
    print("-------------")
    getWeather(cities[index], country)

# methode de recuperation de toutes les villes d'un pays
def getCities(country):
    # creation d'un client depuis l'url du service
    client = Client('http://www.webservicex.net/globalweather.asmx?wsdl')
    # appel de la methode du service avec son parametre
    datas = client.service.GetCitiesByCountry(
        CountryName = country
    )
    # print(datas)
    print("-------------")

    # creation d'un tableau de retour
    cities = []
    # iteration des donnees recues et ajout dans le tableau
    context = etree.iterparse(StringIO(datas.encode("utf16")))
    for action, elem in context:
        if elem.tag == "City":
            cities.append(elem.text)

    # affichage et retour du tableau
    print(cities)
    return cities

# execution du programme
def init(city, country):
    print("-------------")
    print("SOAP / XML")
    print("-------------")
    cities = getCities(country)
    print("-------------")
    getSingleCity(cities, country)
