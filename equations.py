from math import sqrt
import numpy as np


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



def ss_mass(t):
	"""
	Equation to calculate the mass of the space shuttle at time t
	:param t: time after ignition, [s]
	:return: Mass [kg]
	"""
	if 0 <= t < 2:
		return np.interp(t, [0, 2], [2_010_000, 820_000])
	elif 2 <= t <= 8:
		return np.interp(t, [2, 8], [660_000, 118_000])
	elif 8 < t:
		return 118_000
	else:
		raise ValueError('Input time outside valid domain')


def gamma(gamma, T_0 = 3200):
	"""
	:param gamma:
	:param T_0: inlet temperature, given.
	:return:
	"""
	return T_0 / (1 + ((gamma - 1) / 2))






def A_ratio(g_e, g_s, M_e):  # A_e/A_s
	pass
	return (1/M_e) * ((2 + (g_e - 1) * M_e**2) / (g_s + 1))**((g_e + 1) / (2 * (g_e - 1)))


def thrust_coefficient():
	pass

