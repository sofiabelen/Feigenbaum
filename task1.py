import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Parameters
rsteps = 1000
nsteps = 1000
nrepeat = 100
x0 = 0.01

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

## PLotting
sns.set(context='notebook', palette='colorblind')
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig.suptitle(r'Limiting value of $4rx_n(1 - x_n)$')
ax1.set_xlabel(r'$r$')
ax1.set_ylabel(r'$x^* = \lim_{n \to \infty} 4rx_n(1 - x_n)$')
ax2.set_xlabel(r'$r$')

rvalues, xlim = getValues(rsteps, 0, 1)
ax1.scatter(rvalues, xlim, s=0.5)

rvalues, xlim = getValues(rsteps, .86, 1)
ax2.scatter(rvalues, xlim, s=0.5)

fig.savefig("img/task1.pdf")
fig.savefig("img/task1.png")
fig.savefig("img/task1.svg")

plt.show()
