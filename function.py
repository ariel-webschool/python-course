# FUNCTION
# fonction qui affiche: une salutation a un utilisateur
print("#### FONCTION: SALUT UN UTILISATEUR")
def greet(first = "Inconnue"):
    print("hello "+first)
    
greet()
greet("Zeev")
greet("Jessica")

# BUT: afficher le resultat d'une addition
# fonction qui additionne 2 nombres et retourne la somme
print("#### FONCTION: ADDITIONNE DEUX NOMBRES")
def get_sum(num1,num2):
	print("Le calcul est: "+str(num1)+"+"+str(num2))
	return num1+num2

sum = get_sum(3,100)
print("Le resultat est : "+str(sum))


sum = get_sum(3,3)