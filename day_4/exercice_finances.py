montant_salaire = input("Entrez votre salaire :  ")
facture_assurance = input("Entrez votre facutre d'assurance :  ")
facture_loyer = input("Entrez votre facutre du loyer :  ")
facture_tel = input("Entrez votre facutre de tel :  ")
business_extra = input("Entrez vos extras :  ")

"""
input enregistre toujours les valeurs comme du texte: dans certains cas il va falloir convertir

text -----> convertir ----> entier/(decimaux)floatant
                            int()/float()
"""

# reste_disponible = montant_salaire - facture_assurance - facture_loyer - facture_tel + business_extra
reste_disponible = int(montant_salaire) - int(facture_assurance) - int(facture_loyer) - float(facture_tel) + int(business_extra)

print("Finance restant: ", reste_disponible)