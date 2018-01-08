import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

methods = ['exact', 'baseline', 'uniform', 'non-uniform']

# alarm, hepar2, link, munin
data_name = 'alarm'

# read data
exact = pd.read_csv(data_name + '-exact.txt')
baseline = pd.read_csv(data_name + '-baseline.txt')
uniform = pd.read_csv(data_name + '-uniform.txt')
nonuniform = pd.read_csv(data_name + '-nonuniform.txt')
num_cols = ['5K', '50K', '500K', '5M']
print(exact)

# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 22
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['legend.fontsize'] = 15
# mpl.rcParams['legend.frameon'] = False

# exact
plt.figure(1)
plt.boxplot(exact[num_cols].values, sym='')
plt.show()
