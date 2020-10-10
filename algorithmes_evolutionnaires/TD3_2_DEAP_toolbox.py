# Hugo BERANGER - M2 MIAGE IA

from deap import base
from deap import tools

toolbox = base.Toolbox()


def evaluateInd(individual):
    # Do some computation
    return result,


toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluateInd)
