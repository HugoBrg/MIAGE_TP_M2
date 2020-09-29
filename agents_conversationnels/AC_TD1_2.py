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
    if etat[0] == "A":
        if salleA[i] == 1:
            print("On nettoie la salle A")
            salleA[i] = 0
            etat[1] = "sale"
            actionLog.append(etat)
        if salleA[i] == 0:
            print("La salle A est propre, direction salle B")
            etat[0] = salleB[0]
            etat[1] = "propre"
            actionLog.append(etat)


    if etat[0] == "B":    
        if salleB[i] == 1:
            print("On nettoie la salle B")
            salleB[i] = 0
            etat[1] = "sale"
            actionLog.append(etat)
        if salleB[i] == 0:
            print("La salle B est propre, direction salle A")
            etat[0] = salleA[0]
            etat[1] = "propre"
            actionLog.append(etat)


    if etat[0] == "A":
        if salleA[i] == 1:
            proprete = "sale"
            print("On nettoie la salle A")
            salleA[i] = 0
            etat[1] = "sale"
            actionLog.append(etat)
        if salleA[i] == 0:
            print("La salle A est propre, direction salle B")
            etat[0] = salleB[0]
            etat[1] = "propre"
            actionLog.append(etat)

def changerEtat():
    for x in range(NBIT):
        salleA.append(random.randint(0,1))
        salleB.append(random.randint(0,1))

def etatActuel():
    print("L'aspirateur se trouve dans la salle {0} dont l'état est {1}".format(etat[0],etat[1]))

etat.append(initialisation())
etat.append("inconnue")

#salle avant robot
changerEtat()
print(salleA)
print(salleB)

for i in range(NBIT+1):
    action(etat[0])
    #etatActuel()

#salles après robot
print(salleA)
print(salleB)
