age = int(input("Quelle est votre age? "))

if age >= 13:
	print("Vous pouvez voir le film, N'oubliez votre ticket.")
elif age > 0 and age < 13:
	print("Acces non autorisee, il vous manque " + str(13-age) + " annee(s) pour voir le film.")
else:
	print("Age non valide")

