
#import and include

import random
import numpy as np

print("Hello world ")

def increment_w( lamb,mu): # lamb = taux d arrivees des requetes et mu = taux de gestion
                            # et on suppose que l etat nest pas a zero
    w= random.uniform(0,1)
    if w <= lamb/(lamb+mu): # alors on penche du cote arrivee
        return 1
    else: return -1




def WT_w(lamb, mu): # temps dattente pour une file MM1 av flots de clients  lambda et un seul serveur a taux mu
    param = lamb+mu
    return np.random.exponential(param)

def WT_a_zero_w(lamb): #ici on ne prend que le taux d arrivees
    return np.random.exponential(lamb)


