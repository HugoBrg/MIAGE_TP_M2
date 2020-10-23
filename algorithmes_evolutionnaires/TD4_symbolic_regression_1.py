# Hugo BERANGER - M2 MIAGE IA

from deap import base
from deap import tools
import random
from deap import creator
from deap import algorithms

# constant
NGEN = 10           # number of generation
CXPB = 0.1          # crossover probabilty
MUTPB = 0.1         # mutation probability
IND_SIZE = 6        # size of one individual
POP_SIZE = 6        # number of individuals

def evaluateInd(individual):    # fitness evaluation
    a = sum(individual)
    b = sum(individual)
    return a, 1. / b

index = 0
def attrInd():
    global index
    func = []
    with open('TD4.txt','r') as file:    
        line = file.readlines()
        for word in line[index].split():            
            func.append(word)
    index += 1
    file.close()
    return func

toolbox = base.Toolbox()

# creation of an individual composed of 5 float from 0 to 5
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox.register("attr_tuple", attrInd)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_tuple, n=IND_SIZE)

# creation of the population
pop = []
inds = toolbox.individual()                   
for x in range(POP_SIZE):
    pop.append(inds[x])

print(pop)
print(type(pop))
print(type(pop[0]))

# creation of the methods
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluateInd)

for g in range(NGEN):
    # select and clone the next generation individuals
    offspring = map(toolbox.clone, toolbox.select(pop, len(pop)))

    # apply crossover and mutation on the offspring, varAnd regroup the mate() and mutate() function of the toolbox
    offspring = algorithms.varAnd(offspring, toolbox, CXPB, MUTPB)

    # evaluate the individuals with an invalid fitness
    invalid_ind = [inds for ind in offspring if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for inds, fit in zip(invalid_ind, fitnesses):
        inds.fitness.values = fit

    # the population is entirely replaced by the offspring
    pop[:] = offspring