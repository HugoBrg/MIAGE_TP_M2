# Hugo BERANGER - M2 MIAGE IA

from pomegranate import *

G = BayesianNetwork("GestionEmployé")

licenciement = DiscreteDistribution({"oui": 0.5, "non": 0.5})
compta = ConditionalProbabilityTable(
    [
        ["oui", "james",  .37],
        ["non", "james",  .42],
        ["oui", "jules",  .63],
        ["non", "jules",  .58]
    ], 
    [licenciement]
)

rh = ConditionalProbabilityTable(
    [
        ["oui", "janet",  .30],
        ["non", "janet",  .20],
        ["oui", "jim",  .35],
        ["non", "jim",  .20],
        ["oui", "julia",  .35],      
        ["non", "julia",  .60]
    ], 
    [licenciement]
)

notif = ConditionalProbabilityTable(
    [
        ["janet","james","courrier", .40],
        ["janet","james","mail", .60],
        ["janet","jules","courrier", .70],
        ["janet","jules","mail", .30],
        ["jim","james","courrier", .30],
        ["jim","james","mail", .70],
        ["jim","jules","courrier", .65],
        ["jim","jules","mail", .35],
        ["julia","james","courrier", .25],
        ["julia","james","mail", .75],
        ["julia","jules","courrier", .55],
        ["julia","jules","mail", .45]
    ], 
    [rh,compta]
)


compta_state = State(compta, name = 'compta')
rh_state = State(rh, name = 'rh')
notif_state = State(notif, name = 'notif')
licenciment_state = State(licenciement, name = 'licencier')

G.add_states(licenciment_state,compta_state,rh_state,notif_state)
G.add_edge(rh_state,notif_state)
G.add_edge(compta_state,notif_state)
G.add_edge(licenciment_state,compta_state)
G.add_edge(licenciment_state,rh_state)
G.bake()

print(G)


# Question A (0.61)
print("================A================")
beliefs = G.predict_proba({'notif': 'courrier','rh': 'janet','compta': 'jules'})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)
print("================================")


# Question B (0.60)
print("================B================")
beliefs = G.predict_proba({'notif': 'courrier','rh': 'jim','compta': 'james'})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)
print("================================")


# Question C (0.36)
print("================C================")
beliefs = G.predict_proba({'rh': 'julia'})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)
print("================================")


# Question D (0.52)
print("================D================")
beliefs = G.predict_proba({'notif': 'mail'})
beliefs = map(str, beliefs)
for state, belief in zip(G.states, beliefs):
    print(state.name, belief)
print("================================")