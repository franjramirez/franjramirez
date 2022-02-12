
def helpRem(results, guess, words):
    index = 4
    while index >= 0:
        if(results[index] == "n"):
            words = remNonHelp(guess, words,index)
        elif results[index] == "g":
            words = remGreen(guess, words,index) #Cuts in half
        elif results[index] == "o":
            words = remOra(guess, words, index) #Maybe works
        index -= 1
    return words

def remNonHelp(guess, words, index):
    words = [word for word in words if not guess[index] in word]
    return words

    

def remGreen(guess, words, index):
    words = [x for x in words if guess[index] is x[index]]
    return words

def remOra(guess, words, index):
    #newList = [word for word in words if (guess[index] in words) and not (guess[index] is words[index])]
    newList = []
    for word in words:
        if (guess[index] != word[index]) & (guess[index] in word):
            newList.append(word)
    return newList



 


    
