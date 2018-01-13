import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def func(file_name):
    content = open(file_name).readlines()
    content = [x.strip() for x in content]
    return list(map(int, content))


methods = ['exact', 'baseline', 'uniform', 'non-uniform']

# alarm, hepar2, link, munin
data_name = 'munin'

# read data
exact = func('data/' + data_name + '-exact.txt')
baseline = func('data/' + data_name + '-baseline.txt')
uniform = func('data/' + data_name + '-uniform.txt')
nonuniform = func('data/' + data_name + '-nonuniform.txt')
d = {'exact': exact, 'baseline': baseline, 'uniform': uniform, 'nonuniform': nonuniform}
df = pd.DataFrame(data=d)
num_cols = ['5K', '50K', '500K', '5M']

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
# ax.bar(bar_positions, df['exact'], 0.2, hatch='//', color='r', log=True)
# bar_positions = np.arange(4) + 0.9
# ax.bar(bar_positions, df['baseline'], 0.2, hatch='x', color='g', log=True)
# bar_positions = np.arange(4) + 1.1
# ax.bar(bar_positions, df['uniform'], 0.2, hatch='-', log=True)
# bar_positions = np.arange(4) + 1.3
# ax.bar(bar_positions, df['nonuniform'], 0.2, hatch='\\', color='b', log=True)
# plt.ylim(ymax=1e9)

plt.semilogy(range(4), exact, marker='o', color='r')
plt.semilogy(range(4), baseline, marker='*', color='g')
plt.semilogy(range(4), uniform, marker='s', color='b')
plt.semilogy(range(4), nonuniform, marker='+', color='k')

# plt.xticks(range(4), num_cols)
# plt.ylabel('mean error to truth')
# plt.xlabel('training instances')

tick_pos = range(4)
ax.set_xticks(tick_pos)
ax.set_xticklabels(num_cols)
plt.xlabel('training instances')
plt.ylabel('number of messages')

if data_name == 'alarm':
    plt.legend(methods, loc='upper left')

# plt.show()
plt.savefig("figs/" + data_name + ".pdf", dpi=800, bbox_inches='tight')