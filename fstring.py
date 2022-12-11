import numpy as np

# https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting/

# %% surround with signs
print(f'{" Encapsulated (:*^30) ":*^30}')
print(f'{" Left (:*>30)":*>30}')
print(f'{"Right (:*<30) ":*<30}')


# %% align text
print('\n\n', f'{" Alignment ":#^60}')
n=6
strings = [f'string{i}' for i in np.logspace(0, n, n+1, dtype=int)]
m = max([len(s) for s in strings]) + 5

print('\033[4m' +  # starts underline
      f"{'left (:<{m})':<{m}},{'centered (:^{m})':^{m}},{'right (:>{m})':>{m}}" +
      '\033[0m\n')  # ends underline

for s in strings:
    print(f'{s:<{m}},{s:^{m}}, {s:>{m}}')

# %% number representations
print('\n\n', f'{" Float representations ":#^60}')

nan = float('nan')
tests = [
    'f"{1/2:.1%}"',
    'f"{1000:.1e} vs {1000:.1E}"',
    'f"{1000:.1f} vs {1000:.1F}"',
    'f"{1000:.1g} vs {1000:.1G}"',
    'f"{nan:f} vs {nan:F}"'
]
ans = [
    f"{1/2:.1%}",
    f"{1000:.1e} vs {1000:.1E}",
    f"{1000:.1f} vs {1000:.1F}",
    f"{1000:.1g} vs {1000:.1G}",
    f"{nan:f} vs {nan:F}"
]
m = max([len(s) for s in tests])
for t, a in zip(tests, ans):
    print(f'{t:<{m}} = {a}')
