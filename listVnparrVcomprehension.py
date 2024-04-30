from numpy import array as ar, empty as emp
from time import time
from math import log10

#region about:
# We test the speed of 
# - Appending to list
# - List comprehension
# - Assigning to prespecified length of array
#endregion

#TODO: Add more tests (comrehension to np.array, assigning to prespec. list, etc.)

times = {
    "app": list(),
    "comp": list(),
    "arr": list()
}

iters = ar([10**i for i in range(5,9)])

for n in iters:
    print(f"n = 10^{int(log10(n))}...")
    # Append to list
    start = time()
    l = []
    for _ in range(n):
        l.append(1)
    times["app"].append(time() - start)

    # List comprehension
    start = time()
    l = [1 for _ in range(n)]
    times["comp"].append(time() - start)
    
    l = emp(n)
    start = time()
    for i in range(n):
        l[i] = 1
    times["arr"].append(time() - start)



print("\n\n")
for m, t in times.items():
    print(f'method:{m:>5}, {t}')