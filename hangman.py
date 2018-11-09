## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

guess = True

#input word and create lists
hangman = input("Enter a word: ")
hangman = hangman.upper()
list = list(hangman)
word = ["-"] * len(hangman)
count = 6

while count > 0:
    wordstr = ''.join(word)
    letter = input("[%s] You have %s left, enter a letter: " % (wordstr, count))
    letter = letter.upper()

    if letter in list:
        for i in range(len(list)):
            if letter == list[i]:
                word[i] = list[i]
        if "-" not in word:
            print("You win! The word was \"" + hangman + "\"")
            count = 0
        else:
            print("Correct!")

    else:
        count = count - 1
        if count == 0:
            print("You lose! The word was \"" + hangman + "\"")
        else:
            print("Incorrect!")