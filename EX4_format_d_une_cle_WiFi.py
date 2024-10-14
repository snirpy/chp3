# Demander à l'utilisateur d'entrer une clé Wi-Fi WPA/WPA2
cle_wifi = input("Entrez une clé Wi-Fi WPA/WPA2 (8 à 63 caractères) : ")

# Variable pour suivre la validité de la clé
cle_valide = True

# Vérifier si la longueur de la clé est correcte
if len(cle_wifi) < 8 or len(cle_wifi) > 63:
    cle_valide = False
else:
    # Parcourir chaque caractère de la clé pour vérifier qu'il est alphanumérique
    for caractere in cle_wifi:
        if not caractere.isalnum():
            cle_valide = False
            break

# Afficher le résultat de la vérification
if cle_valide:
    print("La clé Wi-Fi est valide.")
else:
    print("La clé Wi-Fi est invalide.")
