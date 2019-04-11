# c. Establish actual thrust value for A_e = 4.478 m**2.


from part_b.b_constants import T_0, P_0
from part_b.part_b import T_e, gamma_s, gamma_e, M_e, P_e, V_e
from part_b.b_constants import R, A_ratio
import c_constants as k
import c_functions as f_c

A_s = f_c.A_s(A_e=k.A_e, A_ratio=A_ratio)

P_a = P_e  # given in part b

T = f_c.Thrust_eq(P0=P_0, Pa=P_a, Pe=P_e, gamma_s=gamma_s, gamma_e=gamma_e, As=A_s, Ae=k.A_e, T0=T_0, Me=M_e)

print('Thrust =', T)
