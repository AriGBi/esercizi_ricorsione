def count_leaf_nodes(input_list):
    #passiamo una lista, questo metodo scorre tutti gli elementi della lista per contare quanti nodi ci sono (ovvero quanti elementi totali)
    #se un elemento è anch'esso una lista, incremento il contatore di 1 e chiamo di nuovo il metodo per gestirlo
    if len(input_list)==0:
        return 0

    else:
        counter=0
        for element in input_list:
            if type(element)==list: #se l'elemento è di nuovo una lista, riapplico il metodo ricorsivo per poterla dividere ulteriormente
                counter+=count_leaf_nodes(element)
            else: #se l'elemento non è una lista, ma un elemento singolo --> lo conto e basta
                counter+=1
        return counter


