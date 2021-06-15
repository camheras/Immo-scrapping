from itertools import groupby

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

r = requests.get('http://www.encheres-publiques.com/annuaire/fiche_vente_en_cours.php?idp=144')
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
links = soup.findAll('table', style='border:1px solid #fff;')
# print(links)

formatted_links = []

for link in links:
    cleanr = re.findall('<a href.*>', str(link))
    req = requests.get(cleanr[0].split("\"")[1])
    s = BeautifulSoup(req.text, 'html.parser')
    # print(s)
    data = s.findAll('b')
    prix = s.find('b', style="color:#C85E2C;").text
    for l in data:
        if l.find(text=re.compile("Visite")):
            date_visite = str(l).split("place ")[1].split("<")[0]
        if l.find(text=re.compile("/ 45 -")):
            type = str(l.text)

    print(type, prix, date_visite)

