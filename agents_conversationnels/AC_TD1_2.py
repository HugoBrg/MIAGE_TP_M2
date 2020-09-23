import random

NBIT = 5 #nombre d'itérations
salleA = ['A']
salleB = ['B']
etat = []
actionLog = []
random.seed()

def initialisation():
    r = random.randint(0,1)
    if r == 1:
        print("L'aspirateur démarre en salle A")
        return salleA[0]
    else:
        print("L'aspirateur démarre en salle B")
        return salleB[0]


def action (emplacement):
    for i in range(NBIT+1):
        if emplacement == "A":
            if salleA[i] == 1:
                print("On nettoie la salle A")
                salleA[i] = 0
            if salleA[i] == 0:
                print("La salle A est propre, direction salle B")
                emplacement = salleB[0]
        if emplacement == "B":    
            if salleB[i] == 1:
                print("On nettoie la salle B")
                salleB[i] = 0
            if salleB[i] == 0:
                print("La salle B est propre, direction salle A")
                emplacement = salleA[0]

        if emplacement == "A":
            if salleA[i] == 1:
                print("On nettoie la salle A")
                salleA[i] = 0
            if salleA[i] == 0:
                print("La salle A est propre, direction salle B")
                emplacement = salleB[0]

def changerEtat():
    for x in range(NBIT):
        salleA.append(random.randint(0,1))
        salleB.append(random.randint(0,1))

emplacement = initialisation()
changerEtat()
etat.append(salleA)
etat.append(salleB)
print(salleA)
print(salleB)
action(emplacement)
print(salleA)
print(salleB)