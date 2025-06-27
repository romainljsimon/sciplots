import numpy as np
import matplotlib.pyplot as plt
import sciplots as spl


x = np.linspace(0.1, 100, 100)
y1 = x**2

plt.figure()
plt.plot(x, y1, label=r'$y = x^2$', color='blue')
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.show()

#spl.update_params(fig_width_pt=300, golden_mean=1.0, backend='pdf')
fig, ax = plt.subplots()
ax.plot(x, y1, label=r'$y = x^2$', color='blue')
spl.Axes(ax, xlim=(0.1, 100), ylim=(0.01, 10000), xscale='log', yscale='log')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x)$')
ax.legend()
plt.show()