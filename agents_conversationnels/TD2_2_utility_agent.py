#Hugo BERANGER - M2 MIAGE IA

import random

NBIT = 5  # nombre d'itérations
salleA = ['A']
salleB = ['B']
etat = []
goal = ["None", 0]
actionLog = []
random.seed()


def initialisation():
    r = random.randint(0, 1)
    if r == 1:
        print("L'aspirateur démarre en salle A")
        return salleA[0]
    else:
        print("L'aspirateur démarre en salle B")
        return salleB[0]


def action(emplacement):
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


def actionTraj(emplacement):
    if etat[0] == "A":
        if etat[2] == goal[1]:
            print("Objectif atteint !")
            print("On va en salle A")
            etat[0] = "A"
            return True
        else:
            etat[2] += 1
            print("Objectif non atteint, on nettoie la salle, nous allons en case {0}".format(
                etat[2]))
            salleA[etat[2]] = 0

    if etat[0] == "B":
        if etat[2] == goal[1]:
            print("Objectif atteint !")
            print("On va en salle B")
            etat[0] = "B"
            return True
        else:
            etat[2] += 1
            print("Objectif non atteint, on nettoie la salle, nous allons en case {0}".format(
                etat[2]))
            salleB[etat[2]] = 0


def utilite():
    saleteA = 0
    saleteB = 0
    for i in range(goal[1]):
        saleteA += salleA[i+1]
        saleteB += salleB[i+1]
    print("Cases à nettoyée en A jusqu'a l'objectif : {0}".format(saleteA))
    print("Cases à nettoyée en B jusqu'a l'objectif : {0}".format(saleteB))
    if saleteA > saleteB:
        etat[0] = "A"
        print("La salle A est la plus salle, on s'y deplace afin de la nettoyée sur notre chemin")
    elif saleteB > saleteA:
        etat[0] = "B"
        print("La salle B est la plus salle, on s'y deplace afin de la nettoyée sur notre chemin")
    return etat


def changerSalles():
    for x in range(NBIT):
        salleA.append(random.randint(0, 1))
        salleB.append(random.randint(0, 1))


def etatActuel():
    print("L'aspirateur se trouve dans la salle {0} dont l'état est {1}".format(
        etat[0], etat[1]))


def setGoal():
    salle = random.randint(0, 1)
    case = random.randint(0, NBIT)
    if salle:
        goal = ['B', case]
    else:
        goal = ['A', case]
    print("Le but de l'aspirateur est la case {0} dans le salle {1}".format(
        goal[1], goal[0]))
    return goal


etat.append(initialisation())
etat.append("inconnue")

# salle avant robot
changerSalles()
print(salleA)
print(salleB)
goal = setGoal()
etat.append(0)
etat = utilite()
for i in range(NBIT+1):
    # action(etat[0])
    if actionTraj(etat[0]):
        break
    # etatActuel()

# salles après robot
print(salleA)
print(salleB)
