"""
Inizio SEO Task - Modul pro stahování dat
-----------------------------------------
Autor: Pavel Mareš
Poznámka: Vyrobeno po směnách na lakovně.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv() # Načtení proměnných prostředí z .env souboru do systému

api_key = os.getenv("API_KEY") # Načtení hodnoty API_KEY z prostředí, které bylo načteno z .env souboru

url = "https://serpapi.com/search" # URL pro API SerpApi


def ziskej_data(dotaz):
    params = {
        "engine": "google",
        "q": dotaz,
        "api_key": api_key
    } # Sestavení parametrů pro API (dotaz přijde dynamicky z webového formuláře)

    response = requests.get(url, params=params) # Odeslání GET požadavku na API SerpApi s danými parametry
    results = response.json() # Převod odpovědi z JSON formátu do Python slovníku

    return results # Vrácení získaných dat jako slovník

if __name__ == "__main__":
    print(ziskej_data("Testovací dotaz"))