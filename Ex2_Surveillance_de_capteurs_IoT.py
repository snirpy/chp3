import random

# Nombre de lectures du capteur
n = 10

# Seuil de température (en degrés Celsius) pour déclencher une alerte
seuil_temperature = 35

# Simuler des valeurs de température envoyées par un capteur IoT
print("Collecte des données de température :")
for i in range(n):
    # Générer une température aléatoire entre 20 et 40 degrés Celsius
    temperature = random.uniform(20, 40)
    
    # Afficher la température
    print(f"Température mesurée : {temperature:.2f}°C")
    
    # Vérifier si la température dépasse le seuil
    if temperature > seuil_temperature:
        print(f"ALERTE : Température élevée détectée ({temperature:.2f}°C) !")
    else:
        print("Température normale.")
    
    print("-" * 30)  # Séparateur visuel entre les lectures
