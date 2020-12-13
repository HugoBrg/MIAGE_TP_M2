# Hugo BERANGER - M2 MIAGE IA

import random as rand
import numpy as np
import pandas
from pomegranate import *

# Q1
model = HiddenMarkovModel("MMC")

bullish = DiscreteDistribution({-1: 1/3, 0: 1/3, +1: 1/3})  # hausse
bearish = DiscreteDistribution({-1: 1/3, 0: 1/3, +1: 1/3})  # baisse

bu = State(bullish,name="bu")
be = State(bearish,name="be")

model.add_states(bu,be)
model.add_transition(model.start, bu, 0.5)
model.add_transition(model.start, be, 0.5)

model.add_transition(bu, be, 0.5)
model.add_transition(be, bu, 0.5)
model.bake()

# Q2
liste = []
to_add = 1
for x in range(1000):
    if x%50 == 49:
        if to_add == -1:
            to_add = +1
        else:
            to_add = -1
    liste.append(to_add)


proba = []
for x in liste:
    r = rand.random()
    if x == -1:
        if r <= 0.2:
            proba.append(-1)
        elif r > 0.2 and r <= 0.5:
            proba.append(0)
        else:
            proba.append(+1)
    else:
        if r <= 0.5:
            proba.append(-1)
        elif r > 0.5 and r <= 0.7:
            proba.append(0)
        else:
            proba.append(+1)

# Q3 
print("========================model========================")
model.fit([proba],algorithm='viterbi')
print(model)
print("=====================================================")

# Q4
print("========================gold=========================")
df = pandas.read_csv('gold.csv')

st = []
previous = 1
for actual in df["Adj Close"]:
    if actual/previous -1 > 0.005:
        st.append(+1)
    elif abs(actual/previous -1) <= 0.005:
        st.append(0)
    elif actual/previous  -1 < -0.005:
        st.append(-1)
    previous = actual
model.fit([st], algorithm="viterbi")

print(model)
print("=====================================================")

# Q5

# Données utilisées : https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF

# Le cours de l'or est généralement stable et en augmentation constante depuis ces derniers mois. 
# Il ressort de mon modèle que ce soit en bearish ou en bullish la stabilité est la tendance la plus observée. 
# La seconde tendance la plus observées est l'augmentation, cela correspond aux observations réelles décrit ci-dessus.

# Il est difficile d'observer une correspondance systématique ou un décalage en l'absence de donnés temporelles

# La modélisation semble globalelement fonctionner

