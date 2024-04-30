u = {}
u['irish'] = 925/5
u['noam'] = 149
u['kristStens'] = 149
u['dahls'] = 784/8

tot = 0
for unit, value in u.items():
    tot += value
    print(f'{unit:<14}{value}')

print(tot)
