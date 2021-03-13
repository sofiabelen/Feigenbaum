import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Parameters
rsteps = 10000
ind = 1000

def f(x, r):
    return 4 * r * x * (1 - x)

def getLimit(r, x0, steps):
    x = x0
    for i in range(0, steps):
        x = f(x, r)
    return x

## Plotting
sns.set(palette='colorblind', context='notebook')
fig, axs = plt.subplots(2, 2, figsize=(15, 13))
fig.suptitle(r'Limiting Value of $4rx_n(1 - x_n)$: Stability with respect to starting conditions')

r = [0.8, 0.87, 0.93, 0.96]
i = 0
xzeros = np.arange(0, 1, 1 / rsteps)

for row in axs:
    for ax in row:
        ax.set_xlabel(r'$x_0$')
        ax.set_ylabel(r'$x_{%d}$'%(ind))
        ax.set_title(r'$r = $ %.2f'%(r[i]))

        xn = np.zeros(rsteps)
        for j in range(rsteps):
           xn[j] = getLimit(r[i], xzeros[j], ind)

        ax.scatter(xzeros[1:], xn[1:], s=0.4)
        i += 1

# fig.savefig("img/task4.pdf")
fig.savefig("img/task4.png", dpi=200)
# fig.savefig("img/task4.svg")
