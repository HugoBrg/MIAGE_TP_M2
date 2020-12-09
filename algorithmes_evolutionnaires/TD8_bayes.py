# Hugo BERANGER - M2 MIAGE IA

import pandas
import numpy
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb

#Q1
df = pandas.read_csv('kr-vs-kp.data')


#Q2
to_classify_str = "f,f,f,f,f,f,f,f,f,f,f,f,l,f,n,f,f,t,f,f,f,f,f,f,f,t,f,f,f,f,f,f,f,t,t,n"
to_classify_arr = to_classify_str.split(',')    #X
won  = "won"                                    #H

proba = numpy.zeros((36, 2))
cpt1 = 0
cpt2 = 0
for x in range(len(df.columns)-1):
    col = df[df.columns[x]]
    var = to_classify_arr[x]
    for z in range(len(col)):
        if col[z] == var:          
            if df.iloc[z][36] == "won":
                proba[x][0] += 1 
                cpt1+=1
            elif df.iloc[z][36] == "nowin" :
                proba[x][1] += 1 
                cpt2+=1
    
    diviseur = proba[x][0]+proba[x][1]
    #proba[x][0] = proba[x][0]/diviseur
    #proba[x][1] = proba[x][1]/diviseur
    proba[x][0] = proba[x][0]/len(col)
    proba[x][1] = proba[x][1]/len(col)
    diviseur  = cpt1+cpt2
    cpt1 = cpt1/diviseur
    cpt2 = cpt2/diviseur

print("Pour chaque attribut [win,nowin] : ")
print(proba)
print("Au total             [win,nowin] : ")
print(cpt1,cpt2)

pXwin = 1
pXnoWin = 1
for x in range(len(proba)):
    pXwin = pXwin * proba[x][0]
    pXnoWin = pXnoWin * proba[x][1]

print("p(X|win)                 : ",pXwin)
print("p(X|noWin)               : ",pXnoWin)
pXwinPwin = pXwin * cpt1
pXnoWinPnoWin = pXnoWin * cpt2
print("p(X|win) * p(win)        : ",pXwinPwin)
print("p(X|noWin) * p(noWin)    : ",pXnoWinPnoWin)

if (pXwinPwin > pXnoWinPnoWin):
    print("X est won")
else:
    print("X est noWin")


#Q3
noeud = [("hdchk","mulch"),("rxmsq","qxmsq"),("simpl","bkon8"),("wkcti","cntxt"),("wkna8","cntxt"),("bkspr","rxmsq"),("wkpos","cntxt"),("wkpos","wkna8"),
        ("bkona","bkspr"),("bkxcr","bkspr"),("dsopp","bkspr"),("dsopp","rxmsq"),("reskr","wkcti"),("reskr","wkpos"),("bkxbq","bkona"),
        ("bkxbq","bkxcr"),("bkxwp","bkxcr"),("dwipd","reskr"),("dwipd","wkcti"),("rimmx","bkxcr"),("blxwp","bkxwp"),("blxwp","rkxwp"),("r2ar8","dwipd"),
        ("wknck","rimmx"),("bknwy","mulch"),("bknwy","r2ar8"),("skrxp","bkona"),("skrxp","wknck"),("wkovl","r2ar8"),("bxqsq","bkxwp"),("bxqsq","rimmx"),
        ("bxqsq","rkxwp"),("bxqsq","wkovl"),("thrsk","bkxbq"),("thrsk","skrxp"),("wtoeg","cntxt"),("wtoeg","skrxp"),("skewr","cntxt"),("skewr","wtoeg"),
        ("katri","cntxt"),("katri","dwipd"),("katri","bkblk"),("class","bkxbq"),("class","bxqsq"),("class","rimmx"),("class","wknck"),("class","katri")]
valeurs = [["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],
        ["l","g"],["t","f"],["n","w"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],
        ["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["t","f"],["won","nowin"]]

bn=gum.BayesNet('chess')
print(bn)

added = []
print(len(noeud),len(valeurs))
y = 0
for x in range(len(noeud)):
    #print("----------------")
    #print(noeud[x])
    
    if(noeud[x][0] not in added):
        added.append(noeud[x][0])
        bn.add((gum.LabelizedVariable(noeud[x][0],noeud[x][0],valeurs[y])))
        y = y+1
    if(noeud[x][1] not in added):
        added.append(noeud[x][1])
        bn.add((gum.LabelizedVariable(noeud[x][1],noeud[x][1],valeurs[y])))
        y = y+1


for z in noeud:
    bn.addArc(*z)
    
print(len(added))
print(bn)

#gnb.configuration()
#gnb.showBN(bn,size="1")

