def quicksort(sequenza):
    if len(sequenza)==1: #mi fermo quando la sequenza che passo per parametro ha solo 1 elemento
        return sequenza
    else:
        #1) scegliere pivot
        pivot=sequenza[0] #prendo quello in prima posizione --> non troppo furbo perchè se è un numero molto grande o molto piccolo avrò le due sottoliste sbilanciate
        #2) dividere seuqueza in sottosequenza
        sequenza_smaller=[]
        sequenza_larger=[]
        sequenza_pivot=[]
        for i in sequenza:
            if i<pivot:
                sequenza_smaller.append(i)
            elif i>pivot:
                sequenza_larger.append(i)
            else:
                sequenza_pivot.append(i)
        return (quicksort(sequenza_smaller)+sequenza_pivot+quicksort(sequenza_larger))

if __name__=="__main__":
        sequenza=[3,5,2,9,11,4,7]
        print(quicksort(sequenza))
