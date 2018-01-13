import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# data is hepar2
methods = ['baseline', 'uniform', 'non-uniform']
method = 'nonuniform'

# read data
data = pd.read_csv('data/' + method + '.txt')
num_cols = ['100K', '500K', '1M', '5M']
# print(data)

# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 25
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 16
mpl.rcParams['figure.figsize'] = [5.2, 3.9]
# mpl.rcParams['legend.frameon'] = False

# plot
fig, ax = plt.subplots()

# log plot
# plt.yscale('log')
# bar_positions = np.arange(4) + 0.7
# ax.bar(bar_positions, data['100K'], 0.2, hatch='//', color='r', log=True)
# bar_positions = np.arange(4) + 0.9
# ax.bar(bar_positions, data['500K'], 0.2, hatch='x', color='g', log=True)
# bar_positions = np.arange(4) + 1.1
# ax.bar(bar_positions, data['1M'], 0.2, hatch='-', log=True)
# bar_positions = np.arange(4) + 1.3
# ax.bar(bar_positions, data['5M'], 0.2, hatch='\\', color='b', log=True)
# plt.ylim(ymax=1e9)

xticks = [0.02, 0.04, 0.06, 0.08, 0.1]
plt.plot(xticks, data['100K'], marker='o', color='r')
plt.plot(xticks, data['500K'], marker='*', color='g')
plt.plot(xticks, data['1M'], marker='s', color='b')
plt.plot(xticks, data['5M'], marker='+', color='k')

plt.xticks(xticks)
plt.ylim(ymin=0)
if method == 'baseline':
    plt.ylim(ymax=0.01)

# tick_pos = range(4)
# ax.set_xticks(tick_pos)
# ax.set_xticklabels(num_cols)
plt.xlabel('approximation factor $\epsilon$')
plt.ylabel('mean error to truth')

if method == 'baseline':
    plt.legend(num_cols, ncol=2)

# plt.show()
plt.savefig("figs/" + method + ".pdf", dpi=800, bbox_inches='tight')