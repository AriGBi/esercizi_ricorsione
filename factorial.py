def factorial(n):
    if n<=1: #condizione terminale
        return 1
    else:
        counter=n-1
        return n * factorial(counter)

#se eseguo il debug, mi fa prima la chiamata alle varie funzioni e POI ritorna indietro mandando i risultati dei problemi + semplici e aumentando di nuovo n finchè non arriva al max

if __name__ == '__main__':
    print(factorial(4))
