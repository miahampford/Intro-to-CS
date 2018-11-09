## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016


#Enter cipher
word = input("Please give me a word: ")
word = word.lower()
letters = list(word)
syllables = 0
adjacent = -5

for i in range(len(letters)):
    if letters[i] == "a" or letters[i] == "e" or letters[i] == "i" or letters[i] == "o" or letters[i] == "u" or letters[i] == "y":
        syllables = syllables + 1
        if adjacent == i-1:
            syllables = syllables - 1
        adjacent = i
        if letters[i] == "e" and len(letters) == adjacent+1:
            syllables = syllables - 1

if syllables == 0:
    syllables = 1

print("The word " + word + " has " + str(syllables) + " syllables.")