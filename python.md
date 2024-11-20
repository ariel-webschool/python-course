# 🚀 Introduction à Python – Guide Ludique et Pratique

## 🌟 1. Les Bases des Fonctions Python

### 📌 Affichage et interactions utilisateur
```python
print("Hello, Python!")  # Afficher un message
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

<details>
<summary>Solution</summary>

```python
age = int(input("Quel est votre âge ? "))

if age >= 13:
    print("Autorisé à voir le film.")
else:
    print("Accès interdit, il vous manque " + str(13 - age) + " ans.")
```
</details>

---

## 🌟 7. Tableaux (listes)

Les tableaux permettent de stocker plusieurs valeurs dans une seule variable.  
**Exemple :**
```python
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])  # pomme
print(len(fruits))  # Nombre d'éléments : 3
```

### 📌 Itération dans une liste :
```python
for fruit in fruits:
    print(fruit)
```

---

## 🌟 8. Fonctions

### 📌 Définir une fonction :
```python
def saluer(nom):
    print("Bonjour, " + nom + " !")
```

### 📌 Appeler une fonction :
```python
saluer("Alice")  # Bonjour, Alice !
```

---

## 🌟 9. Bibliothèques
Une bibliothèque est un ensemble de fonctions prédéfinies que vous pouvez importer dans votre code.

### 📌 Exemple avec `random` :
```python
import random

nombre_aleatoire = random.randint(1, 10)  # Générer un nombre entre 1 et 10
print(nombre_aleatoire)
```

---

## 🌟 10. Fonctionnalités avancées

### 📌 Générer une plage de nombres
```python
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5
```

### 📌 Obtenir le nombre d'éléments dans une liste
```python
nombres = [10, 20, 30]
print(len(nombres))  # 3
```

