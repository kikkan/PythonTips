import numpy as np
from scipy.linalg import qr

np.set_printoptions(precision=1)

np.random.seed(69)
# Create a random matrix
A = np.random.rand(3, 3)

# Compute the QR decomposition of A
Q, R = qr(A)

# Q is an orthogonal matrix
print(Q.T @ Q)
