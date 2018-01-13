import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

method = ['uniform', 'non-uniform']

# read data
data = pd.read_csv('./synthetic.txt')
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
plt.plot(range(5), uniform['msg'], marker='s', color='b')
plt.plot(range(5), nonuniform['msg'], marker='+', color='k')

# xticks
plt.xticks(range(5), uniform['num'])

# labels
plt.xlabel('training instances')
plt.ylabel('number of messages')

# xlim, ylim
plt.ylim(ymin=0)

# legend
plt.legend(method)

# show or save
# plt.show()
plt.savefig("figs/" + "synthetic.pdf", dpi=800, bbox_inches='tight')
