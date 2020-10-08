# Hugo BERANGER - M2 MIAGE IA

import random
N = 20  # longueur d'un génome

random.seed()
pop = []
A = []
AP = []

#------------------INITIALISATION------------------#


def initialisation(pop):
    for i in range(N):
        randomDigit = random.randint(0, N-1)
        pop.append(randomDigit)
    pop.sort(reverse=True)
    print("pop     : {0}".format(pop))

    return pop

#------------------REPARTITION------------------#


def repartition():
    for x in range(len(pop)):
        if sum(A) < sum(AP):
            A.append(pop[x])
        else:
            AP.append(pop[x])
    print("A       : {0}".format(A))
    print("AP      : {0}".format(AP))

#------------------FITNESS------------------#


def fitness(AP):
    return 1/(z(AP)+1)

#------------------Z------------------#


def z(AP):
    APdiffA = 0
    for z in A:
        if z not in AP:
            APdiffA += z
    print("z(A')   : {0}".format(abs(sum(AP) - APdiffA)))
    return abs(sum(AP)*N - APdiffA*N)

#------------------TEST------------------#


def test(pop):
    pop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    pop.sort(reverse=True)
    return pop


#------------------APPELS------------------#
pop = test(pop)
# initialisation(pop)
repartition()
print("fitness : {0}".format(fitness(AP)))
