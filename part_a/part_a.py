# a. Examine M_e variation with Ae/A* (from 1-1000) for varying g_e (between 1.28-1.2 in steps of 0.01).

import a_functions as fn
import a_constants as k
from sympy import *


T, gamma_star = fn.converge()

print('T* =', T)
print('γ* =', gamma_star)


'''for gamma in k.gamma_e:
	M_e = Symbol('M_e')
	
	for A in k.A_ratio:
		print(A)'''
