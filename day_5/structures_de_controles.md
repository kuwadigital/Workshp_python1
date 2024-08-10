### Slide 1 : La Structure `if`

#### Exemple 1 : Vérification de l'âge pour l'entrée dans un club
**Énoncé :** Vérifiez si une personne a l'âge requis pour entrer dans un club. Si l'âge est supérieur ou égal à 18, affichez "Accès autorisé".

**Code :**
```python
age = 20
if age >= 18:
    print("Accès autorisé")
```
**Explication :** Ici, on vérifie simplement si l'âge est suffisant pour accéder au club.

#### Exemple 2 : Détection de la température pour allumer le chauffage
**Énoncé :** Si la température extérieure est inférieure à 15 degrés, allumez le chauffage.

**Code :**
```python
temperature = 10
if temperature < 15:
    print("Allumer le chauffage")
```
**Explication :** Si la température est trop basse, on allume le chauffage.

#### Exemple 3 : Vérification du niveau de batterie
**Énoncé :** Si le niveau de la batterie de votre téléphone est inférieur à 20%, affichez "Batterie faible".

**Code :**
```python
batterie = 15
if batterie < 20:
    print("Batterie faible")
```
**Explication :** On prévient l'utilisateur que la batterie est faible.

#### Exemple 4 : Vérification des stocks en magasin
**Énoncé :** Si le stock d'un produit est inférieur à 10 unités, affichez "Réapprovisionnement nécessaire".

**Code :**
```python
stock = 5
if stock < 10:
    print("Réapprovisionnement nécessaire")
```
**Explication :** Si le stock est bas, on alerte pour réapprovisionner.

#### Exemple 5 : Vérification de la vitesse d'un véhicule
**Énoncé :** Si la vitesse d'un véhicule dépasse 80 km/h, affichez "Vous êtes en excès de vitesse".

**Code :**
```python
vitesse = 85
if vitesse > 80:
    print("Vous êtes en excès de vitesse")
```
**Explication :** On alerte le conducteur qu'il dépasse la vitesse autorisée.

### Slide 2 : La Structure `elif`

#### Exemple 1 : Choix d'une activité selon la météo
**Énoncé :** Si le temps est ensoleillé, affichez "Allons à la plage". Si le temps est nuageux, affichez "Allons au musée".

**Code :**
```python
meteo = "nuageux"
if meteo == "ensoleillé":
    print("Allons à la plage")
elif meteo == "nuageux":
    print("Allons au musée")
```
**Explication :** On choisit une activité en fonction de la météo.

#### Exemple 2 : Sélection d'un moyen de transport selon la distance
**Énoncé :** Si la distance est inférieure à 1 km, affichez "Marche". Si la distance est entre 1 et 5 km, affichez "Vélo".

**Code :**
```python
distance = 3
if distance < 1:
    print("Marche")
elif distance <= 5:
    print("Vélo")
```
**Explication :** On choisit un moyen de transport adapté à la distance.

#### Exemple 3 : Choix d'une tenue selon la température
**Énoncé :** Si la température est supérieure à 25 degrés, affichez "T-shirt". Si elle est entre 15 et 25 degrés, affichez "Pull léger".

**Code :**
```python
temperature = 20
if temperature > 25:
    print("T-shirt")
elif temperature >= 15:
    print("Pull léger")
```
**Explication :** On adapte la tenue à la température.

#### Exemple 4 : Détection de la taille d'un fichier pour le stockage
**Énoncé :** Si la taille du fichier est inférieure à 100 Mo, affichez "Stocker en local". Si elle est entre 100 Mo et 1 Go, affichez "Stocker sur le cloud".

**Code :**
```python
taille_fichier = 150
if taille_fichier < 100:
    print("Stocker en local")
elif taille_fichier <= 1000:
    print("Stocker sur le cloud")
```
**Explication :** On choisit un mode de stockage selon la taille du fichier.

#### Exemple 5 : Répartition d'un budget selon le montant
**Énoncé :** Si le budget est inférieur à 500 €, affichez "Achetez des fournitures". Si le budget est entre 500 € et 1000 €, affichez "Achetez des équipements".

**Code :**
```python
budget = 750
if budget < 500:
    print("Achetez des fournitures")
elif budget <= 1000:
    print("Achetez des équipements")
```
**Explication :** On gère les achats selon le budget disponible.

### Slide 3 : La Structure `else`

#### Exemple 1 : Évaluation d'un examen
**Énoncé :** Si la note est supérieure ou égale à 90, affichez "Grade A". Si elle est entre 80 et 89, affichez "Grade B". Sinon, affichez "Grade C".

**Code :**
```python
note = 75
if note >= 90:
    print("Grade A")
elif note >= 80:
    print("Grade B")
else:
    print("Grade C")
```
**Explication :** On évalue la performance de l'étudiant selon sa note.

#### Exemple 2 : Détection de l'état de charge d'une batterie
**Énoncé :** Si la charge de la batterie est supérieure à 80%, affichez "Batterie pleine". Si elle est entre 20% et 80%, affichez "Batterie moyenne". Sinon, affichez "Batterie faible".

**Code :**
```python
charge_batterie = 15
if charge_batterie > 80:
    print("Batterie pleine")
elif charge_batterie >= 20:
    print("Batterie moyenne")
else:
    print("Batterie faible")
```
**Explication :** On affiche l'état de la batterie selon son niveau de charge.

#### Exemple 3 : Sélection d'une activité de loisir selon l'heure
**Énoncé :** Si l'heure est inférieure à 12, affichez "Allons courir". Si elle est entre 12 et 18, affichez "Allons au cinéma". Sinon, affichez "Allons dîner".

**Code :**
```python
heure = 19
if heure < 12:
    print("Allons courir")
elif heure < 18:
    print("Allons au cinéma")
else:
    print("Allons dîner")
```
**Explication :** On choisit une activité de loisir en fonction de l'heure.

#### Exemple 4 : Choix de la tenue vestimentaire selon la météo
**Énoncé :** Si la météo est ensoleillée, affichez "Portez des lunettes de soleil". Si elle est nuageuse, affichez "Prenez un parapluie". Sinon, affichez "Habillez-vous chaudement".

**Code :**
```python
meteo = "neige"
if meteo == "ensoleillé":
    print("Portez des lunettes de soleil")
elif meteo == "nuageux":
    print("Prenez un parapluie")
else:
    print("Habillez-vous chaudement")
```
**Explication :** On adapte la tenue à la météo.

#### Exemple 5 : Choix d'un mode de transport selon le trafic
**Énoncé :** Si le trafic est faible, affichez "Prenez la voiture". Si le trafic est modéré, affichez "Prenez le vélo". Sinon, affichez "Prenez les transports en commun".

**Code :**
```python
trafic = "élevé"
if trafic == "faible":
    print("Prenez la voiture")
elif trafic == "modéré":
    print("Prenez le vélo")
else:
    print("Prenez les transports en commun")
```
**Explication :** On choisit un mode de transport selon l'état du trafic.
