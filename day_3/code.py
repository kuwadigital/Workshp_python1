"""
Exercice 1 : Créer et afficher différentes variables
	Exemple de vie courante : Informations personnelles
	Exemple de vie courante : Paramètres d'une recette de cuisine
	Exemple de vie courante : Détails d'un livre
	Exemple de vie courante : Caractéristiques d'une voiture
	Exemple de vie courante : Informations météorologiques
	Exemple de vie courante : Détails d'un film
	Exemple de vie courante : Informations sur un produit
	Exemple de vie courante : Coordonnées géographiques
	Exemple de vie courante : Détails d'un événement
	Exemple de vie courante : Paramètres d'un voyage
"""


# Exemple 1 : Informations personnelles
nom = "Alice"
age = 30
ville = "Paris"
print(f"Nom: {nom}, Age: {age}, Ville: {ville}")

# Exemple 2 : Paramètres d'une recette de cuisine
nom_recette = "Gâteau au chocolat"
temps_preparation = 20  # en minutes
temps_cuisson = 30  # en minutes
nombre_personnes = 8
print(f"Recette: {nom_recette}, Préparation: {temps_preparation} min, Cuisson: {temps_cuisson} min, Pour: {nombre_personnes} personnes")

# Exemple 3 : Détails d'un livre
titre_livre = "Le Petit Prince"
auteur = "Antoine de Saint-Exupéry"
nombre_pages = 96
print(f"Titre: {titre_livre}, Auteur: {auteur}, Pages: {nombre_pages}")

# Exemple 4 : Caractéristiques d'une voiture
marque = "Toyota"
modele = "Corolla"
annee = 2020
couleur = "Bleue"
print(f"Voiture: {marque} {modele}, Année: {annee}, Couleur: {couleur}")

# Exemple 5 : Informations météorologiques
temperature = 24.5  # en degrés Celsius
humidite = 60  # en pourcentage
vitesse_vent = 15  # en km/h
print(f"Température: {temperature}°C, Humidité: {humidite}%, Vent: {vitesse_vent} km/h")

# Exemple 6 : Détails d'un film
titre_film = "Inception"
realisateur = "Christopher Nolan"
duree = 148  # en minutes
print(f"Film: {titre_film}, Réalisateur: {realisateur}, Durée: {duree} minutes")

# Exemple 7 : Informations sur un produit
nom_produit = "Smartphone"
marque_produit = "Samsung"
prix = 599.99  # en euros
stock_disponible = 120
print(f"Produit: {nom_produit}, Marque: {marque_produit}, Prix: {prix}€, Stock: {stock_disponible}")

# Exemple 8 : Coordonnées géographiques
latitude = 48.8566
longitude = 2.3522
altitude = 35  # en mètres
print(f"Coordonnées: Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}m")

# Exemple 9 : Détails d'un événement
nom_evenement = "Concert de rock"
date = "2024-08-15"
lieu = "Stade de France"
print(f"Événement: {nom_evenement}, Date: {date}, Lieu: {lieu}")

# Exemple 10 : Paramètres d'un voyage
destination = "Japon"
duree_voyage = 14  # en jours
budget = 3000  # en euros
print(f"Voyage: Destination: {destination}, Durée: {duree_voyage} jours, Budget: {budget}€")



"""
Exercice 2 : Manipuler des variables (opérations arithmétiques)
	Exemple de vie courante : Calcul du budget mensuel
	Exemple de vie courante : Conversion des unités de mesure
	Exemple de vie courante : Calcul des scores de jeu
	Exemple de vie courante : Planification de projets
	Exemple de vie courante : Calcul de la distance parcourue
	Exemple de vie courante : Calcul des calories consommées
	Exemple de vie courante : Gestion des stocks
	Exemple de vie courante : Calcul des moyennes de notes
	Exemple de vie courante : Planification des vacances
	Exemple de vie courante : Gestion des dépenses quotidiennes
"""

# Exemple 1 : Calcul du budget mensuel
revenus = 2500  # en euros
loyer = 800
nourriture = 300
transport = 100
loisirs = 200
economies = revenus - (loyer + nourriture + transport + loisirs)
print(f"Économies mensuelles: {economies}€")

# Exemple 2 : Conversion des unités de mesure
pouces = 12
centimetres = pouces * 2.54
print(f"{pouces} pouces = {centimetres} cm")

# Exemple 3 : Calcul des scores de jeu
score_joueur1 = 150
score_joueur2 = 200
score_total = score_joueur1 + score_joueur2
print(f"Score total: {score_total}")

# Exemple 4 : Planification de projets
heures_travail = 40  # heures par semaine
semaines = 4
total_heures = heures_travail * semaines
print(f"Heures de travail totales pour le projet: {total_heures}")

# Exemple 5 : Calcul de la distance parcourue
vitesse = 60  # en km/h
temps = 2  # en heures
distance = vitesse * temps
print(f"Distance parcourue: {distance} km")

# Exemple 6 : Calcul des calories consommées
calories_petit_dejeuner = 300
calories_dejeuner = 600
calories_diner = 700
calories_totales = calories_petit_dejeuner + calories_dejeuner + calories_diner
print(f"Calories totales consommées: {calories_totales}")

# Exemple 7 : Gestion des stocks
stock_initial = 500
ventes = 120
stock_restant = stock_initial - ventes
print(f"Stock restant: {stock_restant}")

# Exemple 8 : Calcul des moyennes de notes
note1 = 15
note2 = 18
note3 = 14
moyenne = (note1 + note2 + note3) / 3
print(f"Moyenne des notes: {moyenne}")

# Exemple 9 : Planification des vacances
jours_vacances = 10
budget_total = 2000  # en euros
budget_jour = budget_total / jours_vacances
print(f"Budget par jour: {budget_jour}€")

# Exemple 10 : Gestion des dépenses quotidiennes
depenser_jour1 = 20
depenser_jour2 = 15
depenser_jour3 = 30
depenses_totales = depenser_jour1 + depenser_jour2 + depenser_jour3
print(f"Dépenses totales sur 3 jours: {depenses_totales}€")


"""
Exercice 3 : Concaténer des chaînes de caractères
	Exemple de vie courante : Salutation personnalisée
	Exemple de vie courante : Description de produit
	Exemple de vie courante : Création d'une adresse complète
	Exemple de vie courante : Création d'une invitation
	Exemple de vie courante : Création d'un message automatique
	Exemple de vie courante : Composition d'un titre
	Exemple de vie courante : Construction d'une phrase complexe
	Exemple de vie courante : Composition de statut sur les réseaux sociaux
	Exemple de vie courante : Génération de slogan publicitaire
	Exemple de vie courante : Création d'une signature email
"""
# Exemple 1 : Salutation personnalisée
prenom = "Alice"
message = "Bonjour, " + prenom + "!"
print(message)

# Exemple 2 : Description de produit
produit = "smartphone"
marque = "Samsung"
description = "Le " + produit + " de marque " + marque + " est maintenant disponible."
print(description)

# Exemple 3 : Création d'une adresse complète
rue = "123 Rue de la République"
ville = "Paris"
code_postal = "75001"
adresse_complete = rue + ", " + ville + ", " + code_postal
print(adresse_complete)

# Exemple 4 : Création d'une invitation
evenement = "fête"
date = "15 août"
invitation = "Vous êtes invité à la " + evenement + " qui aura lieu le " + date + "."
print(invitation)

# Exemple 5 : Création d'un message automatique
nom_utilisateur = "jdoe"
email = nom_utilisateur + "@example.com"
message_automatique = "Votre email est : " + email
print(message_automatique)

# Exemple 6 : Composition d'un titre
titre_principal = "Python"
sous_titre = "Apprendre la programmation"
titre_complet = titre_principal + " - " + sous_titre
print(titre_complet)

# Exemple 7 : Construction d'une phrase complexe
sujet = "Le chat"
action = "dort"
lieu = "sur le canapé"
phrase = sujet + " " + action + " " + lieu + "."
print(phrase)

# Exemple 8 : Composition de statut sur les réseaux sociaux
nom = "Alice"
activite = "en train de lire un livre"
statut = nom + " est " + activite + "."
print(statut)

# Exemple 9 : Génération de slogan publicitaire
produit = "Boisson Énergisante"
slogan = produit + " - Plus de force, plus d'énergie!"
print(slogan)

# Exemple 10 : Création d'une signature email
nom = "Alice Dupont"
poste = "Directrice Marketing"
signature = nom + "\n" + poste
print(signature)




"""
Exercice 4 : Travailler avec des listes
	Exemple de vie courante : Liste de courses
	Exemple de vie courante : Liste des tâches à faire
	Exemple de vie courante : Liste des invités
	Exemple de vie courante : Liste des destinations de voyage
	Exemple de vie courante : Liste des livres à lire
	Exemple de vie courante : Liste des films à regarder
	Exemple de vie courante : Liste des projets
	Exemple de vie courante : Liste des contacts
	Exemple de vie courante : Liste des courses pour un événement
	Exemple de vie courante : Liste des équipements sportifs
"""


# Exemple 1 : Liste de courses
courses = ["pommes", "bananes", "lait", "pain"]
print(courses)

# Exemple 2 : Liste des tâches à faire
taches = ["faire le ménage", "finir le rapport", "appeler le client"]
print(taches)

# Exemple 3 : Liste des invités
invites = ["Alice", "Bob", "Charlie", "Diane"]
print(invites)

# Exemple 4 : Liste des destinations de voyage
destinations = ["Paris", "New York", "Tokyo", "Sydney"]
print(destinations)

# Exemple 5 : Liste des livres à lire
livres = ["1984", "Le Seigneur des Anneaux", "Harry Potter"]
print(livres)

# Exemple 6 : Liste des films à regarder
films = ["Inception", "Interstellar", "Le Parfum"]
print(films)

# Exemple 7 : Liste des projets
projets = ["refaire le site web", "lancer la campagne marketing"]
print(projets)

# Exemple 8 : Liste des contacts
contacts = ["alice@example.com", "bob@example.com", "charlie@example.com"]
print(contacts)

# Exemple 9 : Liste des courses pour un événement
evenement_courses = ["boissons", "chips", "saucisses", "salades"]
print(evenement_courses)

# Exemple 10 : Liste des équipements sportifs
equipements = ["raquette de tennis", "ballon de football", "gants de boxe"]
print(equipements)


"""
Exercice 5 : Utiliser des variables booléennes
	Exemple de vie courante : Vérifier si une personne est majeure
	Exemple de vie courante : Vérifier si une tâche est terminée
	Exemple de vie courante : Vérifier si un produit est en stock
	Exemple de vie courante : Vérifier si une place est disponible
	Exemple de vie courante : Vérifier si un mot de passe est correct
	Exemple de vie courante : Vérifier si une condition météo est remplie
	Exemple de vie courante : Vérifier si un fichier existe
	Exemple de vie courante : Vérifier si une session est active
	Exemple de vie courante : Vérifier si une promotion est applicable
	Exemple de vie courante : Vérifier si une date est dans le futur
"""

# Exemple 1 : Vérifier si une personne est majeure
age = 20
est_majeur = age >= 18
print(f"Est majeur : {est_majeur}")

# Exemple 2 : Vérifier si une tâche est terminée
tache_terminee = True
print(f"Tâche terminée : {tache_terminee}")

# Exemple 3 : Vérifier si un produit est en stock
stock = 10
est_en_stock = stock > 0
print(f"Produit en stock : {est_en_stock}")

# Exemple 4 : Vérifier si une place est disponible
places_disponibles = 0
place_disponible = places_disponibles > 0
print(f"Place disponible : {place_disponible}")

# Exemple 5 : Vérifier si un mot de passe est correct
mot_de_passe = "1234"
mot_de_passe_correct = (mot_de_passe == "1234")
print(f"Mot de passe correct : {mot_de_passe_correct}")

# Exemple 6 : Vérifier si une condition météo est remplie
temperature = 22
est_chaud = temperature > 20
print(f"Il fait chaud : {est_chaud}")

# Exemple 7 : Vérifier si un fichier existe
fichier_existe = True
print(f"Fichier existe : {fichier_existe}")

# Exemple 8 : Vérifier si une session est active
session_active = False
print(f"Session active : {session_active}")

# Exemple 9 : Vérifier si une promotion est applicable
prix_achat = 50
promotion_applicable = prix_achat >= 50
print(f"Promotion applicable : {promotion_applicable}")

# Exemple 10 : Vérifier si une date est dans le futur
import datetime
date_actuelle = datetime.date.today()
date_evenement = datetime.date(2024, 8, 15)
date_future = date_evenement > date_actuelle
print(f"Date dans le futur : {date_future}")
