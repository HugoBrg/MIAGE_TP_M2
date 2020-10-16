# Hugo BERANGER - M2 MIAGE IA

from deap import base
from deap import tools
import random
from deap import creator
from deap import algorithms
import numpy
import pickle
import matplotlib.pyplot as plt

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

pop, logbook = algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, NGEN)

print("Simple statistics")
stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("avg", numpy.mean)
stats.register("std", numpy.std)
stats.register("min", numpy.min)
stats.register("max", numpy.max)
record = stats.compile(pop)
print(record)

print("Multi objective statistics")
stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("avg", numpy.mean, axis=0)
stats.register("std", numpy.std, axis=0)
stats.register("min", numpy.min, axis=0)
stats.register("max", numpy.max, axis=0)
record = stats.compile(pop)
print(record)

print("Multiple statistics")
stats_fit = tools.Statistics(key=lambda ind: ind.fitness.values)
stats_size = tools.Statistics(key=len)
mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)

mstats.register("avg", numpy.mean)
mstats.register("std", numpy.std)
mstats.register("min", numpy.min)
mstats.register("max", numpy.max)

record = mstats.compile(pop)
print(record)

print("Logging")
logbook = tools.Logbook()
logbook.record(gen=0, evals=30, **record)
gen, avg = logbook.select("gen", "avg")
pickle.dump( logbook, open( "lb_file.txt", "wb" ) ) #saving

print("Printing")
logbook.header = "gen", "avg", "spam"
print(logbook)
#print(logbook.stream)
#logbook.record(gen=1, evals=15, **record)
#print(logbook.stream)                              #print unprinted entries

print("Multi statistics printing")
logbook = tools.Logbook()
logbook.record(gen=0, evals=30, **record)
logbook.header = "gen", "evals", "fitness", "size"
logbook.chapters["fitness"].header = "min", "avg", "max"
logbook.chapters["size"].header = "min", "avg", "max"
print(logbook)


print("Plotting")
gen = logbook.select("gen")
fit_mins = logbook.chapters["fitness"].select("min")
size_avgs = logbook.chapters["size"].select("avg")

fig, ax1 = plt.subplots()
line1 = ax1.plot(gen, fit_mins, "b-", label="Minimum Fitness")
ax1.set_xlabel("Generation")
ax1.set_ylabel("Fitness", color="b")
for tl in ax1.get_yticklabels():
    tl.set_color("b")

ax2 = ax1.twinx()
line2 = ax2.plot(gen, size_avgs, "r-", label="Average Size")
ax2.set_ylabel("Size", color="r")
for tl in ax2.get_yticklabels():
    tl.set_color("r")

lns = line1 + line2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc="center right")

plt.show()