## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

#initialize variables
sum1 = 0
double = []

#get card number
cardNumber = input("Type a credit card number (just digits): ")
numbers = list(cardNumber)
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

#step 1
for i in range(len(numbers)-1, -1, -2):
    sum1 += numbers[i]

#step 2
for i in range(len(numbers)-2, -1, -2):
    double.append(numbers[i]*2)
for i in range(len(double)):
    if double[i] >= 10:
        double.append(1)
        double[i] = double[i]-10

sum2 = sum(double)

#step 3
sum3 = sum1 + sum2

#step 4
if sum3 % 10 == 0:
    print("Yes, " + cardNumber + " is a valid credit card number")
else:
    print(cardNumber + " is not a valid credit card number")