# Hugo BERANGER - M2 MIAGE IA

from deap import base
from deap import tools
from deap import creator
from math import *
import random
import numpy

# constant
NGEN = 100          # number of generation
CXPB = 0.4          # crossover probabilty
MUTPB = 0.2         # mutation probability
IND_SIZE = 8        # size of one individual
POP_SIZE = 100      # number of individuals


def valeurBoursieres(ind):
    return ind(numpy.random.dirichlet(numpy.ones(8), size=1)[0])


def evaluate(individual):
    rendements = [-0.02, -0.01, 0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
    mu = 0
    for x in range(IND_SIZE):
        mu = mu + individual[x] * rendements[x]

    variances = [0, 0.05, 0.09, 0.01, 0.02, 0.16, 0.20, 0.25]
    sigma = 0
    for x in range(IND_SIZE):
        sigma = sigma + individual[x] * variances[x]**2

    sharpe = mu / sqrt(sigma)
    return sharpe,


def sommeInd(individual):
    if sum(individual) == 1:
        return True
    return False


def sommeIndConstrainte(individual):
    if(sommeInd(individual)):
        if (individual[0] + individual[1] >= 0.1 and
            individual[2] <= 0.1 and
            individual[4] + individual[5] >= 0.2 and
                individual[6] + individual[7] <= 0.5):
            return True
        else:
            return False
    return False


def mate(ind1, ind2, ind):
    ind1 = ind(numpy.random.dirichlet(numpy.ones(8), size=1)[0])
    ind2 = ind(numpy.random.dirichlet(numpy.ones(8), size=1)[0])
    return ind1, ind2


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("Individual", valeurBoursieres, creator.Individual)
toolbox.register("pop", tools.initRepeat, list, toolbox.Individual)
toolbox.register("mate", mate, ind=creator.Individual)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=MUTPB)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)
pop = toolbox.pop(POP_SIZE)


def meilleurInd(pop):
    meilleurFit = 0
    meilleurInd = None
    for i in range(len(pop)):
        fit = toolbox.evaluate(pop[i])
        # print(fit)
        if(fit[0] > meilleurFit):
            meilleurFit = fit[0]
            meilleurInd = pop[i]
    return meilleurFit, meilleurInd


def generation(constraint):
    if (constraint):
        toolbox.decorate("evaluate", tools.DeltaPenalty(sommeIndConstrainte, [
                         0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]))
    else:
        toolbox.decorate("evaluate", tools.DeltaPenalty(
            sommeInd, [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]))

    for g in range(NGEN):
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring

        if(g == 0):
            print("Meilleur individu gen 1 - fit   : ", meilleurInd(pop)[0])
            #print("Individu : ",meilleurInd(pop)[1])
        elif(g == NGEN - 1):
            print("Meilleur invidivu gen 100 - fit : ", meilleurInd(pop)[0])
            #print("Individu : ",meilleurInd(pop)[1])


print("Sans contraintes : ")
generation(False)
print("Avec contraintes : ")
generation(True)

# Poour une raison qui  m'est inconnue le meilleur individu n'évolue jamais