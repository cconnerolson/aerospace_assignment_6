from sympy import *

def converge(T_jj = 3000, d_T = 1, d_gamma = 1):
	gamma_jj = schomate(T_jj)
	while d_T > 0.01 or d_gamma > 0.01:
		T_ii = T_ratio(gamma_jj)
		gamma_ii = schomate(T_ii)
		d_T, d_gamma = abs((T_ii - T_jj) / T_jj), abs((gamma_ii - gamma_jj) / gamma_jj)
		T_jj, gamma_jj = T_ii, gamma_ii
	return(T_ii, gamma_ii)


def schomate(T):
	"""
	Shchomate equation to calculate specific heat of water vapor for a given temperature T.
	:param T: Temperature [K]
	:return: Heat Capacity [J/mol*K]
	"""
	t = T / 1000
	if 500 <= T < 1700:
		a, b, c, d, e = [30.092, 6.832514, 6.793425, -2.53448, 0.082139]
	elif T == 1700:
		return 2.7175
	elif 1700 < T <= 6000:
		a, b, c, d, e = [41.96426, 8.622053, -1.49978, 0.098119, -11.1576]
	else:
		raise ValueError('Input temperature outside valid domain')
	c_p = (a + (b * t) + (c * t**2) + (d * t**3) + (e / t**2)) / 18
	R = 0.4615
	c_v = c_p - R
	g = c_p / c_v
	return g


def T_ratio(gamma_star, T_0 = 3_200):
	"""
	:param gamma:
	:param T_0: inlet temperature, given.
	:return:
	"""
	return T_0 / (1 + ((gamma_star - 1) / 2))


x = 'γ*'


def A_eq():
	g_e = Symbol('γₑ')
	g_s = Symbol('g_s')
	A_r = Symbol('Aₑ/A*')
	M_e = Symbol('M_e')
	fn = Eq(
			(sqrt(g_s / g_e)) * (1 / M_e) * (1 + ((g_e - 1) / 2) * M_e**2)**((g_e + 1) / (2 * (g_e - 1))) *
			((g_s + 1) / 2)**(-(g_s + 1) / (2 * (g_s - 1))) - A_r
			)
	return fn




