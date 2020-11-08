###########################################################################################
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
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    model.fit(X, y, epochs=150, batch_size=10)
    # evaluate the keras model
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))

###########################################################################################

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


def numberOfNeurons(ind):
    x = []
    x.append(random.randrange(2, 20))
    x.append(random.randrange(2, 20))
    return ind(x)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("Individual", numberOfNeurons, creator.Individual)
toolbox.register("pop", tools.initRepeat, list, toolbox.Individual)
# toolbox.register("mate", mate, ind=creator.Individual)
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=MUTPB)
toolbox.register("select", tools.selTournament, tournsize=3)
# toolbox.register("evaluate", evaluate)
pop = toolbox.pop(POP_SIZE)
print(pop)