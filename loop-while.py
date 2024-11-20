# Boolean
is_finished = True

# LOOP - BOUCLE
# while condition: # elle est vrai: True
#	print("affiche ce message tant que condition est False")

# Parcourir une liste de numero de 0, jusqu'a 5
print("#### LOOP WHILE THROUGH 0 TO 5:")
index=0
while index < 5: 
    print(index)
    index = index + 1 # augmente de 1

# A quoi est egale index ?
print("#### RESULTAT FINAL APRES LA BOUCLE")
print(index)


# Parcourir une liste de numero de 0, jusqu'a 5, sachant qu'au deuxieme chiffre impaire il sort de la boucle
print("#### LOOP WHILE THROUGH 0 TO 5 BUT EXIT FROM THE LOOP WHEN ARRIVED ON SECOND ODD NUMBER:")
index=0
counter=0
while index < 5 and counter < 2: 
    print(index)
    index = index + 1
    if index % 2 != 0: # c'est impaire ?
        counter = counter + 1

# affiche le second nombre impaire
print("#### AFFICHE LE SECOND NOMBRE IMPAIRE")
print(index)


