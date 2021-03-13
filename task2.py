import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline

def line(x, a, b):
    return a*x + b

data = np.genfromtxt('bifurcation-points', names=True)

def f(k, A, delta):
    rc = 0.892486
    return rc - A * delta**(-k)

popt, pcov = curve_fit(f=f, xdata=data['k'], ydata=data['rk'])

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlabel(r'$k$')
ax.set_ylabel(r'$r_k$')

ax.set_title("Feigenbaum constant")
ax.scatter(x=data['k'], y=data['rk'])
ax.plot(np.arange(1, 6, 0.01), f(np.arange(1, 6, 0.01), popt[0], popt[1]),\
        label=r'$r_k = r_c - A \cdot \delta^{-k}, \quad \delta = %.4f$'%popt[1])
ax.legend()


fig.savefig("img/task2.pdf")
fig.savefig("img/task2.png", dpi=200)
fig.savefig("img/task2.svg")
plt.show()
