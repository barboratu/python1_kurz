# Vytvořte aplikaci pro zasílání SMS zpráv. 
# Napište program, který provede následující činnosti:
# Zeptá se na číslo, kam chce zprávu poslat, a ověří, jestli má číslo správný formát.
# Zeptá se uživatele na zprávu, kterou chce odeslat. Potom vypíše, kolik zpráva bude stát.

def overeni_cisla(cislo):
    """Funkce ověřuje, jestli je zadané číslo platné, platné je v případě, 
    že je devítimístné nebo třináctimístné s předvolbou +420, jinak je neplatné."""
    # Pokud se zadá třináctimístné číslo (devítimístné číslo s předvolbou)
    if len(cislo) == 13 and cislo[:4] == "+420":
        return True
    # Pokud se zadá devítimístné číslo bez předvolby
    elif len(cislo) == 9:
        return True
    else:
        return False
zadane_cislo = input("Zadejte číslo: ")
if overeni_cisla(zadane_cislo):
    print("Číslo je platné.")
else:
    print("Číslo není platné.")

def cena_zpravy(zprava):
    """ Funkce vypočítá cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků. """
    pocet_znaku = len(zprava)
    cena = pocet_znaku // 180 * 3
    if pocet_znaku % 180 != 0:
        cena += 3
    return cena

# Uživatel zadá zprávu.
zprava = input("Zadejte text zprávy: ")
# Vypočítáme cenu zprávy.
cena = cena_zpravy(zprava)
# Vypíšeme cenu zprávy.
print(f"Cena zprávy je: {cena} Kč")


    
