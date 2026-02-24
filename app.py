import os
import json
from flask import Flask, render_template, request, send_file

# Import vlastního modulu
import scraper

app = Flask(__name__)

# Routing pro hlavní stránku - umí web zobrazit (GET) i přijmout data z formuláře (POST)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 1. Uživatel klikl na tlačítko, vytáhne slovo z inputu
        hledany_vyraz = request.form.get("klicove_slovo")

        # 2. Zavolá vlastní funkci ze scraper.py
        data = scraper.ziskej_data(hledany_vyraz)

        # 3. Uloží data do souboru
        vystupni_soubor = "vysledky.json"
        with open(vystupni_soubor, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        # 4. Odešle soubor uživateli ke stažení
        return send_file(vystupni_soubor, as_attachment=True)

    # Pokud uživatel jen přišel na web (metoda GET), ukáže se mu HTML stránka
    return render_template("index.html")

if __name__ == "__main__":
    # Spuštění serveru v debug módu pro lokální testování
    app.run(debug=True)