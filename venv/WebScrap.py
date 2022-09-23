import urllib
import bs4
import pandas
from urllib import request

# Etape 1 : se connecter à la page wikipedia et obtenir le code source

url_ligue_1 = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"

request_text = request.urlopen(url_ligue_1).read()
print(request_text[:1000])

# Etape 2 : utiliser le package BeautifulSoup
# qui "comprend" les balises contenues dans la chaine de caractères renvoyée par la fonction request

page = bs4.BeautifulSoup(request_text, "lxml")

#print(page)
print("Il y a", len(page.findAll("table")), "éléments dans la page qui sont des <table>")
