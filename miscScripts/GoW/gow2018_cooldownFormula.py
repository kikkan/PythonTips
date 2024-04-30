import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit as cf

#%% Data
df = pd.read_excel('cdRunicData.xlsx')
# print(df)

plt.scatter(df['cd'], df['ht'], label="Hel's Touch")
plt.scatter(df['cd'], df['bof'], label='Blessing of the Frost', marker='^')
plt.xlabel('Cooldown (cd)')
plt.ylabel('Time (s)')
plt.title('Cooldown time afo. cooldown')
plt.legend()
# plt.show()

#region this
a=2
#endregion

#%% Find curve formula
x1 = df[df['cd']==50]['bof']
x2 = df[df['cd']==100]['bof']
# print(x1, x2)

def findCurve(cd, t):
    dy = t[1]-[0]
    dx = cd[1]-cd[0]
    a = dy/dx

#region scipy curve fit
def lin(x, a, b):
    return a*x + b

yBof = df['bof']
yHt = df[~df['ht'].isna()]['ht']
x = df['cd']

abBof50, covBof50 = cf(lin, x[x<=50], yBof[x<=50])
abBof100, covBof100 = cf(lin, x[x<=100], yBof[x<=100])
abBof200, covBof200 = cf(lin, x[x<=200], yBof[x<=200])
print(abBof50)
print(abBof100)
print(abBof200)

abHt50, covHt50 = cf(lin, x[(x<=50) &  (~yHt.isna())], yHt[x<=50])
abHt100, covHt100 = cf(lin, x[(x<=100) & (~yHt.isna())], yHt[x<=100])
abHt200, covHt200 = cf(lin, x[(x<=200) & (~yHt.isna())], yHt[x<=200])

print(abHt50)
print(abHt100)
print(abHt200)

#endregion

#%% Comparing forumula to data
# see Onenote for computation
# Formula: Base(1-0.00355cd) = cooldown time
def f(b, x):
    return np.round(b*(1-0.00355*x))

bBof = 197
bHt = 45
xAx = np.arange(0,275,1)
plt.plot(xAx, f(bBof, xAx), "--", color="grey")
plt.plot(xAx, f(bHt, xAx), "--", color="grey")
plt.savefig('cdVStime.pdf')
plt.show()
