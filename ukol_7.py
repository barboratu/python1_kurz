class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozidla."
        else:
            return f"Vozidlo není k dispozici"
        
    def get_info (self):
        return f"Registrační značka: {self.registracni_znacka}, typ vozidla: {self.typ_vozidla}"
 
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, True)

pozadovana_znacka = input("Jakou značku vozidla si chcete půjčit (Peugeot nebo Škoda): ")
if pozadovana_znacka == "Peugeot":
    auto = auto1
elif pozadovana_znacka == "Škoda":
    auto = auto2
else:
    print("Nebyla zadána platná značka.")
    exit()

print(auto.get_info())
if auto.dostupne:
    print(auto.pujc_auto())
else:
    print("Vozidlo není k dispozici.")