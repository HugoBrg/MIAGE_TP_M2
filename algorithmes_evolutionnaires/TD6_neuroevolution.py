# Hugo BERANGER - M2 MIAGE IA

# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

def neuronalNetwork(dense1NeuronNumber, dense2NeuronNumber):
    # define the keras model
    model = Sequential()
    model.add(Dense(dense1NeuronNumber, input_dim=8, activation='relu'))            # modification paramètres layer
    model.add(Dense(dense2NeuronNumber, activation='relu'))                         # modification paramètres layer
    model.add(Dense(1, activation='sigmoid'))
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X, y, epochs=150, batch_size=10, verbose=0)
    # evaluate the keras model
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))
    return(accuracy)

###########################################################################################

from deap import base
from deap import tools
from deap import creator
import random
import numpy

# constant
NGEN = 10            # number of generation
CXPB = 0.4          # crossover probabilty
MUTPB = 0.2         # mutation probability
IND_SIZE = 8        # size of one individual
POP_SIZE = 10        # number of individuals


def numberOfNeurons(ind):
    x = []
    x.append(numpy.ones(random.randrange(2, 11)))
    x.append(numpy.ones(random.randrange(2, 11)))
    return ind(x)

def evaluate(ind):
    dense1NeuronNumber = numpy.count_nonzero(ind[0] == 1)
    dense2NeuronNumber = numpy.count_nonzero(ind[1] == 1)
    return neuronalNetwork(dense1NeuronNumber,dense2NeuronNumber),

def mutate(ind):
    print("mutate")
    y = random.randrange(0, 2) # si 0 layer1 sinon layer2
    x = random.randrange(0, 2) # si 0 dropout sinon ajout neurone
    if(y):
        if(x):
            ind[1] = numpy.append(ind[1],1)
        else:
            ind[1] = numpy.delete(ind[1], [len(ind[1])-1])
    else:
        if(x):
            ind[0] = numpy.append(ind[0],1)
        else:
            ind[0] = numpy.delete(ind[0], [len(ind[1])-1])
    return ind

    
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("Individual", numberOfNeurons, creator.Individual)
toolbox.register("pop", tools.initRepeat, list, toolbox.Individual)
# toolbox.register("mate", mate, ind=creator.Individual)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=MUTPB)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)
pop = toolbox.pop(POP_SIZE)
# print(pop)
# print(pop[0])
# print(evaluate(pop[0]))
# print(mutate(pop[0]))

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

def generation():
    for g in range(NGEN):
        print("GENERATION : ", g)
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        """
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        """
        
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
            print("Individu : ",meilleurInd(pop)[1])
        elif(g == NGEN - 1):
            print("Meilleur invidivu gen 100 - fit : ", meilleurInd(pop)[0])
            print("Individu : ",meilleurInd(pop)[1])

generation()