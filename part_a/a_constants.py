import numpy as np

# convergence guess
T_jj = 3_200
d_T = 1

# data arrays
gamma_e = np.linspace(1.2, 1.28, 9)
A_ratio = np.linspace(1, 1_000, 1_000)
A_values = np.reshape(A_ratio, (1000, 1))
y_data = np.zeros((1000, 9))
