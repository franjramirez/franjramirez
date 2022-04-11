#IF TWO LETTERS ARE THE SAME MAKE SURE TO NOT ERASE WORDS
#Make it so once a word is green, ignore that index

def helpRem(results, guess, words):
    orange = []
    green = []
    greenIndex = []
    index = 0

    for check in results:
        if(check == "g"):
            words = remGreen(guess, words,index) 
            green.append(guess[index])
            greenIndex.append(index)
        index += 1
    index = 0
    for check in results:
        if check == "o":
            words = remOra(guess, words, index) 
            orange.append(index)
        index += 1
    index = 0
    for check in results:
        if check == "n" and guess[index] not in green:
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
    newList = []
    for word in words:
        if guess[index] == word[index] :
            newList.append(word)
    return newList

def remOra(guess, words, index):
    newList = []
    for word in words:
        if (guess[index] != word[index]) & (guess[index] in word):
            newList.append(word)
    return newList
