from base import *

def l_1_function(x):
    return (sqrt(2) - 1)*x + 1

def l_2_function(x):
    return (x-1) / (3 - sqrt(2))

def sector_1(x, y):
    return (y < l_1_function(x)) and  (y > l_2_function(x))

plt.rc('text', usetex=True)
fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111)
plt.xlim(-0.2, 1.8)
plt.ylim(-0.2, 1.8)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
plt.xlabel(r'$q_0$', fontsize=16)
plt.ylabel(r'$q_2$', fontsize=16)

#-----------figures---------------------

sector(ax, sector_1, color='lightgreen')
line(ax, l_1_function, color='black', label=r'$\ell_1: \; q_2=(\sqrt{2}-1)q_0+1$')
line(ax, l_2_function, color='black', label=r'$\ell_2: \; q_2=\dfrac{q_0-1}{3 - \sqrt{2}}$')

#-----------lines----------------------

x_lims = ax.get_xlim()
y_lims = ax.get_ylim()
plt.plot([x_lims[0], 1], [1, 1], c='black', linestyle='--')
plt.plot([x_lims[0], 1], [0, 0], c='black', linestyle='--')
plt.plot([1, 1], [y_lims[0], 1], c='black', linestyle='--')
plt.plot([0, 0], [y_lims[0], 1], c='black', linestyle='--')

#-----------labels--------------------

ax.annotate(r'$\ell_1$',
            xy=(0.6, 1.4), fontsize=25,
            horizontalalignment='right',
            verticalalignment='top')

ax.annotate(r'$\ell_2$',
            xy=(1.4, 0.3), fontsize=25,
            horizontalalignment='right',
            verticalalignment='bottom')

#-----------dots----------------------

ax.scatter(1, 0, c='black', s=2)
ax.annotate(r'$(1,0)$',
            xy=(1, 0), fontsize=15,
            horizontalalignment='left',
            verticalalignment='top')

ax.scatter(0, 1, c='black', s=2)
ax.annotate(r'$(0,1)$',
            xy=(0, 1), fontsize=15,
            horizontalalignment='right',
            verticalalignment='bottom')

ax.scatter(1, 1, c='black', s=2)
ax.annotate(r'$(1,1)$',
            xy=(1, 1), fontsize=15,
            horizontalalignment='left',
            verticalalignment='bottom')

#-------------------------------------

legend = ax.legend(loc='upper left', shadow=False, fontsize='x-large', handlelength=0)
plt.grid(alpha=0.5)
plt.show()
