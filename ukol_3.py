# naimportujeme si json
import json
# načteme si soubor body.json, který jsme si předtím uložili do stejné složky
with open("body.json", encoding = "utf-8" ) as soubor:
    body_slovnik = json.load(soubor)
# Projdeme všechny položky v tomto slovníku 
# a podle počtu bodů nastavíme hodnotu klíče na hodnotu Pass nebo Fail.
prospech_slovnik = {}
for jmeno, body in body_slovnik.items():
    if body >= 60:
        prospech_slovnik[jmeno] = "Pass"
    else:
        prospech_slovnik[jmeno] = "Fail"
# uložíme výsledný slovník prospech_slovnik do souboru prospech.json
with open("prospech.json", mode = "w") as soubor:
    json.dump(prospech_slovnik, soubor)