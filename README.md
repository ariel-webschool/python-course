![Image](./image.png)

## 🌟 Table des matières

1. [Les Bases des Fonctions Python](#-1-les-bases-des-fonctions-python)
2. [Conversion des types (Casting)](#-2-conversion-des-types-casting)
3. [Variables](#-3-variables)
4. [Commentaires](#-4-commentaires)
5. [Conditions (IF/ELSE)](#-5-conditions-ifelse)
6. [Exercices pratiques](#-6-exercices-pratiques)
7. [Tableaux (listes)](#-7-tableaux-listes)
8. [Tuples (listes constantes)](#-8-tuples-listes-constantes)
9. [Sets (listes sans doublon)](#-9-sets-listes-sans-doublon)
10. [Dictionaries (liste clé : valeur)](#-10-dictionaries-liste-clé--valeur)
11. [Classes/Objects | Introduction à l'orienté-objet](#-11-classesobjects--introduction-à-lorienté-objet)
12. [Gestion des fichiers](#-12-gestion-des-fichiers)
13. [JSON (JavaScript Object Notation)](#-13-json-javascript-object-notation)
14. [Gestion des Exceptions avec `try-except`](#-14-gestion-des-exceptions-avec-try-except)

---


## 🌟 1. Les Bases des Fonctions Python

### 📌 Affichage et interactions utilisateur
```python
print("Hello, Python!") # Afficher un message
```

- **`print()`** : Sert à afficher des informations dans la console.

```python
nom = input("Quel est ton nom ? ")  # Récupérer des données de l'utilisateur
print("Bonjour, " + nom + " !")
```

- **`input()`** : Permet à l'utilisateur de saisir des données (toujours retournées sous forme de chaîne).

### 📌 Vérification du type d'une donnée
```python
age = 25
print(type(age))  # <class 'int'>
```

- **`type()`** : Indique le type d'une variable (int, str, float, etc.).

---

## 🌟 2. Conversion des types (Casting)
Python permet de convertir les types grâce à des fonctions appelées *casting* :
- **`int()`** : Convertir en entier.  
- **`float()`** : Convertir en décimal.  
- **`str()`** : Convertir en chaîne de caractères.

### Exemples :
```python
# Conversion de types
nombre = "42"
print(int(nombre))  # Convertir une chaîne en entier
print(float(nombre))  # Convertir une chaîne en nombre décimal

# Combinaison
age = 25
print("J'ai " + str(age) + " ans.")  # Conversion pour concaténation
```

---

## 🌟 3. Variables

### 📌 Règles pour nommer une variable :
1. Doit commencer par une lettre ou un underscore (`_`).  
2. Peut contenir des chiffres, mais ne doit **pas** commencer par un chiffre.  
3. Doit être unique dans un programme.

### Exemples :
```python
# Déclaration de variables
nom = "Alice"
age = 30
pi = 3.14

print(nom, age, pi)
```

---

## 🌟 4. Commentaires
Les commentaires sont ignorés par Python mais utiles pour documenter ton code :
```python
# Ceci est un commentaire sur une seule ligne.

"""
Ceci est un commentaire
multiligne.
"""
```

---

## 🌟 5. Conditions (IF/ELSE)

### 📌 Structure :
```python
if condition:
    # Bloc de code si la condition est vraie
elif autre_condition:
    # Bloc si l'autre condition est vraie
else:
    # Bloc si aucune condition n'est vraie
```

### Exemple :
```python
age = 20

if age >= 60:
    print("Vous êtes senior.")
elif age >= 18:
    print("Vous êtes adulte.")
else:
    print("Vous êtes mineur.")
```

---

## 🌟 6. Exercices pratiques

### 🔹 **Exercice 1 : Présentation**
Écrivez un programme qui demande à l'utilisateur :
- Son nom
- Son âge

Puis affiche : `Bonjour <nom>, vous avez <âge> ans.`

<details>
<summary>Solution</summary>

```python
nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")
print("Bonjour " + nom + ", vous avez " + age + " ans.")
```
</details>

---

### 🔹 **Exercice 2 : Accès au cinéma**
Demandez à l'utilisateur son âge et dites-lui s'il peut regarder un film d'horreur (âge minimum : 13 ans). Si non, précisez combien d'années il doit attendre.

**Solution**

```python
age = int(input("Quel est votre âge ? "))

if age >= 13:
    print("Autorisé à voir le film.")
else:
    print("Accès interdit, il vous manque " + str(13 - age) + " ans.")
```

---

## 🌟 7. Tableaux (listes)

Les tableaux permettent de stocker plusieurs valeurs dans une seule variable.  
**Exemple :**
```python
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])  # pomme
print(len(fruits))  # Nombre d'éléments : 3
```

### 📌 Obtenir le nombre d'éléments dans une liste
```python
nombres = [10, 20, 30]
print(len(nombres))  # 3
```

### 📌 Changer d'élément dans une liste existante:

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits[0] = "strawberry"
```

### 📌 Remplacer une sous liste d'élément par une autre list:

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits[0:2] = ["strawberry","grappe"]
```

### 📌 Insérer un élément dans une liste a l'index-K:

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits.insert(0,"watermelon")
print(fruits)

# ["watermelon", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
```


### 📌 Ajouter un élément a la fin d'une liste:

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits.append("peach")
print(fruits)

# ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","peach"]
```

### 📌 Ajouter et concatener une liste, Ajouter une autre liste dans la liste actuelle:
```python
fruits = ['watermelon', 'strawberry', 'grappe', 'watermelon', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'peach']
fruits.extend( ["tomato","avocado"] )
print(fruits)
# ['watermelon', 'strawberry', 'grappe', 'watermelon', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'peach', 'tomato', 'avocado']
```

### 📌 Supprimer un element de la liste actuelle avec sa valeur:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
fruits.remove("strawberry")
print(fruits)
# ['watermelon', 'grappe']
```


### 📌 Supprimer un element de la liste actuelle avec sa cle:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
fruits.pop(1)
print(fruits)
# ['watermelon', 'grappe']
```

alternative

```python
fruits = ['watermelon', 'strawberry', 'grappe']
del fruits[1]
print(fruits)
# ['watermelon', 'grappe']
```

### 📌 Supprimer le derniere element de la liste actuelle:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
fruits.pop()
print(fruits)
# ['watermelon', 'strawberry']
```

### 📌 Supprimer une liste:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
del fruits
print(fruits)
# Not Defined
```

### 📌 Vide une liste:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
fruits.clear()
print(fruits)
# result: []
```


### 📌 Boucler sur un tableau sur chaque valeur:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
# foreach
for fruit in fruits:
    print("Le fruit actuelle est le: "+fruit)
# result: []
```


### 📌 Boucler sur un tableau a partir de l'index:
```python
fruits = ['watermelon', 'strawberry', 'grappe']
# for
for index in range(0,len(fruits)):
    print("Le fruit actuelle est le: "+fruits[index])
# result: []
```


"salut" = ["s","a","l","u","t"]

### 📌 Trier un tableau numeric:
```python
nums = [9,6,3,6,7]
nums.sort()
print(nums)
# result: [3,6,6,7,9]
```

### 📌 Recuperer l'index d'un élément dans une liste
```python
nombres = [10, 20, 30]
print(nombres.index(20))  # 1
```

### 📌 Copy d'une liste en profondeur
ERREUR A NE PAS FAIRE
```python
# un tableau qui pointe sur le meme tableau manipule les memes donnees
# manipuler (modifier un element, supprimer un element)
nombres = [10, 20, 30]
nombres_2 = nombres
nombres_2[0] = 1000
print(nombres) # [1000, 20, 30]
print(nombres_2) # [1000, 20, 30]
```
Voici comment faire une copie de tableau pour le manipuler sous une autre forme.

```python
nombres = [10, 20, 30]
nombres_2 = nombres.copy()
nombres_2[0] = 1000
print(nombres)  # [10, 20, 30]
print(nombres_2)  # [1000, 20, 30]
```

### 📌 Extraire une liste d'élément a partir d'une autre liste
```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

nouvelle_list_1 = fruits[2:5] # ["cherry", "orange", "kiwi"]
nouvelle_list_2 = fruits[2:] # ["cherry", "orange", "kiwi", "melon", "mango"]
nouvelle_list_3 = fruits[:2] # ["apple", "banana"]
```

### 📌 Verifier si un élément existe dans la liste:
```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if "apple" in fruits:
    print("Ce fruit existe dans notre liste")
else:
    print("Ce fruit n'existe pas dans notre liste")
```


```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

user_input = input("Which fruits is in the list? ")
if user_input.lower() in fruits:
    print("Ce fruit existe dans notre liste")
else:
    print("Ce fruit n'existe pas dans notre liste")
```

### 📌 Itération dans une liste :
```python
for fruit in fruits:
    print(fruit)
```
### 📌 Recap: toutes les fonctions possible sur une liste:
```python
**Method**	**Description**
append()	# Ajout element a la fin de la liste
clear()	    # Vide la liste
copy()	    # Retourne une copy de la liste
count()	    # Recupere le nombre de fois ou un element est present dans le tableau
extend()	# Combine deux liste
index()	    # Retourne l'index d'une valeur
insert()	# Ajoute un element a la position souhaite
pop()	    # Supprime un element a une position
remove()	# Supprime un element qui matche la valeur
reverse()	# Renverse l'ordre de la liste
sort()	    # Trie une liste, et la garde trier
```
---

## 🌟 8. Tuples (listes constantes)

### 📌 Simple declaration
```python
fruits = ['banana','melon','watermelon']
fruits_permanents = tuple(fruits[0:2])
# fruits_permanents est une variable de type list et constant => tuple (inalterable)
```

### 📌 Destructuring - Destructuration
```python
fruits = ['banana','melon','watermelon']
fruits_permanents = tuple(fruits[0:2])
(banana, melon) = fruits_permanents
print(banana) # banana

(x, y) = fruits_permanents
print(x) # banana
```
---
## 🌟 9. Sets (listes sans doublon)
Cette structure de donnee ne permet pas les doublons.

### 📌 Simple declaration
```python
fruits = ['banana','peach','mango','banana']
fruits_once = set(fruits)
print(fruits_once) # ('banana','peach','mango')
```
### 📌 Ajout
```python
mon_set = {1, 2, 3}
mon_set.add(4)  # Ajoute 4 au set
print(mon_set)  # {1, 2, 3, 4}
```
### 📌 Suppression
```python
mon_set = {1, 2, 3}
mon_set.remove(2)  # Supprime 2
print(mon_set)  # {1, 3}
```
---
## 🌟 10. Dictionary (liste cle : valeur)

### 📌 Simple declaration
```python
# un tableau avec cle et valeur
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car = {year: 1969}
car = dict(year:1969
)
```

### 📌 Acces a une valeur (dictionnaire)
```python
print(car['brand']) # Ford
print(car.get('brand')) # Ford
```

### 📌 Recuperer la liste des cles (dictionnaire)
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
k = car.keys()
print(k) # ['brand','model','year']
```

### 📌 Recuperer la liste des valeurs (dictionnaire)
```python
v = car.values()
print(v) # ["Ford","Mustang","1969"]
```

### 📌 Modifier une valeur (dictionnaire)
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["brand"] = "Mitsubichi"
print(car.values()) # ["Mitsubichi","Mustang","1969"]
```

### 📌 Modifier plusieurs valeurs en une fois (dictionnaire)
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
modif = {"brand":"Mitsubichi","year": 2020}
car.update(modif)
# car.update({"brand":"Mitsubichi","year": 2020})
print(car.values()) # ["Mitsubichi","Mustang","2020"]
```

### 📌 Supprimer un element a partir d'une cle (dictionnaire)
```python
car.pop('model')
# { "year": 2020, "brand": "Mitsubichi"}
```

### 📌 Supprimer le derniere element (dictionnaire)
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.popitem()
# { "brand": "Ford", "model": "Mustang" }
```
---

## 🌟 11. Classes/Objects | Introduction a l'oriente-objet

### 📌 Declaration d'une classe (prototypage et referencement)
```python
class Car:
    brand = "Toyota" # par defaut la marque sera toyota
```

### 📌 Instanciation, Creation
```python
car = Car() # instanciation de notre prototype
print(car.brand) # afficher la marque de notre fameuse voiture creer
```

### 📌 Constructeur: def __init__(self,...):
est la pour construire l'objet, de maniere individuel

```python
class Car:
    id = 0 # par defaut c'est 0
    brand = "Toyota" # par defaut la marque toyota

    # Method, Function
    def __init__(self, brand, id):
        self.id = id
        self.brand = brand
        print('Creation de la voiture')

    def setBrand(self, brand):
        self.brand = brand
```

### 📌 Identite de l'objet: def __str__(self,...):
```python
class Car:
    id = 0 # par defaut c'est 0
    brand = "Toyota" # par defaut la marque toyota
    km = 0

    # Method, Function
    def __init__(self, brand, id):
        self.id = id
        self.brand = brand
        print('Creation de la voiture')

    def __str__(self):
        print(f"Je suis une voiture de type {self.brand} numero #{self.id}")

    def drive(self,km):
        self.km = self.km + km
        print(f"Vous avez roulez {self.km}km.")
    
```

### 📌Exercice
### Creer une personne:
    -  name
    -  age
    -  une fonction qui presente la personne
    -  une fonction qui permet a la personne d'apprendre -> apprendre(self,study)
        - on accumule les connaissance, ex:
            zeev.apprend("Violon")
            zeev.apprend("Piloter un avion")
    -  une fonction qui affiche tout ce qu'elle a etudier
            zeev.aAppris()  # Violon
                            # Piloter un avion

**Correction**
```python
class Person:

    # functions
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.matters = []
        print(f"{name} vient de naitre, mais il a quand meme {age} ans")

    def greet(self):
        print(f"Je m'appel {self.name}, et j'ai {self.age} ans.")

    def learned(self, matter):
        self.matters.append(matter)
        print(f"{self.name} a appris {matter}")

    def have_learned(self):
        if len(self.matters) > 0:
            for m in self.matters: # foreach
                print(f"\t{m}")
```

```python
# implementation
zeev = Person("Zeev",30)
zeev.greet()
zeev.learned("HTML")
zeev.learned("CSS")
zeev.learned("Javascript")
zeev.have_learned() # affiche tout ce qu'il a etudier
```

### 📌 Supprimer une propriete ou un objet

```python
del zeev.age # on libere de la memoire
print(zeev.age) # age non defini
```
- On peut supprimer une instance
  - petit rappel une instance c'est:
    - ```python
        dark_vador = Person("Dark Vador",30) # creer une instance
    ```
    -```python
        del dark_vador # on supprime dark vador (merci luke)
    ```

### 📌 Les 3 principes en Oriente-Objet: L'encapsulation, l'heritage et le polymorphisme
### 📌 Getter / Setter: encapsulation (sorte d'intermediaire)
```python
    class Person:
        def __init__(self,name):
            self.name = name
        
        def setName(self,name):
            self.name = name

        def getName(self):
            return self.name

# implementation
dark_miaul = Person("Luke")
print(dark_miaul.getName()) # Luke

dark_miaul.setName("Dark Miaul")
print(dark_miaul.getName()) # Dark Miaul
```
- use case: valider des donnees selon des criteres
```python
    class Person:
        def __init__(self,name):
            self.name = name
        
        def setName(self,name):
            if len(name) < 9:
                self.name = name
            else:
                print("ton nom a plus de 8 caractere, trop long!")

        def getName(self):
            return self.name

# implementation
dark_miaul = Person("Luke")
print(dark_miaul.getName()) # Luke

dark_miaul.setName("DarkMiaul") # affiche une erreur: 9 caracteres trop long
dark_miaul.setName("DarkMiol") # affiche une erreur: 9 caracteres trop long
print(dark_miaul.getName()) # DarkMiol
```

### 📌 Heritage
L'heritage permet de partager les elements d'un ensemble dans un autre:
- Une personne a un nom
- Un etudiant est une personne, donc elle possedera un nom
- On aura pas besoin de creer le nom il est automatiquement appeler sur la classe superieur

```python
class Person:
    def __init__(self,name):
        self.name = name
    
    def setName(self,name):
        if len(name) < 9:
            self.name = name
        else:
            print("ton nom a plus de 8 caractere, trop long!")

    def getName(self):
        return self.name


class Student(Person):
    pass
```
- autre maniere d'herite et d'avoir des propriete et fonctions qui ne sont pas dans la class Person:

```python
class Person:
    def __init__(self,name):
        self.name = name
    
    def setName(self,name):
        if len(name) < 9:
            self.name = name
        else:
            print("ton nom a plus de 8 caractere, trop long!")

    def getName(self):
        return self.name

class Student(Person):
    # la propriete school_name est defini et VISIBLE que sur l'objet Student. (pas la class PERSON 😡)

    def __init__(self,name,age,school_name):
        super().__init__(name,age)
        self.school_name
    
    def get_school_name(self):
        return self.school_name

    def set_school_name(self, school_name):
        self.school_name = school_name

    def advantage(self):
        print("Je suis une fonction qui n'existe pas dans l'ensemble(class) Person")
```

### 📌 Polymorphisme

- un Vehicule:
  - Bus
  - Moto
  - Voiture

```python
class Vehicle:
	def __init__(self,wheels,motor,fuel):
		self.wheels = wheels
		self.motor = motor
		self.fuel = fuel
	def show(self):
		print(f"vehicle:\nw:{self.wheels} \nm:{self.motor} \nf:{self.fuel}")
	def drive(self):
		print("Je roule en vehicle")

class Bus(Vehicle):
    def __init__(self, name, has_microphone):
        self.has_microphone = has_microphone
        super().__init__(8,"essence","super")
        self.name = name
        print(f"{self.name}: {self.wheels}")
        
class Moto(Vehicle):
    def __init__(self,wheels,name,has_top_case):
        self.has_top_case = has_top_case
        super().__init__(wheels,"GP","95")
        self.name = name
        print(f"{self.name}: {self.wheels}")
    def drive(self):
        super().drive()
        print("Je roule en moto")
        

class Car(Vehicle):
    def __init__(self,name):
        super().__init__(4,"battery","electric")
        self.name = name
        print(f"{self.name}: {self.wheels}")
    def drive(self):
        print("Je roule en voiture")
        
toyota = Car('Toyota')
bus_magic = Bus('Le bus magique', True)
moto = Moto(2,'Harley Davidson', True)

for v in (toyota, bus_magic, moto):
	v.show()
	v.drive()
```

- lorsque l'enfant possede la methode drive(), on dit qu'elle override, (= elle n'execute pas la methode parente).


---

## 🌟 12. Gestion des fichiers - Notion de persistance de donnee.

### 📌 Lecture d'un fichier
Lire tout le fichier :
```python
file = open('names.txt')
whole_file = file.read()
```

Lire ligne par ligne :
```python
file = open('names.txt')
line = file.readline() # Affiche la première ligne
line = file.readline() # Affiche la deuxième ligne
```

Traiter le document ligne par ligne :
```python
file = open('names.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
```

### 📌 Écriture dans un fichier
Rajouter des noms dans un fichier :
```python
f = open('names.txt', 'a') # "a" pour ajouter à la fin du fichier
while True:
    name = input('Entrez un nom: ')
    if len(name) == 0:
        break
    f.write(name)
f.close() # Ferme le flux
```

Supprimer tout le contenu d'un fichier :
```python
f = open('names.txt', 'w') # 'w' pour écraser le contenu
f.write('')
f.close()
```

Créer un nouveau fichier vierge :
```python
name = input('Entrez un nom de fichier: ')
f = open(f'{name}.txt', 'x')
f.close()
```

Créer en masse des fichiers :
```python
for filename in ['html', 'css', 'js']:
    open(filename + ".txt", "x") # Crée un fichier selon la variable
```

### 📌 Suppression d'un fichier
Supprimer un fichier :
```python
import os
if os.path.exists("fichier.txt"):
    os.remove("fichier.txt")
else:
    print("Le fichier n'existe pas.")
```

---

## 🌟 13. JSON (JavaScript Object Notation)

JSON est un format léger d'échange de données, facile à lire et à écrire pour les humains, ainsi qu'à analyser et générer pour les machines.

### 📌 Structure JSON
Un fichier JSON est constitué de paires clé-valeur, similaires aux dictionnaires Python :

```json
{
    "nom": "Alice",
    "age": 25,
    "langages": ["Python", "JavaScript"]
}
```

### 📌 Lire un fichier JSON
Pour lire un fichier JSON en Python, utilisez la bibliothèque intégrée `json` :

```python
import json

# Lire le contenu du fichier JSON
with open('data.json', 'r') as file:
    data = json.load(file)  # Charge le JSON en un dictionnaire Python
    print(data)
```

### 📌 Écrire dans un fichier JSON
Pour écrire des données dans un fichier JSON :

```python
import json

# Exemple de données
data = {
    "nom": "Alice",
    "age": 25,
    "langages": ["Python", "JavaScript"]
}

# Écrire dans un fichier JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Ajout d'une indentation pour une meilleure lisibilité
```

### 📌 Modifier un fichier JSON
Pour mettre à jour les données existantes dans un fichier JSON :

```python
import json

# Charger les données existantes
with open('data.json', 'r') as file:
    data = json.load(file)

# Modifier les données
data["age"] = 26

# Réécrire les données dans le fichier
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

### 📌 Gestion JSON avec le File Manager
Voici comment combiner la manipulation des fichiers et le JSON :

- **Créer un fichier JSON vide :**

```python
import json

# Initialiser des données vides
data = {}

# Créer un fichier JSON vide
with open('new_file.json', 'w') as file:
    json.dump(data, file, indent=4)
```

- **Ajouter des données à un fichier JSON :**

```python
import json

new_entry = {
    "nom": "Bob",
    "age": 30,
    "langages": ["Java", "Go"]
}

# Charger les données existantes
with open('data.json', 'r') as file:
    data = json.load(file)

# Ajouter la nouvelle entrée
if "personnes" not in data:
    data["personnes"] = []
data["personnes"].append(new_entry)

# Réécrire les données dans le fichier
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

- **Supprimer une entrée d'un fichier JSON :**

```python
import json

# Charger les données existantes
with open('data.json', 'r') as file:
    data = json.load(file)

# Suppression basée sur une condition
if "personnes" in data:
    data["personnes"] = [p for p in data["personnes"] if p["nom"] != "Bob"]

# Réécrire les données mises à jour
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

---

## 🌟 14. Gestion des Exceptions avec `try-except`

En Python, la gestion des erreurs est essentielle pour éviter les plantages de programme lorsque des erreurs inattendues surviennent. La structure `try-except` permet de gérer ces situations de manière propre et contrôlée.

### 📌 Structure de base

```python
try:
    # Code qui pourrait générer une erreur
    operation = 10 / 0
except ZeroDivisionError:
    # Code à exécuter en cas d'erreur
    print("Division par zéro interdite !")
```

### 📌 Types d'Exceptions Courantes
Voici quelques types d'exceptions courantes que vous pourriez rencontrer :

- **`ZeroDivisionError`** : Division par zéro.
- **`ValueError`** : Erreur de type pour une valeur incorrecte.
- **`FileNotFoundError`** : Fichier introuvable.
- **`TypeError`** : Type incorrect utilisé.
- **`IndexError`** : Indice hors des limites d'une liste.
- **`KeyError`** : Clé inexistante dans un dictionnaire.

### 📌 Exemple avec plusieurs exceptions

```python
try:
    fichier = open("inexistant.txt", "r")
    contenu = int(fichier.read())
    print(10 / contenu)
except FileNotFoundError:
    print("Le fichier n'existe pas.")
except ValueError:
    print("Erreur : Impossible de convertir le contenu en entier.")
except ZeroDivisionError:
    print("Erreur : Division par zéro détectée.")
```

### 📌 Blocs `else` et `finally`

- **`else`** : S'exécute si aucune exception n'est levée.
- **`finally`** : S'exécute quoi qu'il arrive (utile pour nettoyer les ressources).

```python
try:
    fichier = open("data.txt", "r")
    contenu = fichier.read()
    print("Lecture réussie :", contenu)
except FileNotFoundError:
    print("Erreur : Le fichier est introuvable.")
else:
    print("Aucune erreur détectée.")
finally:
    print("Fin de l'exécution.")
```

### 📌 Lever une exception personnalisée
Vous pouvez lever vos propres exceptions avec l'instruction `raise` :

```python
def verifier_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif !")
    print("Âge valide :", age)

try:
    verifier_age(-5)
except ValueError as e:
    print("Erreur détectée :", e)
```

### 📌 Utilisation avancée : Capturer l'exception
Vous pouvez capturer l'objet exception pour plus de détails :

```python
try:
    resultat = 10 / 0
except ZeroDivisionError as e:
    print(f"Erreur capturée : {e}")
```

---

