import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

methods = ['exact', 'baseline', 'uniform', 'non-uniform']

# alarm, hepar2, link, munin
data_name = 'munin'

# read data
exact = pd.read_csv(data_name + '-exact.txt')
baseline = pd.read_csv(data_name + '-baseline.txt')
uniform = pd.read_csv(data_name + '-uniform.txt')
nonuniform = pd.read_csv(data_name + '-nonuniform.txt')
num_cols = ['5K', '50K', '500K', '5M']
ymax = 0.16
yticks = np.arange(0.0, 0.18, 0.02)


# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 25
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 18
# mpl.rcParams['legend.frameon'] = False

# exact
fig, ax = plt.subplots()
ax.boxplot(exact[num_cols].values, sym='')
# xtick
ax.set_xticklabels(num_cols)
ax.set_yticks(yticks)
# ylim
ax.set_ylim(ymax=ymax)
# ylabel
ax.set_ylabel('relative error to truth')
# plt.show()
plt.savefig("figs/" + data_name + "-exact.pdf", dpi=600, bbox_inches='tight')

# baseline
fig, ax = plt.subplots()
ax.boxplot(baseline[num_cols].values, sym='')
# xtick
ax.set_xticklabels(num_cols)
ax.set_yticks(yticks)
# ylim
ax.set_ylim(ymax=ymax)
# plt.show()
plt.savefig("figs/" + data_name + "-baseline.pdf", dpi=600, bbox_inches='tight')

# uniform
fig, ax = plt.subplots()
ax.boxplot(uniform[num_cols].values, sym='')
# xtick
ax.set_xticklabels(num_cols)
ax.set_yticks(yticks)
# ylim
ax.set_ylim(ymax=ymax)
# plt.show()
plt.savefig("figs/" + data_name + "-uniform.pdf", dpi=600, bbox_inches='tight')

# nonuniform
fig, ax = plt.subplots()
ax.boxplot(nonuniform[num_cols].values, sym='')
# xtick
ax.set_xticklabels(num_cols)
ax.set_yticks(yticks)
# ylim
ax.set_ylim(ymax=ymax)
# plt.show()
plt.savefig("figs/" + data_name + "-nonuniform.pdf", dpi=600, bbox_inches='tight')