import numpy as np

C = np.zeros((3, 8))
C[0, 5], C[1, 6], C[2, 7] = 1, 1, 1
# print(C)
np.random.seed(1)


D = np.array([-1 if i < 16 else 1 for i in range(32)])
F = np.array([-1 if i%8 < 4 else 1 for i in range(32)])
T = np.array([-1 if i%2 == 0 else 1 for i in range(32)])
DF = D.T*F
DT = D.T*T
FT = F.T*T
DFT = D*F*T
# print(np.sum(D.T*F))
# print(np.sum(D.T*T))
# print(np.sum(F.T*T))
# print(sum(DFT*D))
# print(DF)


# X = np.random.randint(-1, high=2, size=(32, 8))
X = np.array([np.ones_like(D), D, F, T, DF, DT, FT, DFT]).T
print(np.shape(X))
print(X)

# for i in range(np.shape(X)[0]):
#     for j in range(np.shape(X)[1]):
#         if X[i, j] == 0:
#             t = np.random.random()
#             if t>= 0.5:
#                 X[i, j] = 1
#             else:
#                 X[i, j] = -1

b = np.linalg.inv(X.T @ X)
# te = X.T @ X
# print(te)

print()
print('b\n', b)
print()
print(C@b)
print()
# print(C@b@C.T)
print(np.linalg.inv(C@b@C.T))
