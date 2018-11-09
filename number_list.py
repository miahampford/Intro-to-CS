## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016


#numbers
number = [0]*5
sum = 0
sum2 = 0

#input numbers
number[0]= int(input("Number 1: "))
number[1]= int(input("Number 2: "))
number[2]= int(input("Number 3: "))
number[3]= int(input("Number 4: "))
number[4]= int(input("Number 5: "))
print()

#display list
print("You entered:", number)

#find average
for i in range(5):
    sum = sum + number[i]
avg = sum/5
print("The average is:", avg)

#make a copy
copy = number[:]

#find range
copy.sort()
rang = copy[4]-copy[0]
print("The range is:", rang)

#remove an item
rem = int(input("Which item do you want to remove? "))
number.remove(rem)
print()

#display new list
print("The new list has the following values:", number)

#find average
for i in range(4):
    sum2 = sum2 + number[i]
avg = sum2/4
print("The average is:", avg)

#make a copy
copy = number[:]

#find range
copy.sort()
rang = copy[3]-copy[0]
print("The range is:", rang)