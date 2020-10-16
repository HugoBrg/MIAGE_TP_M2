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

algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, NGEN)