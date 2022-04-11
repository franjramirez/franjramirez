from analyzer import analyzer
from wordList import wordList
from helperRemove import helpRem
from answerList import answerList
with open('wordle-solution.txt', 'w') as text:
    attempts = 0
    wordsAnalyzed = 1
    solved = False #False until it is either solver or exited
    words = wordList()
    CHECKWORDS = answerList()#Creates the initial list of all the words
    reachedEnd = 0
    counter = 0
    for word in CHECKWORDS:
        #Iteration until wordle is solved
        solutions = []
        solved = False
        words = wordList()
        attemptNum = 1
        print(wordsAnalyzed)
        while solved == False:
            wordle = analyzer(words, attemptNum) #Calls analyze() to return most probable word
            solutions.append(wordle)
            result = ''
            index = 0
            if len(words) != 0:
                for letter in wordle:
                    if (letter == word[index]):
                        result += 'g'
                    elif(letter in word):
                        result += 'o'
                    elif letter not in word:
                        result += 'n'
                    index += 1
            if word == wordle:
                counter += 1
                wordsAnalyzed += 1
                attempts += len(solutions)
                solved = True
                solutions = ",".join(solutions) + "\n"
                text.write(solutions)
            #Else, offer two words in order to get rid of 50/50 chance at the end
            else:
                words = helpRem(result, wordle, words)
                attemptNum += 1
    text.close()
    print(attempts/2315)


