import os # Načtení základní knihovny pro komunikaci s operačním systémem
from dotenv import load_dotenv # Načtení funkce z knihovny - prostředí z .env souboru

load_dotenv() # Načtení proměnných prostředí z .env souboru do systému

api_key = os.getenv("API_KEY") # Načtení hodnoty API_KEY z prostředí, které bylo načteno z .env souboru

if api_key: # Kontrola úspěšnosti použití API klíče
    print("Super! Klíč byl úspěšně načten a je připraven k použití.")
else:
    print("Chyba: Klíč nebyl nalezen. Zkontroluj soubor .env!")