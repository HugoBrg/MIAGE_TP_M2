from OpenBayes import BNet, BVertex, DirEdge, JoinTree

G = BNet ("BotanicalProblem")

s = G.add_v(BVertex ("s", True, 2))
d = G.add_v(BVertex ("d", True, 2))
l = G.add_v(BVertex ("l", True, 2))

for e in [(s, l), (d, l)]:
    G.add_e(DirEdge(len(G.e), *e))

print(G)