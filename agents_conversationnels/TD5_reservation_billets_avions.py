# Hugo BERANGER - M2 MIAGE IA

import dateutil.parser as dparser

print("Bienvenue sur la plateforme de réservation")


ville_valides = ["nice",
                "paris",
                "marseille",
                "lyon",
                "toulouse",
                "nice",
                "nantes",
                "montpellier",
                "strasbourg",
                "bordeaux",
                "lille",
                "rennes"]

def extract_date(string, fuzzy=False):
    try: 
        return dparser.parse(string,fuzzy=True)
    except ValueError:
        return False

confirmation = False
while(confirmation != True):
    while(confirmation!=True):
        print("Quelle est votre ville de depart ? (ville)")
        ville_depart = input("").lower()
        ville_depart = ville_depart.split()
        for mot in ville_depart:
            if mot in ville_valides:
                ville_depart = mot
                confirmation=True

    confirmation = False
    while(confirmation!=True):
        print("Ou vous rendez vous ? (ville)")
        ville_arrive = input("").lower()
        ville_arrive = ville_arrive.split()
        for mot in ville_arrive:
            if mot in ville_valides and mot != ville_depart:
                ville_arrive = mot
                confirmation=True

    confirmation = False
    while(confirmation!=True):
        print("Quand voulez vous partir ? (dd/mm/yyyy)")
        date = input("").lower()
        if extract_date(date) != False:
                date = extract_date(date)
                confirmation=True


    confirmation = False
    while(confirmation!=True):
        print("Es-ce un aller simple ou un aller retour ? (aller simple/aller retour)")
        type_vole = input("").lower()
        type_vole = type_vole.split()
        for mot in type_vole:
            if mot == "simple" or mot == "aller-simple":
                type_vole = "simple"
                confirmation = True
            elif mot == "retour" or mot == "aller-retour":
                type_vole = "retour"
                confirmation = True


    confirmation = False
    if type_vole == "simple":
        print("Voulez vous bien partir de {} à {} le {} pour un aller-{}? (oui/non)".format(
                ville_depart,
                ville_arrive,
                date,
                type_vole))
        confirmation_vol = input("").lower()
        confirmation_vol = confirmation_vol.split()
        for mot in confirmation_vol:
            if mot == "oui":
                confirmation_vol = True
                print("Réservation effectuée")
            elif mot == "non":
                confirmation_vol = False
                print("Réservation annulée")
    elif type_vole == "retour":
        confirmation = False
        while(confirmation!=True):
            print("Quand voulez vous repartir ? (dd/mm/yyyy)")
            date_retour = input("").lower()
            if extract_date(date_retour) != False:
                date_retour = extract_date(date_retour)
                if date_retour < date:
                    confirmatio=False
                else:
                    confirmation=True
                    print("Voulez vous bien partir de {} à {} le {} et faire le trajet retour le {} pour un aller-{}? (oui/non)".format(ville_depart,
                            ville_arrive,
                            date,
                            date_retour,
                            type_vole))
                    confirmation_vol = input("").lower()
                    confirmation_vol = confirmation_vol.split()
                    for mot in confirmation_vol:
                        if mot == "oui":
                            confirmation_vol = True
                            print("Réservation effectuée")
                        elif mot == "non":
                            confirmation_vol = False
                            print("Réservation annulée")
            else:
                confirmation=False
