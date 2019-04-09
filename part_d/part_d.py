# d. Using the design Ae/A* examine thrust coefficient variation with ambient pressure (Pa/P0),
#    with Pa from 1 atmosphere to vacuum conditions during flight; use appropriate 15 steps,
#    with design pressure prominently represented; note C_tau can be higher than design value for ideal calculations.


import numpy as np

# given
T = np.linspace(start=1, stop=0, num=15)
