import MM1
import numpy as np
import matplotlib.pyplot as plt


Init_Value =0
nbOfClients = Init_Value
scale = []


class Queue:
    """le numero
    le taux darrivee
    le taux de gestion
    le nb de clients au temps t
    le nb de taches gerees etc

    arrival_rate := lamb for lambda
    service_rate := mu
    """

    def __init__(self, nmbr=0, lamb= 2, mu=1.3, Init_Value=0, InterJumps = [], Increments= []):
        # si lamb > mu : return error
        self.nbr = nmbr #numero de la file
        self.arrival_rate= lamb
        self.service_rate = mu
        self.Nb_Jobs = Init_Value
        self.HistoInterJump =  InterJumps   # coresspond aux attentes entre les sauts
        self.HistoIncrement = Increments

    def fillQueue_tillN(self, Capacity): # on met une borne sur la capacite
        WT =0
        increment =0
        while(self.Nb_Jobs<= Capacity):

            # on fait le tirage du  temps d attente et de l'increment

            if self.Nb_Jobs==0:
                WT = MM1.WT_a_zero_w(self.arrival_rate)
                increment =1 # on attend forcement qu un client arrive

            if self.Nb_Jobs >=1:
                WT = MM1.WT_w(self.arrival_rate, self.service_rate) # normalement arrival_rate < service_rate sinon ca dv
                increment = MM1.increment_w(self.arrival_rate, self.service_rate)


            # on met a jour les donnees de la file dattente
            self.HistoInterJump.append(WT) # on actualise l historique des interJumps
            self.HistoIncrement.append(increment)
            self.Nb_Jobs += increment
        return

    def PlotQueue(self):

        Abcisse = np.cumsum(self.HistoInterJump)
        Ordonnee = np.cumsum(self.HistoIncrement)

        plt.plot(Abcisse, Ordonnee, )
        plt.plot(Abcisse, Ordonnee, )

        plt.show()
        return

print(0)
Queue_0 = Queue()
Queue_0.fillQueue_tillN(10000)

Queue_0.PlotQueue()



