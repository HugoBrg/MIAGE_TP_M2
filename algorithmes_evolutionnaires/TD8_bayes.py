# Hugo BERANGER - M2 MIAGE IA

import pandas
import numpy

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
    proba[x][0] = proba[x][0]/diviseur
    proba[x][1] = proba[x][1]/diviseur
    diviseur  = cpt1+cpt2
    cpt1 = cpt1/diviseur
    cpt2 = cpt2/diviseur

print("Pour chaque attribut [win,nowin] : ")
print(proba)
print("Au total             [win,nowin] : ")
print(cpt1,cpt2)

