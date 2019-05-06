from base import *

m = 0.5

def A(m):
    if m < 2 / 3:
        return (2 - 3*m) / (2 + (sqrt(2) - 3) * m), 0
    else:
        return 0, (3*m - 2) / (2*(sqrt(2) - 1) + (3 - 2*sqrt(2))*m)

def l_1_function(x, y):
    global m
    l_1 = (1 - x + (sqrt(2) - 1) * y) / m
    l_2 = (1 - y + (sqrt(2) - 1) * x) / (2 * (1 - m))
    return l_1 - l_2

def l_2_function(x):
    return (x - 0.5) / (sqrt(2)-1)

def sector_1(x, y):
    return (l_1_function(x, y) < 0) and  (y >= 0) and (y <= 1) and (x >= 0) and (x <= 1)

plt.rc('text', usetex=True)
fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111)
plt.xlim(0, 1)
plt.ylim(0, 1)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
plt.xlabel(r'$q_0$', fontsize=16)
plt.ylabel(r'$q_2$', fontsize=16)

#-----------figures---------------------

sector(ax, sector_1, color='lightgreen')
line(ax, l_2_function, color='black', label=r'$\ell_2: \; q_2=(\sqrt{2} - 1)q_0 + c$')

#-----------labels--------------------

ax.annotate(r'$A(\mu)$',
            xy=A(m), fontsize=25,
            horizontalalignment='right',
            verticalalignment='bottom')
ax.scatter(*A(m), c='black')

#-------------------------------------

legend = ax.legend(loc='upper left', shadow=False, fontsize='x-large', handlelength=0)
plt.grid(alpha=0.5)
plt.show()
