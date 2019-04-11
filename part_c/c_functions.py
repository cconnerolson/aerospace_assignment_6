from sympy import *
from part_b.b_constants import R


def A_s(A_e, A_ratio):
	return A_e / A_ratio


def Thrust_eq(P0, Pa, Pe, gamma_s, gamma_e, As, Ae, T0, Me, R=R):
	P_0 = Symbol('P_0')
	P_a = Symbol('P_a')
	P_e = Symbol('P_e')
	g_s = Symbol('γ*')
	g_e = Symbol('γₑ')
	A_s = Symbol('A*')
	A_e = Symbol('Aₑ')
	T_0 = Symbol('T_0')
	M_e = Symbol('M_e')
	e1 = P_0 / (((g_s + 1)/2)**((g_s + 1) / (2 * (g_s - 1))))
	e2 = A_s / (sqrt(R * T_0))
	e3 = sqrt(g_s)
	e4 = sqrt(g_e * R * T_0)
	e5 = M_e / ((1 + (g_e - 1) / 2 * M_e**2)**0.5)
	e6 = (P_e - P_a) * A_e
	eq = e1 * e2 * e3 * e4 * e5 + e6
	eq = eq.subs([(P_0, P0), (P_a, Pa), (P_e, Pe), (g_s, gamma_s), (g_e, gamma_e), (A_e, Ae), (T_0, T0), (M_e, Me)])
	return eq

