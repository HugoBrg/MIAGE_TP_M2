# Hugo BERANGER - M2 MIAGE IA

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Q1
res = ctrl.Antecedent(np.arange(0, 21, 1),'resultat')
met = ctrl.Antecedent(np.arange(0, 21, 1),'methode')
pre = ctrl.Antecedent(np.arange(0, 21, 1),'presentation')
eva = ctrl.Consequent(np.arange(0, 21, 1),'evaluation')

# Q2 Q3
res['mediocre'] = fuzz.trimf(res.universe, [0, 0, 10])
res['moyen'] = fuzz.trimf(res.universe, [0, 10, 20])
res['excellent'] = fuzz.trimf(res.universe, [10, 20, 20])

met['mediocre'] = fuzz.trimf(met.universe, [0, 0, 10])
met['moyen'] = fuzz.trimf(met.universe, [0, 10, 20])
met['excellent'] = fuzz.trimf(met.universe, [10, 20, 20])

pre['mediocre'] = fuzz.trimf(pre.universe, [0, 0, 10])
pre['moyen'] = fuzz.trimf(pre.universe, [0, 10, 20])
pre['excellent'] = fuzz.trimf(pre.universe, [10, 20, 20])

eva['mediocre'] = fuzz.trimf(eva.universe, [0,0,5])
eva['mauvais'] = fuzz.trimf(eva.universe, [0,5,10])
eva['moyen'] = fuzz.trimf(eva.universe, [5,10,15])
eva['bon'] = fuzz.trimf(eva.universe, [10,15,20])
eva['excellent'] = fuzz.trimf(eva.universe, [15,20,20])


rule1 = ctrl.Rule(res['moyen'] & met['mediocre'], eva['mauvais'])
rule2 = ctrl.Rule(res['moyen'] & met['excellent'], eva['bon'])
rule3 = ctrl.Rule(res['mediocre'] & met['moyen'], eva['mauvais'])
rule4 = ctrl.Rule(res['excellent'] & met['excellent'] & pre['excellent'], eva['excellent'])
rule5 = ctrl.Rule(res['mediocre'] | met['moyen'], eva['moyen'])
rule6 = ctrl.Rule(res['moyen'] | met['mediocre'], eva['mediocre'])

note_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])

note = ctrl.ControlSystemSimulation(note_ctrl)

# Q4 - Résultat globale : 6.77 - moyen
note.input['resultat'] = 12
note.input['methode'] = 6
note.input['presentation'] = 19

note.compute()
print(note.output['evaluation'])

# Q5 - Je pense que cette base  de règle n'est pas bien établie car quelqu'un ayant eu 12 à tout les critères de notation se retrouve avec une moyenne à 8.57 dite moyenne
note.input['resultat'] = 12
note.input['methode'] = 12
note.input['presentation'] = 12

note.compute()
print(note.output['evaluation'])

# Q6 - Plus les critères de notations sont complexe plus il est difficile d'écrire de règle effiace et cohérente. Ce genre de système a ses limites.