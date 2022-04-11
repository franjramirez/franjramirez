from analyze import analyze
from wordList import wordList
from helperRemove import helpRem
from mainPersonalize import main
import tkinter as tk

def go():
    global refresh
    global word
    global go_buttond
    global attempted

    word = search_entry.get()
    word = word.lower()
    refresh = True
    if attempted:
        go_buttond = tk.Button(lower_frame, text="Go!",highlightbackground= 'white',bg = 'white', width=5, command=answer)
        go_buttond.pack()
        attempted = False

def answer():
    global listWords
    global attemptNumber
    global attempted

    result = wordResult_entry.get()
    listWords  = helpRem(result, word, listWords)
    print(listWords)
    wordle = analyze(listWords, attemptNumber)
    print(listWords)
    print(attemptNumber)
    if(len(listWords) == 1):
        word1_label['text'] = f'The word is {wordle}'
        word2_label['text'] = 'Congrats'
    elif len(listWords) == 0:
        word1_label['text'] = 'Word was not found'
        word2_label['text'] = 'Sorry'
    else:
        word1_label['text'] = wordle[0]
        word2_label['text'] = wordle[1]

    numWords['text'] = f"Number of words left: {len(listWords)}"
    go_buttond.destroy()
    attempted = True
    attemptNumber += 1


def restart():
    global listWords
    global attemptNumber

    listWords = wordList()
    numWords['text'] = f"Number of words left: {len(listWords)}"
    wordle = analyze(listWords, attemptNumber)
    word1_label['text'] = wordle[0]
    word2_label['text'] = wordle[1]
    attemptNumber = 1

attempted = True
attemptNumber = 1
word = 'didnt update'
listWords = wordList()
solved = False
wordle = analyze(listWords, attemptNumber)

#Create the root
root = tk.Tk()

#Create my canvas
canvas = tk.Canvas(root, width = 500, height = 400, bg = '#d8f6fa')
canvas.pack()

#Create frame
frame = tk.Frame(root, bg = 'white')
frame.place(relheight= .28,relwidth=.8, relx= .1, rely=.1)

#Create the widgets
search_label = tk.Label(frame, text="Enter word inputted here:", fg = 'black',bg = 'white')
search_entry = tk.Entry(frame, bg = 'white', bd = 2, fg = 'black')
search_label.pack()
search_entry.pack()
go_button = tk.Button(frame, text="Go!",highlightbackground= 'white',bg = 'white', width=5, command=go)
go_button.pack()

numWords = tk.Label(frame, text=f"Number of words left: {len(listWords)}", fg = 'black',bg = 'white')
numWords.pack()

lower_frame  = tk.Frame(root, bg = 'white')
lower_frame.place(relheight= .4,relwidth=.8, relx= .1, rely=.4)
suggest_label = tk.Label(lower_frame, text="Suggested words:", fg = 'black',bg = 'white')
word1_label = tk.Label(lower_frame, text= wordle[0], fg = 'black',bg = 'white')
word2_label = tk.Label(lower_frame, text=wordle[1], fg = 'black',bg = 'white')    

suggest_label.pack()
word1_label.pack()
word2_label.pack()

wordResult_label = tk.Label(lower_frame, text="What was the result? (green = g, orange = o, none = n)", fg = 'black',bg = 'white')
wordResult_entry = tk.Entry(lower_frame, bg = 'white', fg = 'black')
wordResult_label.pack()
wordResult_entry.pack(pady=5)

restartButton = tk.Button(root, text = 'Restart', width = 5, command = restart)
restartButton.pack()

root.mainloop()