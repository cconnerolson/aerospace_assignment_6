# a. Examine M_e variation with Ae/A* (from 1-1000) for varying g_e (between 1.28-1.2 in steps of 0.01).

import numpy as np
from scipy.optimize import fsolve, newton_krylov
import matplotlib.pyplot as plt
from equations import gamma, schomate


T_jj = 3200
d_T = 1


def converge(T_jj = 3000, d_T = 1, d_gamma = 1):
	gamma_jj = schomate(T_jj)
	while d_T > 0.01 or d_gamma > 0.01:
		T_ii = gamma(gamma_jj)
		gamma_ii = schomate(T_ii)
		d_T, d_gamma = abs((T_ii - T_jj) / T_jj), abs((gamma_ii - gamma_jj) / gamma_jj)
		T_jj, gamma_jj = T_ii, gamma_ii
	return(T_ii, gamma_ii)


"""T, gamma = converge()
print('T     =', T)
print('gamma =', gamma)"""


def fun():
	pass