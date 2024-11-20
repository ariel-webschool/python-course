# CONDITIONS
# LOGIQUE

number = 1001

if number > 4:
    print('Je suis superieur a 4')

if number < 8:
    print('Je suis inferieur a 8')
    
if number > 0 and number < 8: # CONDITION1=True + CONDITION2=True = True
    print("Je suis entre 0 et 8")
    
if number > 0 or number < 8: # CONDITION1=TRUE | CONDITION1=False, alors il verifie la deuxieme condition
    print("Je suis superieur a 0 OU inferieur a 8")