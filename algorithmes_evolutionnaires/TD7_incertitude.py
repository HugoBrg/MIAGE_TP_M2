# Hugo BERANGER - M2 MIAGE IA

import pandas
import numpy

#####################Q1,Q2,Q3,Q4#####################
df = pandas.read_csv('yahoo_finance.csv')

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

print(st)

#####################Q5#####################
pr1 = 0 #[0,1]
pr2 = 0 #[0,-1]
pr3 = 0 #[1,0]

prst1 = 0
prstm1 = 0
prst0 = 0

for actual in st:
    if actual == 1 :
        prst1+=1
    elif actual == -1:
        prstm1+=1
    elif actual == 0:
        prst0+=1

    if previous == 0 and actual == 1:
        pr1+=1
    elif previous == 0 and actual == -1: 
        pr2+=1   
    elif previous == 1 and actual == 0:
        pr3+=1
    previous = actual

print("[0,1][0,-1][1,0]")
print(prst1,prstm1,prst0)
print(pr1,pr2,pr3)
pr1 = pr1/(len(st)-1)
pr2 = pr2/prstm1
pr3 = pr3/prst0
print(pr1,pr2,pr3)

#####################Q6#####################
coupleIndices = numpy.zeros(9)
for x in range(len(st)):
    if x > 2:
        stm3 = st[x-3]
        stm2 = st[x-2]
        stm1 = st[x-1]
        stm0 = st[x]
        #print(stm3, stm2, stm1, stm0)
        if stm3 == 0 and stm2 == 1:
            if stm1 == 0 and stm0 == 1:         #[0,1][0,1]
                coupleIndices[0] +=1
            elif stm1 == 0 and stm0 == -1:      #[0,1][0,-1]
                coupleIndices[1] +=1
            elif stm1 == 1 and stm0 == 0:       #[0,1][1,0]
                coupleIndices[2] +=1
        elif stm3 == 0 and stm2 == -1:
            if stm1 == 0 and stm0 == 1:         #[0,-1][0,1]
                coupleIndices[3] +=1
            elif stm1 == 0 and stm0 == -1:      #[0,-1][0,-1]
                coupleIndices[4] +=1
            elif stm1 == 1 and stm0 == 0:       #[0,-1][1,0]
                coupleIndices[5] +=1
        elif stm3 == 1 and stm2 == 0:
            if stm1 == 0 and stm0 == 1:         #[1,0][0,1]
                coupleIndices[6] +=1
            elif stm1 == 0 and stm0 == -1:      #[1,0][0,-1]
                coupleIndices[7] +=1
            elif stm1 == 1 and stm0 == 0:       #[1,0][1,0]
                coupleIndices[8] +=1
print(coupleIndices)

#####################Q8#####################
#Grace aux probabilités de la question 5 on peut déduire que l'augmentation est le changement d'indice qui est apparue le plus l'année passée (109) suivie de près par la baisse (106), 
#en revanche la stabilisation après une augmentation est arrivée peu de fois (38).

#On peut aussi observer que quand une stabilisation apparait c'est très souvent après une augmentation (0.3157894736842105)

#Grace à la question 6 on peut observer que le couple le plus apparue est [0,-1][0,-1] (3 fois): Une baisse après une stabilisation suivie d'une autre stabilisdation et d'une autre baisse.
#Le second couple le plus apparue est [1,0][0,-1] (2 fois): Une stailisation après une augmentation suivie d'une autre stabilisation et enfin une baisse.



#####################Q9#####################
#Un agent intelligent pourrait observer les changements d'indices apparaissant le plus souvent par rapport aux précédentes changements d'indices et acheter ou vendre en conséquence.