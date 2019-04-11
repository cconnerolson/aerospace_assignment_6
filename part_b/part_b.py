# b. The operational design A_e/A* for SSME =69:1; establish Me, Pe, Ve for this operation.
#    Note at design condition Pe=Pa and all thrust is momentum thrust.

from part_a.a_functions import schomate
import b_functions as f_b
import b_constants as k

gamma_s = schomate(k.T_0)

T_e, gamma_e, M_e = f_b.converge_b(T_jj=5500)

print('Tₑ =',T_e,'K')  # 5512.735083496886 K
print('γₑ =',gamma_e)  # 1.1607368871868258
print('Mₑ =',M_e)  # 4.35297776197226

P_e = f_b.P_e_eq(g_e=gamma_e, M_e=M_e)

print('Pₑ =', P_e,'atm')  # 0.255146548570028 atm

V_e = f_b.V_e_eq(gamma=gamma_e, Te=T_e, Me=M_e)
print('Vₑ =',V_e,'m/s')


