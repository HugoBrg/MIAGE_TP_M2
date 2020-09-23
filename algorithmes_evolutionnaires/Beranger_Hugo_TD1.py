#Hugo BERANGER - M2 MIAGE IA

import random
MAXGEN = 100                                                       #nb max de générations
POPSIZE = 100                                                       #taille de la population
N = 20                                                              #longueur d'un génome
PMUT = 0.01                                                         #proba d'une mutation
PX = 0.6                                                            #proba d'une recombination

random.seed()
pop = []

#------------------INITIALISATION------------------#
def initialisation(pop):
    for i in range(POPSIZE):
        genome = ""
        for x in range(N):
            randomDigit = random.randint(0,1)
            genome += "{}".format(randomDigit)                      #création des génomes
        pop.append(genome)
    return pop

#------------------SELECTION------------------#
def selection(pop):
    selection = [[0 for k in range(2)] for j in range(POPSIZE)]
    Cf = 0
    for z in range(POPSIZE):    
        selection[z][0] = pop[z]                                    #tableau[génome][Cf]
        for y in pop[z]:
            if y == '1':    
                Cf += 1                                             #calcul de Cf
        selection[z][1] = Cf  

    randomNumberSeq = []                                            #génération random sequence
    for p in range(POPSIZE):
        randomNumberSeq.append(random.randint(0,selection[POPSIZE-2][1]))


    popNew = []
    for m in range(POPSIZE):                                        #recherche cf plus proche
        for u in range(POPSIZE):
            if selection[u][1] > randomNumberSeq[m]:                #on trouve le cF superieur le plus proche
                popNew.append(selection[u][0])
                break                                               #dès qu'on trouve le cF superieur on sort du de la boucle
    print("cF max               : {0}".format(selection[POPSIZE-1][1]))                                
    return popNew

#------------------COMBINATION------------------#
def recombination(pop):
    nbRecombination = 0
    for i in range(POPSIZE):
        if random.random() <= PX:
            nbRecombination += 1
            secondGenomeId = random.randint(0,POPSIZE-1)
            while(secondGenomeId == i):
                secondGenomeId = random.randint(0,POPSIZE-1)
            cut = random.randint(1,N-1)                             #selection de l'endroit de découpe alétoire
            left1 = pop[i][0:cut]                                   #intervertie les "bout" de génomes
            left2 = pop[secondGenomeId][0:cut]
            right1 = pop[i][cut:N]
            right2 = pop[secondGenomeId][cut:N]
            pop[i] = left2 + right1                                 #assignation des génomes recombinés
            pop[secondGenomeId] = left1 + right2    
    print("nb de recombination  : {0}".format(nbRecombination))
    return pop
            

#------------------MUTATION------------------#
def mutation(pop):
    nbMutation = 0                                
    for i in range(POPSIZE):
        for x in range(N-1):      
            if random.random() <= PMUT:                             #probabilité d'avoir une mutation
                nbMutation += 1
                if pop[i][x]=="1":                                  #inverse les bits muté 
                    pop[i] = pop[i][0:x] + '0' + pop[i][x+1:N]
                elif pop[i][x]=="0":
                    pop[i] = pop[i][0:x] + '1' + pop[i][x+1:N]
    print("nb de mutation       : {0}".format(nbMutation))
    return pop

#------------------GENERATION------------------#
for g in range(100):
    print("_______________GEN {0}________________".format(g+1))   
    pop = initialisation(pop)
    print("nb de génomes        : {0}".format(len(pop)))
    pop = selection(pop)
    pop = recombination(pop)
    pop = mutation(pop)
    #print(pop)                                                     #pour observer la population
print("--------------Paramètres--------------")
print("taille génome        : {0}".format(N))
print("proba recombination  : {0}".format(PX))
print("proba mutation       : {0}".format(PMUT))
print("cF maximum théorique : {0}".format(N*POPSIZE))
print("--------------------------------------")