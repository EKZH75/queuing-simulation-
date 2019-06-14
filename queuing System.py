

import numpy as np




   #############################################
   # _w means that the considered method contains some randomness

def WaitingTime_w(nb_Q, Card_BS,lamb, mu, ): # temps d attente a un etat donne parametre par les arguments
    param = nb_Q*lamb + Card_BS*mu #taux total d une arrivee
    return np.random.exponential(param)

def Increment_w( nb_Q,Card_BS, lamb, mu ):  # choix d arrivee ou depart d un client
    param = (nb_Q*lamb)/(nb_Q*lamb + Card_BS*mu)
    value = np.random.binomial(1, param)
    return 2*value -1

#def CoalescingNewJobs() ;:= il suffit de tirer au hasard un entier plus petit que nb_Q

def idle():
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


    def __init__(self, nb_Q =2, nb_S = 1, lamb = 1, mu =1.3,Vect_Jobs =[0,0],Vect_Serv=[0,0]):

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

    def NonEmptyQ(self):
        return

    def EmptyQ(self):
        return

    def ProcessingUntill_Time(self, TimeHorizon):

        time =0
        WT_cour =0

        BS_cour = self.On_ProcessQ() # index where lie the busy servers
        Card_BS_cour = len(BS_cour)


        LUQ_cour = self.Left_UnprocessedQ() # index of queues non empty but left unprocessed
        Card_LUQ_cour = len(LUQ_cour)

        while(time<TimeHorizon):

            #on tire le temps d attente du prochain evt, ce peut etre une arrivee ou un depart
            WT_cour = WaitingTime_w(self.nbr_Q, Card_BS_cour, self.arrival_rate, self.service_rate)
            time += WT_cour

            #on tire si on charge ou on vide
            incr = Increment_w(self.nbr_Q, Card_BS_cour, self.arrival_rate, self.service_rate)

            ####################### UPDATE + : si une requete arrive #################################

            if incr ==1:

                #on tire une file au hasard
                index_chosen_to_increment = np.random.random_integers(0,self.nbr_Q -1)
                #on incremente la file choisie au hasard
                self.Vect_Jobs[index_chosen_to_increment] +=1

                #si on tombe dans une file vide et qu il existe un serveur disponible
                if self.Vect_Jobs[index_chosen_to_increment] ==0 and self.nb_S > Card_BS_cour:

                    # on remet a jour les BS_cour et Card_BS_cour
                    Card_BS_cour += 1
                    BS_cour.append(index_chosen_to_increment)

                    #on remet a jour l etat general
                    self.Vect_Jobs[index_chosen_to_increment] =1

                #si on tombe dans une file non vide ou qu aucun serveur est dispo
                else:
                    idle()

            ###################### UPDATE - : si un BS_cour conclut une requete ############################

            if incr ==-1:

                #on tire au hasard quelle file  en cours de traitement se vide de 1
                IndexServ_finishing_his_task = np.random.choice(BS_cour)

                #mise a jour de l etat general
                self.Vect_Jobs[IndexServ_finishing_his_task] -= 1
                self.Vect_Serv[IndexServ_finishing_his_task] =0

                #mise a jour des variables courantes
                BS_cour.remove(IndexServ_finishing_his_task)  # on la sort des Q under process

                # si la file choisie nest tjs pas vide
                if self.Vect_Jobs[IndexServ_finishing_his_task] >= 1:
                    LUQ_cour.append(IndexServ_finishing_his_task)     # on la range dans les Q left Unprocessed

                # dans le cas contraire on va la rajouter au set des emptyQ
                if self.Vect_Jobs[IndexServ_finishing_his_task]==0:
                    idle()

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

        return



QSystem_test_1 = QSystem()

QSystem_test_1.ProcessingUntill_Time(10)









































