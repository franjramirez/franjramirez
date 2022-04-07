#IF TWO LETTERS ARE THE SAME MAKE SURE TO NOT ERASE WORDS
#Make it so once a word is green, ignore that index

def helpRem(results, guess, words):
    orange = []
    green = []
    greenIndex = []
    index = 0
    wordListF = words

    for check in results:
        if(check == "g"):
            wordListF = remGreen(guess, wordListF,index) 
            green.append(guess[index])
            greenIndex.append(index)
        index += 1

    index = 0
    for check in results:
        if check == "o":
            wordListF = remOra(guess, wordListF, index) 
            orange.append(index)
        index += 1
    
    index = 0
    for check in results:
        if check == "n" and guess[index] not in green:
            wordListF = remNonHelp(guess, wordListF,index,orange, green, greenIndex)
        index += 1

    return wordListF


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
