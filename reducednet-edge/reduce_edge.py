import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

method = ['exact', 'baseline', 'uniform', 'non-uniform']

# read data
# folder_name = 'reducednet-edge/'
folder_name = './'
exact = pd.read_csv(folder_name + 'exact.txt', header=None)
baseline = pd.read_csv(folder_name + 'baseline.txt', header=None)
uniform = pd.read_csv(folder_name + 'uniform.txt', header=None)
nonuniform = pd.read_csv(folder_name + 'nonuniform.txt', header=None)

# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 25
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 18
mpl.rcParams['figure.figsize'] = [5.2, 3.9]
# mpl.rcParams['legend.frameon'] = False


plt.figure(1)
plt.plot(exact[1], exact[2], marker='o', color='r')
plt.plot(baseline[1], baseline[2], marker='*', color='g')
plt.plot(uniform[1], uniform[2], marker='s', color='b')
plt.plot(nonuniform[1], nonuniform[2], marker='+', color='k')

# ticks
plt.xticks(exact[1])

# xlim, ylim
plt.ylim(ymin=0, ymax=8e8)

# labels
plt.xlabel('number of edges')
plt.ylabel('number of messages')

# legend
# plt.legend(method)

# show or save
# plt.show()
plt.savefig("figs/reducednet-edge.pdf", dpi=800, bbox_inches='tight')



plt.figure(2)
plt.semilogy(exact[1], exact[2], marker='o', color='r')
plt.semilogy(baseline[1], baseline[2], marker='*', color='g')
plt.semilogy(uniform[1], uniform[2], marker='s', color='b')
plt.semilogy(nonuniform[1], nonuniform[2], marker='+', color='k')

# ticks
plt.xticks(exact[1])

# labels
plt.xlabel('number of edges')
plt.ylabel('communication messages')

# legend
plt.legend(method)

# show or save
# plt.show()
plt.savefig("./figs/reducednet-edge-logscale.pdf", dpi=800, bbox_inches='tight')