# Hugo BERANGER - M2 MIAGE IA

from deap import base
from deap import tools
import random
from deap import creator
from deap import algorithms

NGEN = 10
CXPB = 0.1
MUTPB = 0.1
IND_SIZE = 5
POP_SIZE = 100

toolbox = base.Toolbox()


def evaluateInd(individual):
    a = sum(individual)
    b = len(individual)
    return a, 1. / b

creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=IND_SIZE)


pop = []
for x in range(POP_SIZE):
    ind = toolbox.individual()
    pop.append(ind)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluateInd)

# Using the tools

for g in range(NGEN):
    # Select and clone the next generation individuals
    offspring = map(toolbox.clone, toolbox.select(pop, len(pop)))

    # Apply crossover and mutation on the offspring, varAnd regroup the mate() and mutate() function of the toolbox
    offspring = algorithms.varAnd(offspring, toolbox, CXPB, MUTPB)

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # The population is entirely replaced by the offspring
    pop[:] = offspring