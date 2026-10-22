import numpy as np
import matplotlib.pyplot as plt
import sciplots as spl

if __name__ == '__main__':
    x = np.linspace(0, 10, 100)
    with spl.style_context(figsize=(7, 3),
                            legend_fontsize=12,
                            xtick_labelsize=12,
                            ytick_labelsize=12):
        
        _, ax = plt.subplots(1, 2)
        ax[0].plot(x, x**2, label=r'$y = x^2$', color='blue')
        ax[1].plot(x, np.exp(x), label=r'$y = \exp(x)$', color='blue')
        spl.configure_axes( ax[0], xlim=(0.1, 10), ylim=(0.01, 10**2),
                            xscale='log', yscale='log',
                            xlabel=r'$x$', ylabel=r'$y(x)$')

        spl.configure_axes( ax[1], xlim=(0, 10), ylim=(1, 10**4),
                            xscale='linear', yscale='log',
                            xlabel=r'$x$', ylabel=r'$y(x)$')
        ax[0].legend(frameon=False)
        ax[1].legend(frameon=False)
        spl.label_panels(ax, labels=['(a)', '(b)'], fontsize=12)
        plt.tight_layout(pad=2)
        plt.savefig("panels_plot.png", dpi=300)
        plt.show()
