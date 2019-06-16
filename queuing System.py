

import numpy as np
import matplotlib.pyplot as plt



   #############################################
   # _w means that the considered method contains some randomness

def WaitingTime_w(nb_Q, Card_BS,lamb, mu, ): # temps d attente a un etat donne parametre par les arguments
    """

    :param nb_Q: nbr de files au total
    :param Card_BS: nb de busy servers au total
    :param lamb: taux darrivee
    :param mu: taux de service
    :return: temps d attente du prochain evenement , ce peut etre une arrivee ou un depart
    """
    param = nb_Q*lamb + Card_BS*mu #taux total d une arrivee
    return np.random.exponential(param)

def Increment_w( nb_Q,Card_BS, lamb, mu ):  # choix d arrivee ou depart d un client
    param = (nb_Q*lamb)/(nb_Q*lamb + Card_BS*mu)
    print("nb_Q = ", nb_Q, "Card_BS = ", Card_BS, "lamb = ", lamb, "mu = ", mu)
    print("param  = ", param )
    value = np.random.binomial(1, param)
    print("value = ", value )
    return 2*value -1

#def CoalescingNewJobs() ;:= il suffit de tirer au hasard un entier plus petit que nb_Q

def idle():
    return



def Data_Reformatting(Histo_IJD, Histo_IoS, Histo_SI, Init_Vect_Jobs, nbr_Q):

    #IJD := Inter-arrival Jump Duration
    #IoS := Index of Spiking
    #SI  := Sign Increment

    abcisse  = np.cumsum(Histo_IJD)
    nbr_J = len(Histo_IJD) ## ie le nb de Jumps
    GlobalOrdonnees = []

    # on initialise les coordonnes globales
    for k in range(nbr_Q):
        GlobalOrdonnees.append([Init_Vect_Jobs[k]]) # on ajoute une petite liste a un elt dans

    print(GlobalOrdonnees) # on est cense avoir que les cond ini donc un format nbr_Q x 1

    #on obtient ainsi un tableau de format nbr_Q x 1

    for k in range(1,nbr_J): # k := pas de temps
        for n in range(nbr_Q): # n := index de file
            # definit la k ieme val de la n ieme file comme la derniere valeur d avant plus l increment si la n ieme spike
            GlobalOrdonnees[n].append(GlobalOrdonnees[n][k-1] + Histo_SI[k]*(Histo_IoS[k]==n) )

    #la matrice d ordonnees est remplie et contient des fonctions constantes pm
    return abcisse, GlobalOrdonnees

def plot_QSystem(abcisse, GC, nbr_Q): # où GC := global coordonnees ie un tableau a N entrees (nbr_Q) x history of each queue
    for n in range(nbr_Q):
        plt.plot(abcisse, GC[n])
    plt.show()
    return


class QSystem:
    """
    Nb_Q := total number of queues
    Nb_Serv := total number of servers
    lambda, mu := arrival and processing rates

    Vect_Jobs[k] := nb of jobs waiting at the kth queue
    Vect_Serv[k] := presence (1) or not (0) at the kth Queue



    one queue  = nb of jobs still waiting to be processed

    list of busy servers            Busy_S
    list of iddling servers         Idd_S
    list of nonempty queues t in term of jobs) left unprocessed

    """


    def __init__(self, nb_Q =2, nb_S = 1, lamb = 1, mu =2,Vect_Jobs =[0,0],Vect_Serv=[0,0]):

        #  number of queues
        # nb_S nb of servers
        # normalement longueur de Vect_Jobs =longueur de Vect_Serv= nb_Q sinon envoyer une erreur

        self.nbr_Q = nb_Q
        self.nb_S = nb_S
        self.arrival_rate =lamb
        self.service_rate =mu

        self.Vect_Jobs = Vect_Jobs
        self.Vect_Serv = Vect_Serv

        ##### decrit completement letat du systeme

    def On_ProcessQ(self): ### liste d indexs des files under process ie les busyservers
        OPQ =[]

        for k in range(self.nbr_Q):
            if self.Vect_Serv[k]==1:        # si il ya un seveur a la k ieme file
                OPQ.append(k)               #on  ajoute a la liste des files/ serveurs busy

        return OPQ

    def Left_UnprocessedQ(self): # liste des indexes des files non vides et laissees pour compte
        LUP = []

        for k in range(self.nbr_Q):
            if self.Vect_Serv[k]==0 and self.Vect_Jobs[k] >=1: #il n ya pas de serveurs dans la file k et il ya des requetes en attente
                LUP.append(k)

        return LUP

    def NonEmptyQ(self): # liste d index des files non vides
        return

    def EmptyQ(self):
        return


    def Transition_Arrival(self,BS_cour,Card_BS_cour,LUQ_cour, Card_LUQ_cour ):
        print("arrivee d un Job")

        # on tire une file au hasard
        index_chosen_to_increment = np.random.random_integers(0, self.nbr_Q - 1)
        print("on tire au hasard la file = ", index_chosen_to_increment)


        # si on tombe dans une file vide et qu il existe un serveur disponible
        if self.Vect_Serv[index_chosen_to_increment] == 0 and self.nb_S > Card_BS_cour:

            # on remet a jour les BS_cour et Card_BS_cour
            Card_BS_cour += 1
            BS_cour.append(index_chosen_to_increment)

            # on remet a jour l etat general, particulierement on assigne un serveur a la file choisie
            self.Vect_Serv[index_chosen_to_increment] = 1

        # si on tombe dans une file non vide ou qu aucun serveur est dispo
        else:
            idle()



        #####################################################
        #HistoIndex_of_Spik.append(index_chosen_to_increment)
        #####################################################

        # on incremente la file choisie au hasard
        self.Vect_Jobs[index_chosen_to_increment] += 1


        return
    
    def Transition_Departure(self, BS_cour, Card_BS_cour, LUQ_cour, Card_LUQ_cour):
        """

        :param BS_cour:
        :param Card_BS_cour:
        :param LUQ_cour:
        :param Card_LUQ_cour:
        :return: le self modifie, une file de BS_cour, une file de LUQ_cour
        """

        return self


    def ProcessingUntill_Time(self, TimeHorizon):

        time =0
        WT_cour =0

        ##########################donnees collectees pour tracer les courbes

        HistoInterJumpDurat = []  ##### duree entre deux jumps
        HistoIndex_of_Spik = []           ##### which queue spikes
        HistoSign_Increment = []       # if a new job arrives in the system or if a completed one leaves it

        #### next step : the server behaviour

        BS_cour = self.On_ProcessQ() # index where lie the busy servers
        Card_BS_cour = len(BS_cour)


        LUQ_cour = self.Left_UnprocessedQ() # index of queues non empty but left unprocessed
        Card_LUQ_cour = len(LUQ_cour)

        while(time<TimeHorizon):

            print("on affiche l objet queuing System ")
            print("self.Vect_Jobs = ", self.Vect_Jobs )
            print("self.Vect_Serv = ", self.Vect_Serv)
            print("liste des BS = ", BS_cour)
            print("liste des  LUQ = ", LUQ_cour)

            #on tire le temps d attente du prochain evt, ce peut etre une arrivee ou un depart
            WT_cour = WaitingTime_w(self.nbr_Q, Card_BS_cour, self.arrival_rate, self.service_rate)
            time += WT_cour

            ################################################ REFRESH HISTO
            HistoInterJumpDurat.append(WT_cour)
            ################################################

            #on tire si on charge ou on vide
            incr = Increment_w(self.nbr_Q, Card_BS_cour, self.arrival_rate, self.service_rate)
            print("incr = ", incr)

            ################################################ REFRESH HISTO
            HistoSign_Increment.append(incr)
            ################################################

            ####################### UPDATE + : si une requete arrive #################################

            if incr ==1:
                print("arrivee d un Job")

                #on tire une file au hasard
                index_chosen_to_increment = np.random.random_integers(0,self.nbr_Q -1)
                print("on tire au hasard la file = ", index_chosen_to_increment)

                #####################################################
                HistoIndex_of_Spik.append(index_chosen_to_increment)
                #####################################################

                #on incremente la file choisie au hasard
                self.Vect_Jobs[index_chosen_to_increment] +=1

                #si on tombe dans une file vide et qu il existe un serveur disponible
                if self.Vect_Serv[index_chosen_to_increment] ==0 and self.nb_S > Card_BS_cour:

                    # on remet a jour les BS_cour et Card_BS_cour
                    Card_BS_cour += 1
                    BS_cour.append(index_chosen_to_increment)

                    #on remet a jour l etat general, particulierement on assigne un serveur a la file choisie
                    self.Vect_Serv[index_chosen_to_increment] =1

                #si on tombe dans une file non vide ou qu aucun serveur est dispo
                else:
                    idle()

            ###################### UPDATE - : si un BS_cour conclut une requete ############################

            if incr ==-1:
                print("service effectue")

                #on tire au hasard quelle file  en cours de traitement se vide de 1
                IndexServ_finishing_his_task = np.random.choice(BS_cour)

                ############################################################# REFRESH HISTO
                HistoIndex_of_Spik.append(IndexServ_finishing_his_task)
                ############################################################


                #mise a jour de l etat general :on fait monentanement disparaitre un processeur mais on va le replacer apres
                self.Vect_Jobs[IndexServ_finishing_his_task] -= 1
                self.Vect_Serv[IndexServ_finishing_his_task] =0

                #mise a jour des variables courantes
                BS_cour.remove(IndexServ_finishing_his_task)  # on la sort des Q under process pour la prendre en compte parmi les lUQ
                Card_BS_cour -= 1
                # en plus si on prend nbr_Q grand, on ade grandes chances que le meme serveur ne retourne pas dans la meme file que juste avant


                # si la file choisie nest tjs pas vide
                if self.Vect_Jobs[IndexServ_finishing_his_task] >= 1:
                    LUQ_cour.append(IndexServ_finishing_his_task)     # on la range dans les Q left Unprocessed
                    Card_LUQ_cour +=1

                # dans le cas contraire on va la rajouter au set des emptyQ
                if self.Vect_Jobs[IndexServ_finishing_his_task]==0:
                    idle()
                    Card_LUQ_cour -= 1

                #maintenant on va replacer le processeur qui vient de finir
                # dans le cas ou il reste au moins une file laissee pour compte

                if Card_LUQ_cour >= 1:
                    # on tire au hasard une file
                    Index_Q_taken_over = np.random.choice(LUQ_cour)

                    #on remet a jour l etat general  remarque :  ici on peut verifier que lon a bien choisi une LUQ
                    self.Vect_Serv[Index_Q_taken_over]= 1

                    #on remet a jour les variables courantes
                    LUQ_cour.remove(Index_Q_taken_over) #on sort la Q nouvellement prise en charge du set des LUQ
                    Card_LUQ_cour -= 1

                    BS_cour.append(Index_Q_taken_over) # et on la rentre dans le set des prise en charge
                    Card_BS_cour +=1

                #dans le cas ou il ne reste pas de file non vide laissee pour compte
                else:
                    idle()
        print("HistoSign_Increment = ", HistoSign_Increment)
        return (HistoInterJumpDurat, HistoIndex_of_Spik, HistoSign_Increment)



QSystem_test_1 = QSystem()

Histo_IJD_test,Histo_IoS_test, Histo_SI_test =  QSystem_test_1.ProcessingUntill_Time(1000)

# def plot_QSystem(Histo_IJD, Histo_IoS, Histo_SI, Init_Vect_Jobs, nbr_Q):

#return abcisse, GlobalOrdonnees
abc, Glo_Ord = Data_Reformatting(Histo_IJD_test, Histo_IoS_test, Histo_SI_test, [0,0], 2)

plot_QSystem(abc, Glo_Ord, 2)











































