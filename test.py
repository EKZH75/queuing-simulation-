import random
import numpy as np

# cette methode vient directement de queuing System mais comme je ne sais pas importer proprement
# je lai copie brutalement en changeant le nom pr eviter toute collision
#####neophyte # debutant # sagouin
def Increment_ww( nb_Q,Card_BS, lamb, mu ):  # choix d arrivee ou depart d un client
    param = (nb_Q*lamb)/(nb_Q*lamb + Card_BS*mu)
    value = np.random.binomial(1, param)
    return 2*value -1

N=10
lambbb, muuu = 1, 3
for n in range(1,N): # n := nbr_Q
    for  bs in range(1,5):
        print(" avec ", "n=",n , "bs =", bs,"increment =",  Increment_ww(n, bs, lambbb, muuu))

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

print("(1 == 1) =" , (1==1))

print(" on multiplie par 2 un false ", (1!=1)*1)

