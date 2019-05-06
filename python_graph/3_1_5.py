from base import *

m = 0.5
p = 0.8

def A(m):
    if m < 2 / 3:
        return (2 - 3*m) / (2 + (sqrt(2) - 3) * m), 0
    else:
        return 0, (3*m - 2) / (2*(sqrt(2) - 1) + (3 - 2*sqrt(2))*m)

def B(m):
    if m < 1 / 3:
        return (1 - 3*m) / (1 + (2*sqrt(2) - 3)*m), 0
    else:
        return 0, (3*m - 1) / (sqrt(2) - 1 + (3 - sqrt(2))*m)

def l_1_function(x, y):
    global m
    l_1 = (1 - x + (sqrt(2) - 1) * y) / m
    l_2 = (1 - y + (sqrt(2) - 1) * x) / (2 * (1 - m))
    return l_1 - l_2

def l_2_function(x, y):
    global m
    l_3 = (1 - x + (sqrt(2) - 1) * y) / (2 * m)
    l_4 = (1 - y + (sqrt(2) - 1) * x) / (1 - m)
    return l_3 - l_4

def g_1(p, m):
    return (sqrt(2) - 1)*p*m - (1 - p)*(1 - m)

def g_2(p, m):
    return (1 - p)*(1 - m)*(sqrt(2) - 1) - p*m

def l_3_function(x):
    global m, p
    c = -0.1
    return (c - g_1(p, m)*x) / g_2(p, m)

k = 0.5
def l_4_function(x):
    global k
    c = 0.2
    return k*x + c 

def sector_1(x, y):
    return (l_1_function(x, y) > 0) and (l_2_function(x, y) < 0) and \
            (y >= 0) and (y <= 1) and (x >= 0) and (x <= 1)

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
# line(ax, l_4_function, color='black', label=r'$\ell: \; q_2=k(p,\mu)q_0 + c(p,\mu)$')

#-----------labels--------------------

ax.annotate(r'$A(\mu)$',
            xy=A(m), fontsize=25,
            horizontalalignment='right',
            verticalalignment='bottom')
ax.scatter(*A(m), c='black')

ax.annotate(r'$B(\mu)$',
            xy=B(m), fontsize=25,
            horizontalalignment='right',
            verticalalignment='bottom')
ax.scatter(*B(m), c='black')

x = 0.5
y = 0.5#l_4_function(x)
length = 0.2# / sqrt(1 + k ** 2)
dx = -length
dy = 0#length# * k
ax.plot([0,1], [0.5, 0.5],color='black', linewidth=2, label=r'$\ell: \; q_2=k(p,\mu)q_0 + c(p,\mu)$')
ax.arrow(x,y,dy,dx, head_length=length*0.2, head_width=0.02, color='black')

#-------------------------------------

legend = ax.legend(loc='upper left', shadow=False, fontsize='x-large', handlelength=0)
plt.grid(alpha=0.5)
plt.show()
