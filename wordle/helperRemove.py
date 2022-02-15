def helpRem(results, guess, words):
    orange = ''
    green = ''
    greenIndex = []
    index = 0
    for check in results:
        if(check == "g"):
            words = remGreen(guess, words,index) 
            green += guess[index]
            greenIndex.append(index)
        index += 1

    index = 0
    for check in results:
        if check == "o":
            words = remOra(guess, words, index) 
            orange += guess[int(index)]
        index += 1
    
    index = 0
    for check in results:
        if check == "n":
            words = remNonHelp(guess, words,index,orange, green, greenIndex)
        index += 1

    return words

def remNonHelp(guess, words, index, orange, green, greenIndex):
    
    if (guess[index] not in orange) & (guess[index] not in green):
        newList = []
        newList = [word for word in words if (guess[index] not in word)]
    elif (guess[index] in green):
        newList = []
        for indexs in greenIndex: 
            for word in words:
                if (guess[index] not in word[not index]) and (guess[index] == guess[indexs]):
                    newList.append(word)
    return newList

    

def remGreen(guess, words, index):
    words = [x for x in words if guess[index] is x[index]]
    return words

def remOra(guess, words, index):
    newList = []
    for word in words:
        if (guess[index] != word[index]) & (guess[index] in word):
            newList.append(word)
    return newList

    
