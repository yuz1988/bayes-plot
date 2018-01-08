import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read experiment result
def read(method_name, data_name):
    errors = []
    sizes = [50, 500, 5000]
    sizes = [e * 1000 for e in sizes]
    for i in sizes:
        filename = 'C:/Users/Yu/Desktop/bayes-result1/' + data_name + '/' + \
                   method_name + '/' + 'query-' + str(i) + '.txt'
        f = open(filename, 'r')
        data = f.readlines()
        data = list(map(float, data))
        errors.append(data)
    return errors


# boxplot result
data_name = 'alarm'
counterTypes = ['exact', 'improve', 'uniform', 'nonuniform']

# read data
exact_error = read('exact', data_name)
uniform_error = read('improve', data_name)
improve_error = read('uniform', data_name)
nonuniform_error = read('nonuniform', data_name)

fig, axes = plt.subplots(figsize=(8, 5))
# no outliers
plt.boxplot(exact_error, sym='')
fig.savefig("filename.eps", dpi=200, bbox_inches='tight')
