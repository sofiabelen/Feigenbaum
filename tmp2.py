import numpy as np

data = np.genfromtxt('bifurcation-points', names=True)

rc = 0.892486

for i in range(len(data)):
    print(i + 1, " ", np.log(rc - data['rk'][i]))
