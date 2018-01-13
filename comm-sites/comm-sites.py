import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

method = ['baseline', 'uniform', 'non-uniform']

# read data
data = pd.read_csv('./comm-sites.txt')
baseline = data[data['method'] == 'baseline']
uniform = data[data['method'] == 'uniform']
nonuniform = data[data['method'] == 'nonuniform']
# print(data)

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


# plot
plt.figure(1)
plt.plot(baseline['sites'], baseline['msg'], marker='*', color='g')
plt.plot(uniform['sites'], uniform['msg'], marker='s', color='b')
plt.plot(nonuniform['sites'], nonuniform['msg'], marker='+', color='k')

# labels
plt.xlabel('number of sites')
plt.ylabel('number of messages')

# xlim, ylim
plt.ylim(ymin=0, ymax=3e7)

# legend
plt.legend(method, loc='upper left')

# show or save
# plt.show()
plt.savefig("figs/" + "comm-sites.pdf", dpi=800, bbox_inches='tight')
