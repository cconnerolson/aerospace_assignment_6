# a. Examine M_e variation with Ae/A* (from 1-1000) for varying g_e (between 1.28-1.2 in steps of 0.01).

from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import a_functions as f_a
import a_constants as k

T, gamma_s = f_a.converge_a()

for gamma in k.gamma_e:
	fn = f_a.A_eq_g(gamma, gamma_s)
	c = int(((gamma - 1.2) * 100))
	for A in k.A_ratio:
		f = f_a.A_eq_A(A, fn)
		M = nsolve(f, 10)
		k.y_data[(int(A - 1), c)] = M

#data = np.concatenate([k.A_values, k.y_data], axis=1)
np.savetxt('a_data.csv', k.y_data, delimiter=',')
