import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

method = ['exact', 'baseline', 'uniform', 'non-uniform']

# read data
# folder_name = 'reducednet-var/'
folder_name = './'
exact = pd.read_csv(folder_name + 'exact.txt', header=None)
baseline = pd.read_csv(folder_name + 'baseline.txt', header=None)
uniform = pd.read_csv(folder_name + 'uniform.txt', header=None)
nonuniform = pd.read_csv(folder_name + 'nonuniform.txt', header=None)


# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 22
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['legend.fontsize'] = 15
# mpl.rcParams['legend.frameon'] = False


plt.figure(1)
plt.plot(exact[0], exact[1], marker='o', color='r')
plt.plot(baseline[0], baseline[1], marker='*', color='g')
plt.plot(uniform[0], uniform[1], marker='s', color='b')
plt.plot(nonuniform[0], nonuniform[1], marker='+', color='k')

# xlim, ylim
plt.ylim(ymin=0)

# ticks
plt.xticks(exact[0])

# labels
plt.xlabel('number of variables')
plt.ylabel('communication messages')

# legend
plt.legend(method)

# show or save
# plt.show()
plt.savefig("figs/reducednet-var.pdf", dpi=600, bbox_inches='tight')


plt.figure(2)
plt.semilogy(exact[0], exact[1], marker='o', color='r')
plt.semilogy(baseline[0], baseline[1], marker='*', color='g')
plt.semilogy(uniform[0], uniform[1], marker='s', color='b')
plt.semilogy(nonuniform[0], nonuniform[1], marker='+', color='k')

# ticks
plt.xticks(exact[0])

# labels
plt.xlabel('number of variables')
plt.ylabel('communication messages')

# legend
plt.legend(method)

# show or save
# plt.show()
plt.savefig("./figs/reducednet-var-logscale.pdf", dpi=600, bbox_inches='tight')