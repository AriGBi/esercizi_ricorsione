def dichotomic(input_list,val): #ho una lista e devo vedere se val è al suo interno
    if len(input_list)==1:
        if input_list[0]==val:
            return True
        else:
            return False
    else:
        index=len(input_list)//2 #prendo l'indice della metà della lista
        return dichotomic(input_list[:index],val) or dichotomic(input_list[index+1:],val) #inefficiente perchè non ho controllato in quale sottolista potrebbe cadere ill numero

#pensare a casa a come implementare questo metodo confrontando con i valori a metà

if __name__=='__main__':
    input_list=[1,2,3,4,5,6,7] #lista ordinata
    print(dichotomic(input_list,5)) #True
    print(dichotomic(input_list,12)) #False
