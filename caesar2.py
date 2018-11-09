cipher = input("Enter your cipher text: ")
cipher = cipher.lower()
letters = list(cipher)

numbers = [0] * len(letters)

alphabet1 = ['#','#','#','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']

for i in range(len(letters)):
    if letters[i] in alphabet:
        numbers[i] = alphabet1.index(letters[i])
        numbers[i] = numbers[i]-3
        letters[i] = alphabet[numbers[i]]

final = ''.join(letters)
print("The decoded phrase is: " + final)
