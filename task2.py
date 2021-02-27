import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Parameters
rsteps = 10000
nsteps = 1000
nrepeat = 100
x0 = 0.01
eps = 0.0001

def f(x, r):
    return 4 * r * x * (1 - x)

def getLimit(r, x0, steps):
    x = x0
    for i in range(0, steps):
        x = f(x, r)
    return x

def getValues(rsteps, rstart, rend):
    xlim = np.zeros(rsteps * nrepeat)
    rvalues = np.zeros(rsteps * nrepeat)

    for i in range(0, rsteps):
        r = rstart + (rend - rstart) * i / rsteps
        xlim[i] = getLimit(r, x0, nsteps)
    
        for j in range(1, nrepeat):
            xlim[i + j * rsteps] = f(xlim[i + (j - 1) * rsteps], r)
    
        for j in range(0, nrepeat):
            rvalues[i + j * rsteps] = r
    return rvalues, xlim

def getBifurcations(rsteps, rstart, rend, xlim):
    rbif = np.zeros(5)
    curperiod = 0

    i = 0
    j = 0
    while j < 5:
        r = rstart + (rend - rstart) * i / rsteps
        if r >= 3 / 4:
            xcur = f(xlim[i], r)
            period = 0

            while abs(xcur - xlim[i]) >= eps:
                xcur = f(xcur, r)
                period += 1
            
            if curperiod < period:
                rbif[j] = r
                print("r:", r, " period:", period + 1)
                j += 1
                curperiod = period
        i += 1

    return rbif

## PLotting
sns.set(palette='colorblind')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7))
fig.suptitle(r'Limiting Value of $4rx_n(1 - x_n)$: Bifurcation Points')
ax1.set_xlabel(r'$r$')
ax1.set_ylabel(r'$x^* = \lim_{n \to \infty} 4rx_n(1 - x_n)$')
ax2.set_xlabel(r'$r$')

rvalues, xlim = getValues(rsteps, 0, 1)
rbif = getBifurcations(rsteps, 0, 1, xlim)

ax1.scatter(rvalues, xlim, s=0.4)
ax1.vlines(rbif, 0, 1, color='black')
ax1.set_xlim(left=0.7)

rvalues, xlim = getValues(rsteps, .885, .90)
ax2.scatter(rvalues, xlim, s=0.4)
ax2.vlines(rbif[2:], 0, 1, color='black')
ax2.set_ylim(bottom=0.3, top=0.9)

fig.savefig("img/task2.pdf")
fig.savefig("img/task2.png", dpi=300)
fig.savefig("img/task2.svg")
