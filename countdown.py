#voglio fare una funzione ricorsiva che effettui un countdown
from time import sleep


#COUNTDOWN ITERATIVO:
def countdown(n):
    while n > 0:
        print(n)
        sleep(0.5) #metto una pausa per visualizzare meglio il countdown
        n-=1

#COUNTDOWN RICORSIVO
def countdown_recursive(n):
    if n<=0: #contiene la condizione terminale
        print("Stop")
    else: #scompongo il problema
        print(n)
        sleep(0.5)
        counter=n-1
        countdown_recursive(counter) #chiamo la funzione su questo counter --> n ora ha un valore uguale a counter!!
#quando faccio soluzione iterativa, rimango dentro l'istanza del metodo e itero su quello
#quando invece faccio ricorsivo --> chiamo TANTE volte lo stesso metodo (creo STACK di chiamate) --> faccio una chiamata per ogni valore di n
#il meccanismo fa accrescere lo stack di chiamate della stessa funzione, quando si arriva al problema piu piccolo possibile, TUTTE le chiamate che abbiamo fatto vengono terminate con effetto a catena (UNWINDING CALL STACK)

if __name__ == '__main__':
    #countdown(10)
    countdown_recursive(10)
