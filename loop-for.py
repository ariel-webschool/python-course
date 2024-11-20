# FONCTIONS RANGE

print("##### RANGE FUNCTION:")
arr=range(0,10)

# print(arr[0]) # affiche 0
# print(arr[9]) # affiche 9

print("##### LOOP:")
# LES BOUCLES
# FOR
for index in range(0,10): # for index in [0,1,2,3,4,5,6,7,8,9]:
    print("hello")


# Parcourir un tableau de nom
names=["Ariel","Zeev","David","Chai","Jordan","Aurelie","Jessica"]
print(len(names))

# name = "Ariel" # premier fois
# name = "Zeev" # deuxieme fois
# name = "David" # Troisieme fois

# 1ere maniere
print("#### 1ere maniere")
for name in names:
    print(name)

# 2em maniere
print("#### 2em maniere")    
for index in range(0,len(names)):
    print(names[index])

