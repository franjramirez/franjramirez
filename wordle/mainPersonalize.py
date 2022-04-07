from analyze import analyze
from wordList import wordList
from helperRemove import helpRem



def main():
    # Beggining VARIABLES 
    solved = False #False until it is either solver or exited
    words = wordList() #Creates the initial list of all the words
    #Iteration until wordle is solved
    while solved == False:
        wordle = analyze(words) #Calls analyze() to return most probable word
        #If there is one word left, declare it as the words
        if len(words) == 1:
            print(f"The word is {wordle}")
            solved = True
        #Else, offer two words in order to get rid of 50/50 chance at the end
        elif len(words) > 1:
            print(f"\nThe calculated words are: {wordle[0]}(More probable) or {wordle[1]}(Less Probable)")
            print(f"There are {len(words)} words left")
            #Get input from user on what the wordle output is 
            word = input("\nWhat word did you input? ")
            result = input("What was the result? (green = g, orange = o, none = n) TO QUIT INPUT -1: ")
            #Offer an end to the iteration
            if result == "-1":
                print("\nFair enough")
                solved = True
            #Remove the words based on the wordle output
            elif result == ' ':
                print(words)
            else:
                words = helpRem(result, word, words)
        else:
            print("Word is not in bank, sorry")
            solved = True
            
        
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()