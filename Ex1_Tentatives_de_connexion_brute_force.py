# Utilisateur correct prédéfini
utilisateur_correct = "admin"

# Nombre maximum de tentatives
max_tentatives = 3

# Compteur de tentatives
tentatives = 0

# Boucle pour les tentatives de connexion
while tentatives < max_tentatives:
    utilisateur = input("Entrez le nom d'utilisateur : ")
    
    if utilisateur == utilisateur_correct:
        print("Connexion réussie!")
        break  # Arrête la boucle si l'utilisateur est correct
    else:
        tentatives += 1
        print(f"Nom d'utilisateur incorrect. Tentative {tentatives}/{max_tentatives}")
    
    if tentatives == max_tentatives:
        print("Trop de tentatives infructueuses. Connexion refusée.")
