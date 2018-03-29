import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

methods = ['exact', 'baseline', 'uniform', 'non-uniform']

# alarm, hepar2, link, munin
data_name = 'alarm'

# read data
exact = pd.read_csv('data/' + data_name + '-exact.txt')
baseline = pd.read_csv('data/' + data_name + '-baseline.txt')
uniform = pd.read_csv('data/' + data_name + '-uniform.txt')
nonuniform = pd.read_csv('data/' + data_name + '-nonuniform.txt')
num_cols = ['5K', '50K', '500K', '5M']

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

# process data
mean_exact = [np.mean(exact['5K']), np.mean(exact['50K']), np.mean(exact['500K']), np.mean(exact['5M'])]
mean_baseline = [np.mean(baseline['5K']), np.mean(baseline['50K']), np.mean(baseline['500K']), np.mean(baseline['5M'])]
mean_uniform = [np.mean(uniform['5K']), np.mean(uniform['50K']), np.mean(uniform['500K']), np.mean(uniform['5M'])]
mean_nonuniform = [np.mean(nonuniform['5K']), np.mean(nonuniform['50K']), np.mean(nonuniform['500K']), np.mean(nonuniform['5M'])]

# plot
fig, ax = plt.subplots()
bar_positions = np.arange(4) + 0.7
ax.bar(bar_positions, mean_exact, 0.2, hatch='//', color='r')
bar_positions = np.arange(4) + 0.9
ax.bar(bar_positions, mean_baseline, 0.2, hatch='x', color='g')
bar_positions = np.arange(4) + 1.1
ax.bar(bar_positions, mean_uniform, 0.2, hatch='-')
bar_positions = np.arange(4) + 1.3
ax.bar(bar_positions, mean_nonuniform, 0.2, hatch='\\', color='b')

# plt.plot(range(4), mean_exact, marker='o', color='r')
# plt.plot(range(4), mean_baseline, marker='*', color='g')
# plt.plot(range(4), mean_uniform, marker='s', color='b')
# plt.plot(range(4), mean_nonuniform, marker='+', color='k')

# plt.xticks(range(4), num_cols)
# plt.ylabel('mean error to truth')
# plt.xlabel('training instances')

tick_pos = [1, 2, 3, 4]
ax.set_xticks(tick_pos)
ax.set_xticklabels(num_cols)
plt.xlabel('training instances')
plt.ylabel('mean error to truth')

if data_name == 'alarm':
    plt.legend(methods, frameon=False, fancybox=True)

# plt.show()
plt.savefig("figs/" + data_name + ".pdf", dpi=800, bbox_inches='tight', transparent=True)