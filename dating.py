## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

#Ask user to input age
age = float( input("How old are you? "))

#Calculate dating age range
lowAge = int((age/2) + 7)
highAge = int((age*2) - 13)

#Display results
print('You can date people between', lowAge, 'and', highAge, 'years old')
