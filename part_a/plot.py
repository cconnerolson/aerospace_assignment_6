import matplotlib.pyplot as plt
import pandas

cols = ['1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28']
df = pandas.read_csv('a_data.csv', header=-1, names=cols)
df.index = df.index + 1

df.plot(kind='line', use_index=True)
plt.legend(title='γₑ')
plt.title(r'Mach No. Varying with $\frac{Aₑ}{A*}$ for Various γₑ', fontsize=15, y=1.02)
plt.ylabel(r'$M_e$', fontsize=14)
plt.xlabel(r'$\frac{Aₑ}{A*}$', fontsize=20)
plt.savefig('graph_a', bbox_inches='tight', dpi=200)
plt.show()



