# A short code simulating two dice throws picking the best one and computing the estimated mean

import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations_with_replacement as combinations

sides = 6
throws = int(1e6)

samples = np.array([np.random.randint(1, sides+1, throws), np.random.randint(1, sides+1, throws)])
choice = samples.max(axis=0)
print(f'After throwing two dices with {sides} sides thrown {throws} times, while chosing the highest dice each time, we got')
print(f'Dice 1: Mean = {np.mean(samples[0,:])}\nDice 2: Mean = {np.mean(samples[1,:])}\nChoice: Mean = {np.mean(choice)}\n')


# %% Deeper delve into the stats
unique, counts = np.unique(choice, return_counts=True)
print(f'The percentage each eye appeared in our choiced dice sample was\n'
      f'{np.array([unique, np.round(counts/throws*100,2)]).T}'
      )

plt.bar(unique, counts/throws*100)
plt.xlabel('Side')
plt.ylabel('%')
plt.xticks(unique)
plt.yticks(np.round(counts/throws*100, 2))
plt.show()


# %% Statistics
# TODO fix combinations (outer pair desired)
combs = np.array(list(combinations(unique, 2)))
print(np.reshape(np.array(list(combinations(unique, 2))), (sides, sides)))
