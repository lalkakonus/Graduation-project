import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

N=1000
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

def line(ax, function, color='green', label=''):
    x_cords = ax.get_xlim()
    y_cords = list(map(lambda x: function(x), x_cords))
    ax.plot(x_cords, y_cords, c=color, linewidth=2, label=label)

def curve(ax, function, N=5e2, color='green', size=0.5):
    x_array, y_array = [], []
    for x in np.linspace(*ax.get_xlim(), N):
        y = function(x)
        x_array.append(x)
        y_array.append(y)
    ax.scatter(x_array, y_array, s=size, c=color)

def sector(ax, function, N=5e2, color='green', alpha=1, size=2):
    x_array, y_array = [], []
    for x in np.linspace(*ax.get_xlim(), N):
        for y in np.linspace(*ax.get_ylim(), N):
            if function(x, y):
                x_array.append(x)
                y_array.append(y)
    ax.scatter(x_array, y_array, s=size, c=color, alpha=alpha)
