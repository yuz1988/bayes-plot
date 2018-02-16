import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

method = ['exact', 'baseline', 'uniform', 'non-uniform']

# read data
# alarm, hepar2, link, munin
data_name = 'alarm'
data = pd.read_csv('./data/' + data_name + '.txt', header=None)
exact = data[data[1] == 'exact']
baseline = data[data[1] == 'baseline']
uniform = data[data[1] == 'uniform']
nonuniform = data[data[1] == 'nonuniform']
# print(exact)

# configuration
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['font.size'] = 25
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 17
mpl.rcParams['figure.figsize'] = [5.2, 3.9]
# mpl.rcParams['legend.frameon'] = False


# # msg transmitted
# plt.figure(0)
# plt.plot(exact[0], exact[2], marker='o', color='r')
# plt.plot(baseline[0], baseline[2], marker='*', color='g')
# plt.plot(uniform[0], uniform[2], marker='s', color='b')
# plt.plot(nonuniform[0], nonuniform[2], marker='+', color='k')
#
# # labels
# plt.xlabel('number of sites')
# plt.ylabel('number of messages')
#
# # xlim, ylim
# plt.ylim(ymin=0)
#
# # legend
# plt.legend(method, ncol=2)
#
# # show or save
# # plt.show()
# plt.savefig("figs/" + data_name + "-message.pdf", dpi=600, bbox_inches='tight')


# runtime delay
plt.figure(1)
plt.plot(exact[0], exact[3], marker='o', color='r')
plt.plot(baseline[0], baseline[3], marker='*', color='g')
plt.plot(uniform[0], uniform[3], marker='s', color='b')
plt.plot(nonuniform[0], nonuniform[3], marker='+', color='k')

# labels
plt.xlabel('number of sites')
plt.ylabel('runtime (sec)')

# xlim, ylim
plt.ylim(ymin=0, ymax=480)

# legend
if data_name == 'alarm':
    plt.legend(method, ncol=2, columnspacing=0.5, frameon=True)

# show or save
# plt.show()
plt.savefig("figs/" + data_name + "-time.pdf", dpi=800, bbox_inches='tight')


# Throughput
pd.options.mode.chained_assignment = None
num_vec = 500 * 1000
exact[3] = num_vec / exact[3]
baseline[3] = num_vec / baseline[3]
uniform[3] = num_vec / uniform[3]
nonuniform[3] = num_vec / nonuniform[3]

plt.figure(2)
plt.plot(exact[0], exact[3], marker='o', color='r')
plt.plot(baseline[0], baseline[3], marker='*', color='g')
plt.plot(uniform[0], uniform[3], marker='s', color='b')
plt.plot(nonuniform[0], nonuniform[3], marker='+', color='k')

# labels
plt.xlabel('number of sites')
plt.ylabel('throughput (events/sec)')

# xlim, ylim
plt.ylim(ymin=0)
# if data_name == 'alarm':
#     plt.ylim(ymax=2800)
# elif data_name == 'hepar2':
#     plt.ylim(ymax=1200)

# legend
# if data_name == 'alarm':
#     plt.legend(method, ncol=2, bbox_to_anchor=(0.5, -0.05),
#                loc='lower center', columnspacing=0.5)

# show or save
# plt.show()
plt.savefig("figs/" + data_name + "-throughput.pdf", dpi=800, bbox_inches='tight')