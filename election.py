## Amelia Hampford
## CS1110-002 Fall 2016
## 09/10/2016

import random
count = 0
trump = 0

# states are VA, FL, PA, CO, OH (in that order)
state_chances_for_trump = [.238, .569, .304, .324, .634]
electoral_votes_by_state = [13, 29, 20, 9, 18]

#simulation runs
runs = int(input("How many simulation runs?: "))

#seed random number
seed = int(input("Enter a seed (0 for random): "))
if seed != 0:
    random.seed(seed)

for j in range(runs):
    for i in range(5):
        chance = random.random()
        if chance <= state_chances_for_trump[i]:
            count = count + electoral_votes_by_state[i]
    if count > 44:
        print("Run " + str(j) + ": Trump wins with " + str(count))
        trump += 1
    else:
        print("Run " + str(j) + ": Clinton wins with " + str(89-count))
    count = 0

print("Chance of Trump winning: " + str(trump/runs))
print("Chance of Clinton winning: " + str(1-(trump/runs)))