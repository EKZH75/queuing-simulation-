import random
import numpy as np

val = random.uniform(0,1)

def uniformefacile(nbTirage):
    tab = []
    for k in range(nbTirage):
        tab.append(random.uniform(0,1))

    return tab

def moyenne( tabb):
    moy= 0
    for elt in tabb:
        moy += elt

    return moy
"""
print("val = ",val)
print (uniformefacile(10))
print("moyenne a 100 =",moyenne(uniformefacile(100))) 

tab =[]
valeur= 10
tab.append(valeur)
valeur = 12
tab.append(valeur)
print(tab)
print(valeur)
print(tab[0])
print(hex(id(tab[0])))
 
 """

WaitingTime = [1,2,2,1,2,2,2,3,3,1,1]
#InstantJump = np.cumsum(WaitingTime)

"""
for k in range(20):
    aleat = np.random.random_integers(1, 10)
    print("aleat = ",k, "   ", aleat)
"""

for k in range(20):
    choisis_au_hasard_parmi = random.choice([1,1,1,1,2,0])
    print("choisis_au_hasard_parmi", choisis_au_hasard_parmi)


print(np.sum(WaitingTime))
