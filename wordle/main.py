from analyze import analyze
from wordList import wordList
from readScreen import readScreens
from helperRemove import helpRem



def main():
    #VARIABLES
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
            result = input("\nWhat was the result? (green = g, orange = o, none = n) TO QUIT INPUT -1: ")
            #Offer an end to the iteration
            if result == "-1":
                print("\nFair enough")
                solved = True
            #Remove the words based on the wordle output
            else:
                check = False
                while check == False:
                    option = int(input("Did you input first or second option "))
                    if option == 1 or option == 2:
                        check = True
                    else: 
                        print("Invalid input")
                words = helpRem(result, wordle[option-1], words)
        else:
            print("Word is not in bank, sorry")
            solved = True
            
        
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()