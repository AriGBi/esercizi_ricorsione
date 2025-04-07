def palyndrome(word):
    if len(word) ==1 or len(word)==0: #in base a se la stringa ha un numero pari o dispari di lettere
        return True #quando ho una sola lettera per forza è palindroma
    else:
        #devo verificare che la prima e l'ultima lettera siano uguali e che tutto ciò che sta in mezzo è palindromoo
        return (word[0]==word[-1]) and palyndrome(word[1:-1])


#si poteva fare anche così:
def palyndrome_banale(word):
    return word==word[::-1] #se la parola è uguale al suo inverso viene True se no False
    #funziona solo perchè python ha gia implementato l'inversione di una stringa

if __name__ == '__main__':
    print(palyndrome('casa')) #mi aspetto False
    print(palyndrome('civic')) #mi aspetto True

    print(palyndrome_banale('casa'))
    print(palyndrome_banale('civic'))
