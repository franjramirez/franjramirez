from probabilityHelper import helperOcc 
from probabilityHelper import helperProb

def analyze(words):
    #If only one word no need to analyze
    if len(words) == 1:
        theWord = words[0]  
        return theWord
    #If 0 words it would cause an error
    elif len(words) == 0:
        theWord = "Word is not in bank"
        return theWord
    else:
        letter1Occurence = [0] * 26 #How many times a letter shows up in index 0
        letter2Occurence = [0] * 26 #How many times a letter shows up in index 1
        letter3Occurence = [0] * 26 #How many times a letter shows up in index 2
        letter4Occurence = [0] * 26 #How many times a letter shows up in index 3
        letter5Occurence = [0] * 26 #How many times a letter shows up in index 4
        letterProbability1 = [0] * 26 #Will calculate the letter probability at that position
        letterProbability2 = [0] * 26 #Will calculate the letter probability at that position
        letterProbability3 = [0] * 26 #Will calculate the letter probability at that position
        letterProbability4 = [0] * 26 #Will calculate the letter probability at that position
        letterProbability5 = [0] * 26 #Will calculate the letter probability at that position
        count = 0 
        
    
        letter1Occurence = helperOcc(words,0) #Checks the first letter of each word and sees which one has the most occurences
        letter2Occurence = helperOcc(words,1) #Checks the second letter of each word and sees which one has the most occurences
        letter3Occurence = helperOcc(words,2)  #Checks the third letter of each word and sees which one has the most occurences
        letter4Occurence = helperOcc(words,3)  #Checks the fourth letter of each word and sees which one has the most occurences
        letter5Occurence = helperOcc(words,4)  #Checks the fifth letter of each word and sees which one has the most occurences

        #If its bigger than 2 words, return 2 words to give user more choice
        if len(words) >= 2:
            count = 0
            for letter in letter1Occurence:
                letterProbability1[count] = letter / len(words)     
                letterProbability2[count] = letter2Occurence[count] / len(words)
                letterProbability3[count] = letter3Occurence[count] / len(words)
                letterProbability4[count] = letter4Occurence[count] / len(words)
                letterProbability5[count] = letter5Occurence[count] / len(words)
                count += 1
            
            #Calculates the probability of each letter of a specific word
            word1 = helperProb(letter1Occurence,words,0)
            word2 = helperProb(letter2Occurence,words,1)
            word3 = helperProb(letter3Occurence,words,2)
            word4 = helperProb(letter4Occurence,words,3)
            word5 = helperProb(letter5Occurence,words,4)

            #Creates list for the words as probabilities
            wordsAsProbabilities = [0] * len(words)
            count = 0
            
            #Calculate each word probability
            for word in words:
                wordsAsProbabilities[count] = word1[count] * word2[count] * word3[count] * word4[count] * word5[count]
                count +=1 
            
            #Choose max
            theWord = max(wordsAsProbabilities)
            theWord = words[wordsAsProbabilities.index(theWord)]
            listForTwo = wordsAsProbabilities
            listForTwo.remove(max(wordsAsProbabilities))
            listForTwo = max(wordsAsProbabilities)
            listForTwo = [theWord, words[wordsAsProbabilities.index(listForTwo)]]
            return listForTwo
