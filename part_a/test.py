from sympy import *
# fn = A_eq()

g_s = Symbol('g_s')
g_e = Symbol('g_e')
M_e = Symbol('M_e')
A_r = Symbol('A_r')


e1 = sqrt(g_s / g_e)
e2 = 1 / M_e
e3 = (1 + ((g_e - 1) / 2) * M_e**2)**((g_e + 1) / (2 * (g_e - 1)))
e4 = ((g_s + 1) / 2)**((g_s + 1) / (2 * (g_s - 1)))


fn = (e1 * e2 * e3) / e4 - A_r
print(fn)
fn = fn.subs([(g_s, 1.1758101459676122), (g_e, 1.2), (A_r, 1000.)])
print(fn)
x = nsolve(fn, 10)
print(x)



