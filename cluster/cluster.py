import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

method = ['exact', 'baseline', 'uniform', 'non-uniform']

# read data
# alarm, hepar2, link, munin
data_name = 'hepar2'
data = pd.read_csv(data_name + '.txt', header=None)
exact = data[data[1] == 'exact']
baseline = data[data[1] == 'baseline']
uniform = data[data[1] == 'uniform']
nonuniform = data[data[1] == 'nonuniform']

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
plt.plot(exact[0], exact[2], marker='o', color='r')
plt.plot(baseline[0], baseline[2], marker='*', color='g')
plt.plot(uniform[0], uniform[2], marker='s', color='b')
plt.plot(nonuniform[0], nonuniform[2], marker='+', color='k')

# labels
plt.xlabel('number of sites')
plt.ylabel('runtime (seconds)')

# xlim, ylim
plt.ylim(ymin=0)

# legend
plt.legend(method)

# show or save
# plt.show()
plt.savefig("figs/" + data_name + "-time.pdf", dpi=600, bbox_inches='tight')


# Throughput
pd.options.mode.chained_assignment = None
num_vec = 50 * 1000
exact[2] = num_vec / exact[2]
baseline[2] = num_vec / baseline[2]
uniform[2] = num_vec / uniform[2]
nonuniform[2] = num_vec / nonuniform[2]

plt.figure(2)
plt.plot(exact[0], exact[2], marker='o', color='r')
plt.plot(baseline[0], baseline[2], marker='*', color='g')
plt.plot(uniform[0], uniform[2], marker='s', color='b')
plt.plot(nonuniform[0], nonuniform[2], marker='+', color='k')

# labels
plt.xlabel('number of sites')
plt.ylabel('throughput (events per second)')

# xlim, ylim
plt.ylim(ymin=0)
if data_name == 'alarm':
    plt.ylim(ymax=2800)
elif data_name == 'hepar2':
    plt.ylim(ymax=1200)

# legend
plt.legend(method, loc='upper left')

# show or save
# plt.show()
plt.savefig("figs/" + data_name + "-throughput.pdf", dpi=600, bbox_inches='tight')