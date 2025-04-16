def quadrato_magico(N): #N=dimensione lato
    rimanenti=[]
    for i in range(N*N):
        rimanenti.append(i)
    ricorsione([],rimanenti,N) #i rimanenti sono tutti i numeri fino ad N^2

def ricorsione(parziale,rimanenti,N):
    if len(parziale)==N*N: #ho finito quando nella lista di parziale ho N*N numeri, che è il numero di numeri totali nel quadrato di lato N
        print(parziale)

    else:
        for i in range(len(rimanenti)):
            numero=rimanenti[i]
            parziale.append(numero)
            nuovi_rimanenti=rimanenti[:i]+rimanenti[i+1:] #salto l'i-esimo numero
            ricorsione(parziale,nuovi_rimanenti,N)
            parziale.pop()


if __name__=='__main__':
    quadrato_magico(3)
