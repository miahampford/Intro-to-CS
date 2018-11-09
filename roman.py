## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

#Enter integer
number = int(input("Enter an integer: "))
copy = number
roman = []

#1000(M):
while number >= 1000:
    number = number - 1000
    roman.append("M")

#900(CM):
if number >= 900 and number < 1000:
    number = number - 900
    roman.append("CM")

#500(D):
if number >= 500 and number < 900:
    number = number - 500
    roman.append("D")

#400(CD):
if number >= 400 and number < 500:
    number = number - 400
    roman.append("CD")

#100(C):
while number >= 100:
    number = number - 100
    roman.append("C")

#90(XC):
if number >= 90 and number < 100:
    number = number - 90
    roman.append("XC")

#50(L):
if number >= 50 and number < 90:
    number = number - 50
    roman.append("L")

#40(XL):
if number >= 40 and number < 50:
    number = number - 40
    roman.append("XL")

#10(X):
while number >= 10:
    number = number - 10
    roman.append("X")

#9(IX):
if number == 9:
    number = number - 9
    roman.append("IX")

#5(V):
if number >= 5 and number < 9:
    number = number - 5
    roman.append("V")

#4(IV):
if number == 4:
    number = number - 4
    roman.append("IV")

#1(I):
while number > 0:
    number = number - 1
    roman.append("I")

#Display final answer
if copy > 3999 or copy < 1:
    print("Input must be between 1 and 3999")
else:
    final = ''.join(roman)
    print("In roman numerals, " + str(copy) + " is " + final)
