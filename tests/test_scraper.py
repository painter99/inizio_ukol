import pytest
from unittest.mock import patch, MagicMock
# Import funkce, kterou chci testovat
from scraper import ziskej_data

# Až se v testu zavolá 'requests.get', nepoužije se opravdový internet,
# ale použije tuto náhražku (mock).
@patch('scraper.requests.get')
def test_ziskej_data_vraci_spravnou_strukturu(mock_get):
    
    # 1. Příprava
    # Nastavení, co má podstrčená odpověď obsahovat
    mock_response = MagicMock()
    # Tohle vrátí .json():
    mock_response.json.return_value = {
        "organic_results": [
            {"title": "Inizio - Marketing", "link": "https://inizio.cz"}
        ]
    }
    # Když zavolá requests.get(), vrátí to mock
    mock_get.return_value = mock_response

    # 2. Akce
    # Zavolá funkci s nějakým testovacím slovem
    vysledek = ziskej_data("testovací dotaz")

    # 3. Ověření
    # Kontrola, zda funkce opravdu vrátila podstrčenou náhražku dat
    assert vysledek["organic_results"][0]["title"] == "Inizio - Marketing"
    
    # Kontrola, zda se kód opravdu pokusil zavolat requests.get
    mock_get.assert_called_once()