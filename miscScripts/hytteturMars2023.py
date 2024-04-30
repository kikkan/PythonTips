import numpy as np

#%%MARK: About
# Compute how to split the bill seperated by vegetarian and meat eaters.

T1 = 2289.41  # total on receipt 1
T2 = 731.47  # Total on receipt 2
Tall = T1 + T2
T = Tall

notInclude = { # expenses to not include (personal)
    # first receipt
    'frydPils': 167.4+6*2,
    'pokal': 149.4+2*6,
    # second receipt
    'frydJuicy': 41.9+2
}
vegetar = {
    # first receipt
    'kidney': 13.9,
}
meat = {
    # first receipt
    'bacon': 2*63,
    'kjottdeig': 4*73.9,
    #
    'pepperoni': 36.9,
    'strandaSkinke': 86.9
}
# tVeg = 0
# tMeat = 0
# for d in [notInclude, vegetar, meat]:
#     for product, price in d.items():
#         T -= price

print(f'Total expenses: {Tall} (R1: {T1}, R2: {T2})\n'
      f'Shared all =    {Tall}-{sum(notInclude.values())}-{sum(vegetar.values())}-{sum(meat.values())}\n'
      f'           =    {Tall-sum(notInclude.values())-sum(vegetar.values())-sum(meat.values())}\n'
      f'Meat expenses:  {sum(meat.values())}\n'
      f'Veg expenses:   {sum(vegetar.values())}'
      )

# print(T)
