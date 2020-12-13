# Hugo BERANGER - M2 MIAGE IA

from pomegranate import *

G = BayesianNetwork("BotanicalProblem")

malade = DiscreteDistribution({"Oui": 0.1, "Non": 0.9})
sec = DiscreteDistribution({"Oui": 0.1, "Non": 0.9})
perd_feuilles = ConditionalProbabilityTable([
    ["Non", "Non", "Non", .98],
    ["Non", "Non", "Oui", .02], 
    ["Non", "Oui", "Non", .15], 
    ["Non", "Oui", "Oui", .85], 
    ["Oui", "Non", "Non", .1], 
    ["Oui", "Non", "Oui", .9], 
    ["Oui", "Oui", "Non", .05], 
    ["Oui", "Oui", "Oui", .95]], 
    [malade, sec])

s = State(malade, name = "malade")
d = State(sec, name = "sec")
l = State(perd_feuilles, name = "perd_feuilles")
G.add_states(s, d, l)
G.add_edge(s, l)
G.add_edge(d, l)
G.bake()

print(G)

beliefs = G.predict_proba({})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)

beliefs = G.predict_proba({"perd_feuilles": "Oui"})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)

beliefs = G.predict_proba({"perd_feuilles": "Oui", "sec": "Non"})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)