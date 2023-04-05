sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
# Napiš software, který bude využívat prodavač v případě, 
# že do obchodu přijde zákazník. 
# Software se nejprve zeptá na kód součástky 
# a poté na množství, které si zákazník chce koupit.
kod_soucastky = input("Zadejte kód součástky: ")
mnozstvi = int(input("Zadejte požadované množství: "))

# Pokud zadaný kód není ve slovníku, není součástka skladem. 
# Vypiš tedy zprávu, že součástka není skladem.
if kod_soucastky not in sklad:
    print("Součástka není skladem.")

# Pokud zadaná součástka na skladě je, ale je jí méně, 
# než požaduje zákazník, vypiš text o tom, 
# že lze prodat pouze omezené množství kusů.
elif sklad[kod_soucastky] < mnozstvi:
    print("Lze prodat pouze omezené množství kusů.")

# Následně součástku odeber ze slovníku, protože je vyprodaná.
# Uživatel zadá třeba množství 100 u součástky 2N7002 a zobrazí se mu,
# že už je vyprodaná. Odebereme ji tedy ze slovníku.
    sklad.pop(kod_soucastky)
    print("Skladové zásoby: ", sklad)
else:
    print("Poptávku lze uspokojit v plné výši.")
# A sniž počet součástek na skladě o množství požadované zákazníkem.
    sklad[kod_soucastky] -= mnozstvi
    print("Skladové zásoby: ", sklad)