#mm1.py
#M/M/1 queue system simulator

import random,sys,numpy as np

# terms:
# k - the number of processed users observed in the simulation 
# n - the number of users who can enter the system 
# i - arrival counter 
# j - departure counter 
# IA - a sequence of interlude times 
# A - a sequence of arrival times 
# W - a sequence of job times 
# D - a sequence of with departure times 
# t_Q - a sequence of waiting times 
# t - a sequence of retention time in the system 
# t_stop - the moment of completion of the simulation 
# rho - average system utilization 
# N_Q - average number of users in the waiting room 
# T - average user retention in the system 
# T_Q - average user retention in the waiting room 

lambd = float(sys.argv[1])
mu = float(sys.argv[2])
k = int(sys.argv[3])

n,i,j = int(1.2*k),0,0
IA,W,A,D,t_Q,t=[],[],[],[],[],[]

for m in range(int(n)):
    IA.append(random.expovariate(lambd))
    W.append(random.expovariate(mu))
    A.append(sum(IA[0:m+1]))

D.append(A[0]+W[0])
i+=1

#event processing 
while(j<k):
    if(A[i]<D[j]):
        #arrival processing 
        i+=1
    else:
        #departure processing 
        t_Q.append(D[j]-A[j]-W[j])
        t.append(D[j]-A[j])
        j+=1
        if(j!=i):
            #the system is not empty 
            D.append(D[j-1]+W[j])
        else:
            #the system is empty 
            D.append(A[j]+W[j])


#processing and printing of results 
t_stop=D[k-1]
rho=sum(W[0:k])/t_stop
N_Q=sum(t_Q)/t_stop
T=sum(t)/k
T_Q=sum(t_Q)/k
np.disp([rho,N_Q,T,T_Q])
