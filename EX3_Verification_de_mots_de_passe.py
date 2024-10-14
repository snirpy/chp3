# Demander à l'utilisateur de créer un mot de passe
mot_de_passe = input("Définissez un mot de passe : ")

# Initialiser le compteur de tentatives
tentatives = 0
max_tentatives = 3

# Boucle pour permettre les tentatives de connexion
while tentatives < max_tentatives:
    mot_de_passe_entre = input("Entrez votre mot de passe pour vous connecter : ")
    
    # Vérifier si le mot de passe est correct
    if mot_de_passe_entre == mot_de_passe:
        print("Connexion réussie. Bienvenue !")
        break
    else:
        tentatives += 1
        print(f"Mot de passe incorrect. Tentatives restantes : {max_tentatives - tentatives}")
    
    # Si le nombre maximum de tentatives est atteint
    if tentatives == max_tentatives:
        print("Accès refusé. Trop de tentatives échouées.")
