Voici 10 énoncés complexes où l'utilisation de toutes les structures de contrôle (`if`, `elif`, `else`) ainsi que des imbrications sera nécessaire :

1. **Calcul de l'impôt sur le revenu**
   - Énoncé : Écrivez un programme qui calcule l'impôt sur le revenu selon les tranches suivantes :
     - Si le revenu est inférieur à 10 000 €, l'impôt est de 0 %.
     - Si le revenu est entre 10 000 € et 20 000 €, l'impôt est de 10 % pour la partie excédant 10 000 €.
     - Si le revenu est entre 20 000 € et 40 000 €, l'impôt est de 15 % pour la partie excédant 20 000 €.
     - Si le revenu est supérieur à 40 000 €, l'impôt est de 20 % pour la partie excédant 40 000 €.
   - Solution :
     ```python
     revenu = 45000
     impot = 0

     if revenu <= 10000:
         impot = 0
     elif revenu <= 20000:
         impot = (revenu - 10000) * 0.1
     elif revenu <= 40000:
         impot = (20000 - 10000) * 0.1 + (revenu - 20000) * 0.15
     else:
         impot = (20000 - 10000) * 0.1 + (40000 - 20000) * 0.15 + (revenu - 40000) * 0.2

     print(f"L'impôt est de {impot} €")
     ```

2. **Calcul de la note finale d'un étudiant**
   - Énoncé : Calculez la note finale d'un étudiant selon les critères suivants :
     - Si la moyenne des devoirs est inférieure à 40 %, l'étudiant échoue automatiquement.
     - Sinon, si la moyenne des devoirs est entre 40 % et 60 %, l'examen final doit être au moins de 60 % pour réussir.
     - Si la moyenne des devoirs est supérieure à 60 %, l'examen final doit être au moins de 50 % pour réussir.
   - Solution :
     ```python
     moyenne_devoirs = 65
     examen_final = 55

     if moyenne_devoirs < 40:
         print("Échec automatique")
     elif moyenne_devoirs <= 60:
         if examen_final >= 60:
             print("Réussi")
         else:
             print("Échec")
     else:
         if examen_final >= 50:
             print("Réussi")
         else:
             print("Échec")
     ```

3. **Calcul du prix des billets de cinéma avec réductions**
   - Énoncé : Calculez le prix des billets selon les critères suivants :
     - Le prix de base est de 12 €.
     - Si le client a moins de 18 ans ou plus de 65 ans, il obtient une réduction de 50 %.
     - Si le client achète plus de 3 billets, il obtient une réduction de 10 % sur le total.
   - Solution :
     ```python
     age = 17
     nombre_billets = 4
     prix_base = 12
     prix_total = prix_base * nombre_billets

     if age < 18 or age > 65:
         prix_total *= 0.5

     if nombre_billets > 3:
         prix_total *= 0.9

     print(f"Le prix total est de {prix_total} €")
     ```

4. **Sélection d'un plan d'abonnement pour un utilisateur**
   - Énoncé : Sélectionnez un plan d'abonnement selon les critères suivants :
     - Si l'utilisateur a plus de 50 Go de données à stocker, choisissez le plan "Premium".
     - Si l'utilisateur a entre 20 et 50 Go de données, choisissez le plan "Standard".
     - Si l'utilisateur a moins de 20 Go de données, choisissez le plan "Basic".
     - Si l'utilisateur souhaite un plan avec des fonctionnalités supplémentaires, ajoutez 10 € au prix du plan.
   - Solution :
     ```python
     donnees = 30
     fonctionnalites_suppl = True
     plan = ""
     prix = 0

     if donnees > 50:
         plan = "Premium"
         prix = 20
     elif donnees >= 20:
         plan = "Standard"
         prix = 15
     else:
         plan = "Basic"
         prix = 10

     if fonctionnalites_suppl:
         prix += 10

     print(f"Plan choisi : {plan}, Prix : {prix} €")
     ```

5. **Sélection d'une assurance pour une voiture**
   - Énoncé : Sélectionnez un plan d'assurance selon les critères suivants :
     - Si la voiture a moins de 5 ans, choisissez "Plan A".
     - Si la voiture a entre 5 et 10 ans, choisissez "Plan B".
     - Si la voiture a plus de 10 ans, choisissez "Plan C".
     - Si le conducteur a plus de 25 ans et moins de 65 ans, une réduction de 20 % est appliquée.
   - Solution :
     ```python
     age_voiture = 8
     age_conducteur = 30
     plan = ""
     prix = 0

     if age_voiture < 5:
         plan = "Plan A"
         prix = 500
     elif age_voiture <= 10:
         plan = "Plan B"
         prix = 400
     else:
         plan = "Plan C"
         prix = 300

     if age_conducteur > 25 and age_conducteur < 65:
         prix *= 0.8

     print(f"Plan choisi : {plan}, Prix : {prix} €")
     ```

6. **Évaluation d'une candidature à un emploi**
   - Énoncé : Évaluez une candidature selon les critères suivants :
     - Si le candidat a plus de 5 ans d'expérience et une maîtrise, il est "Fortement recommandé".
     - Si le candidat a plus de 5 ans d'expérience mais pas de maîtrise, il est "Recommandé".
     - Si le candidat a entre 2 et 5 ans d'expérience et une licence, il est "Considéré".
     - Sinon, il est "Non recommandé".
   - Solution :
     ```python
     experience = 6
     diplome = "maîtrise"
     evaluation = ""

     if experience > 5:
         if diplome == "maîtrise":
             evaluation = "Fortement recommandé"
         else:
             evaluation = "Recommandé"
     elif experience >= 2:
         if diplome == "licence":
             evaluation = "Considéré"
         else:
             evaluation = "Non recommandé"
     else:
         evaluation = "Non recommandé"

     print(f"Évaluation : {evaluation}")
     ```

7. **Détermination du niveau d'urgence d'un patient**
   - Énoncé : Déterminez le niveau d'urgence selon les critères suivants :
     - Si le patient a une douleur sévère et une température supérieure à 38,5°C, le niveau est "Urgence Critique".
     - Si le patient a une douleur modérée et une température entre 37°C et 38,5°C, le niveau est "Urgence".
     - Si le patient a une douleur légère et une température inférieure à 37°C, le niveau est "Non Urgent".
   - Solution :
     ```python
     douleur = "modérée"
     temperature = 38

     if douleur == "sévère":
         if temperature > 38.5:
             niveau_urgence = "Urgence Critique"
         else:
             niveau_urgence = "Urgence"
     elif douleur == "modérée":
         if temperature >= 37 and temperature <= 38.5:
             niveau_urgence = "Urgence"
         else:
             niveau_urgence = "Non Urgent"
     else:
         if temperature < 37:
             niveau_urgence = "Non Urgent"
         else:
             niveau_urgence = "Urgence"

     print(f"Niveau d'urgence : {niveau_urgence}")
     ```

8. **Attribution d'un logement étudiant**
   - Énoncé : Attribuez un logement étudiant selon les critères suivants :
     - Si l'étudiant est en première année et a des revenus inférieurs à 10 000 €, attribuez un logement "Résidence A".
     - Si l'étudiant est en deuxième année et a des revenus entre 10 000 € et 20 000 €, attribuez un logement "Résidence B".
     - Si l'étudiant est en troisième année et a des revenus supérieurs à 20 000 €, attribuez un logement "Résidence C".
     - Si l'étudiant a un handicap, attribuez automatiquement un logement "Résidence Accessible".
   - Solution :
     ```python
     annee_etudes = 1
     revenus = 9000
     handicap = False
     residence = ""

     if handicap:
         residence = "Résidence Accessible"
     elif annee_etudes == 1:
         if revenus < 10000:
             residence = "Résidence A"
         else:
             residence = "Autre Résidence"
     elif annee_etudes == 2:
         if revenus <= 20000:
             residence = "Résidence B"
         else:
             residence = "

Autre Résidence"
     elif annee_etudes == 3:
         if revenus > 20000:
             residence = "Résidence C"
         else:
             residence = "Autre Résidence"

     print(f"Résidence attribuée : {residence}")
     ```

9. **Configuration des paramètres de notification**
   - Énoncé : Configurez les paramètres de notification selon les critères suivants :
     - Si l'utilisateur est en ligne, activez toutes les notifications.
     - Si l'utilisateur est hors ligne, activez uniquement les notifications critiques.
     - Si l'utilisateur est en mode "Ne pas déranger", désactivez toutes les notifications.
     - Si l'utilisateur a activé les notifications de nuit et est entre 22h et 7h, désactivez les notifications non critiques.
   - Solution :
     ```python
     etat_utilisateur = "en ligne"
     heure = 23
     notifications_nuit = True

     if etat_utilisateur == "en ligne":
         notifications = "Toutes les notifications activées"
     elif etat_utilisateur == "hors ligne":
         if notifications_nuit and (heure >= 22 or heure < 7):
             notifications = "Seules les notifications critiques sont activées"
         else:
             notifications = "Notifications critiques activées"
     elif etat_utilisateur == "ne pas déranger":
         notifications = "Toutes les notifications désactivées"

     print(f"Paramètres de notification : {notifications}")
     ```

10. **Détermination du statut d'un vol**
    - Énoncé : Déterminez le statut d'un vol selon les critères suivants :
      - Si le vol est à l'heure, affichez "À l'heure".
      - Si le vol est retardé de moins de 30 minutes, affichez "Retardé de moins de 30 minutes".
      - Si le vol est retardé entre 30 et 60 minutes, affichez "Retardé de 30 à 60 minutes".
      - Si le vol est retardé de plus de 60 minutes, affichez "Retardé de plus de 60 minutes".
      - Si le vol est annulé, affichez "Vol annulé".
    - Solution :
      ```python
      statut_vol = "retardé"
      retard_minutes = 45

      if statut_vol == "à l'heure":
          statut = "À l'heure"
      elif statut_vol == "retardé":
          if retard_minutes < 30:
              statut = "Retardé de moins de 30 minutes"
          elif retard_minutes <= 60:
              statut = "Retardé de 30 à 60 minutes"
          else:
              statut = "Retardé de plus de 60 minutes"
      elif statut_vol == "annulé":
          statut = "Vol annulé"

      print(f"Statut du vol : {statut}")
      ```