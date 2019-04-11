from part_a.a_functions import schomate
from sympy import *
import b_constants as k




def T_eq(T_s, T_0=3200, M_0=1):
	return (2 / M_0**2) * ((T_0 / T_s) - 1) + 1


gamma = schomate(k.T_0)


def A_eq_g(gam_e=1.2, gam_s=1.1758101459676122, Ar = k.A_ratio):
	g_e = Symbol('γₑ')
	g_s = Symbol('γ*')
	A_r = Symbol('Aₑ/A*')
	M_e = Symbol('Mₑ')
	e1 = sqrt(g_s / g_e)
	e2 = 1 / M_e
	e3 = (1 + ((g_e - 1) / 2) * M_e**2)**((g_e + 1) / (2 * (g_e - 1)))
	e4 = ((g_s + 1) / 2)**((g_s + 1) / (2 * (g_s - 1)))
	eq = (e1 * e2 * e3) / e4 - A_r
	eq = eq.subs([(g_e, gam_e), (g_s, gam_s), (A_r, Ar)])
	return nsolve(eq, 10)


# *Schomate imported from part a*


def converge_b(T_jj = 5500, d_T=1, d_gamma=1, d_M=1):
	gamma_jj = schomate(T_jj)
	M_e_jj = A_eq_g(gam_e=gamma_jj)
	while d_T > 0.001 or d_gamma > 0.001 or d_M > 0.001:
		T_ii = T_eq(gamma_jj)
		gamma_ii = schomate(T_ii)
		M_e_ii = A_eq_g(gam_e=gamma_ii)
		gamma_ii = schomate(T_ii)
		d_T, d_gamma, d_M = abs((T_ii-T_jj)/T_jj),\
						abs((gamma_ii-gamma_jj)/gamma_jj),\
						abs((M_e_ii-M_e_jj)/M_e_jj)
		T_jj, gamma_jj, M_e_jj = T_ii, gamma_ii, M_e_jj
	return(T_ii, gamma_ii, M_e_ii)


def P_e_eq(g_e, M_e, P_0=k.P_0):
	return P_0 / ((1 + ((g_e - 1) / 2) * M_e**2)**((g_e) / (g_e - 1)))


def V_e_eq(gamma, Te, Me, R=k.R):
	M_e = Symbol('Mₑ')
	g_e = Symbol('γₑ')
	T_e = Symbol('Tₑ')
	eq = M_e * sqrt(g_e * R * T_e)
	eq = eq.subs([(g_e, gamma), (T_e, Te), (M_e, Me)])
	return eq

