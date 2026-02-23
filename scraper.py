import os # Načtení základní knihovny pro komunikaci s operačním systémem
import requests # Načtení knihovny pro HTTP požadavky
from dotenv import load_dotenv # Načtení funkce z knihovny - prostředí z .env souboru

load_dotenv() # Načtení proměnných prostředí z .env souboru do systému

api_key = os.getenv("API_KEY") # Načtení hodnoty API_KEY z prostředí, které bylo načteno z .env souboru

url = "https://serpapi.com/search" # URL pro API SerpApi

params = {
    "engine": "google",
    "q": "Pavel Mareš Inizio",
    "api_key": api_key
} # Parametry pro API požadavek, včetně typu vyhledávače (Google), hledaného dotazu ("Pavel Mareš Inizio") a API klíče pro autentizaci

response = requests.get(url, params=params) # Odeslání GET požadavku na API SerpApi s danými parametry
results = response.json() # Převod odpovědi z JSON formátu do Python slovníku

print(results) # Výpis získaných výsledků na konzoli