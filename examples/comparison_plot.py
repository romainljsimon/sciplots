import numpy as np
import matplotlib.pyplot as plt
import sciplots as spl


def plot_default(x, y, filename='comparison_plot_default.pdf'):
    plt.figure()
    plt.tight_layout()
    plt.plot(x, y, label=r'$y = x^2$', color='blue')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y(x)$')
    plt.xlim(0.1, 100)
    plt.ylim(0.01, 10000)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(filename)
    plt.show()


def plot_sciplots(x, y, filename='comparison_plot_sciplots.pdf'):
    with spl.style_context( fig_width_pt=300,
                            aspect_ratio=1.0,
                            legend_fontsize=10,
                            xtick_labelsize=10,
                            ytick_labelsize=10):

        _, ax = plt.subplots()
        plt.tight_layout(pad=2)
        ax.plot(x, y, label=r'$y = x^2$', color='blue')
        spl.configure_axes(ax, xlim=(0.1, 100), ylim=(0.01, 10000),
                        xscale='log', yscale='log',
                        xlabel=r'$x$', ylabel=r'$y(x)$')
        ax.legend(frameon=False)
        plt.savefig(filename)
        plt.show()
        

if __name__ == '__main__':
    x = np.linspace(0.1, 100, 100)
    y = x**2
    plot_default(x, y)
    plot_sciplots(x, y)

