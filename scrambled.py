## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

import random
import string

def scrambled_word(word):
    if len(word) > 3:
        wordlist = list(word)
        first = wordlist.pop(0)
        last = wordlist.pop(len(wordlist)-1)
        punctuation = []
        while last in string.punctuation:
            punctuation.append(last)
            last = wordlist.pop(len(wordlist) - 1)
        random.shuffle(wordlist)
        word = ''.join(wordlist)
        newWord = first + word + last
    else:
        newWord = word
    return newWord

def remove_punct(word):
    punct = ["!", ".", ",", "?",";", ":"]
    add = ['']
    wordlist = list(word)
    for i in range(len(punct)):
        while punct[i] in wordlist:
            ad = wordlist.pop()
            add.append(ad)
    word = ''.join(wordlist)
    add.reverse()
    addAll = ''.join(add)
    return word, addAll

# get user input and seperate words
entered_sent = input("Enter your text: ")
sepWords = entered_sent.split(" ")

# seed random number
seed = int(input("Enter a seed (0 for random): "))
if seed != 0:
    random.seed(seed)

length = len(sepWords)
newWord = ["0"]*length
for i in range(length):
    sepWords[i], add = remove_punct(sepWords[i])
    newWord[i] = scrambled_word(sepWords[i])
    newWord[i] = str(newWord[i]) + add

final = ' '.join(newWord)
print("Your scrambled sentence is: " + final)
