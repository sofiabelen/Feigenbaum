import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Parameters
rsteps = 10000
nsteps = 1000
rvalues = np.zeros(rsteps)
x0 = 0.01

def f(x, r):
    return 4 * r * x * (1 - x)

def getLimit(r, x0, steps):
    x = x0
    for i in range(0, steps):
        x = f(x, r)
    return x

for i in range(0, rsteps):
    rvalues[i] = getLimit(i / rsteps, x0, nsteps)
    # print('r= ', i / rsteps, ' x^* = ', rvalues[i])

## PLotting
sns.set(context='notebook', palette='colorblind')
fig, ax = plt.subplots(figsize=(9, 9))
ax.set_title(r'Limiting value')
ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$x^* = \lim_{n \to \infty} 4rx_n(1 - x_n)$')

ax.scatter(np.arange(0, 1, step=1.0 / rsteps), rvalues, s=0.6)

fig.savefig("img/task2.pdf")
fig.savefig("img/task2.png")
plt.show()
