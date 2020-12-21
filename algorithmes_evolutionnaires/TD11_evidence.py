# Hugo BERANGER - M2 MIAGE IA


from __future__ import print_function
from pyds import MassFunction
from itertools import product


print('=== creating mass functions ===')
m1 = MassFunction([({'NW', 'N', 'E', 'SE'}, 0.5), ({'C', 'NE'}, 0.3), ({'W', 'SW', 'S'}, 0.2)])     # Q1
print('m_1 =', m1) 
m2 = MassFunction([({'SW'}, 0.5), ({'C', 'S'}, 0.3), ({'E', 'SE'}, 0.2)])                           # Q2
print('m_2 =', m2)
m3 = MassFunction([({'NW', 'N', 'NE', 'W', 'C', 'E', 'SW', 'S', 'SE'}, 0.9), ({'W'}, 0.1)])         # Q3
print('m_3 =', m3)


print('\n=== Dempster\'s combination rule, unnormalized conjunctive combination (exact and approximate) ===')
print('Dempster\'s combination rule for m_1, m_2, and m_3 =', m1.combine_conjunctive(m2, m3))       # Q4
combined = m1.combine_conjunctive(m2, m3)
# Il faudrait concentrer les recherches dans les secteurs SE et E puis SW > C > S


print('\n=== pignistic transformation ===')
print('pignistic transformation of combined =', combined.pignistic())
print('pignistic transformation of m_1 =', m1.pignistic())
print('pignistic transformation of m_2 =', m2.pignistic())
print('pignistic transformation of m_3 =', m3.pignistic())

# Q5

print('\n=== test erreur estimations masses ===')
m1 = MassFunction([({'NW', 'N', 'E', 'SE'}, 0.45), ({'C', 'NE'}, 0.35), ({'W', 'SW', 'S'}, 0.2)])

print('\n=== Dempster\'s combination rule, unnormalized conjunctive combination (exact and approximate) ===')
print('Dempster\'s combination rule for m_1, m_2, and m_3 =', m1.combine_conjunctive(m2, m3))       # Q4
combined = m1.combine_conjunctive(m2, m3)
# Il faudrait concentrer les recherches dans les secteurs C puis SW > S > E > SE
# Une legère erreur dans l'estimation des masses change grandement le résultat


print('\n=== pignistic transformation ===')
print('pignistic transformation of combined =', combined.pignistic())