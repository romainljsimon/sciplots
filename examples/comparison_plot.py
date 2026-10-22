import numpy as np
import matplotlib.pyplot as plt
import sciplots as spl


def plot_default(x, y, filename='comparison_plot_default.png'):
    plt.rcParams['font.family'] = 'serif'
    fig, ax = plt.subplots(figsize=(4.15, 4.15))
    ax.plot(x, y, label=r'$y = x^2$', color='blue')
    ax.set_xlabel(r'$x$', fontsize=12)
    ax.set_ylabel(r'$y$', fontsize=12)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend(frameon=False, fontsize=12)
    fig.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


def plot_sciplots(x, y, filename='comparison_plot_sciplots.png'):
    with spl.style_context( figsize=(4.15, 4.15),
                            legend_fontsize=12,
                            xtick_labelsize=12,
                            ytick_labelsize=12,
                            labelsize=12):

        fig, ax = plt.subplots()
        ax.plot(x, y, label=r'$y = x^2$', color='blue')
        spl.configure_axes( ax,
                            xscale='log', yscale='log',
                            xlabel=r'$x$', ylabel=r'$y$')
        ax.legend(frameon=False)
        fig.tight_layout()
        plt.savefig(filename, dpi=300)
        plt.show()
        

if __name__ == '__main__':
    x = np.linspace(0.1, 100, 100)
    y = x**2
    plot_default(x, y)
    plot_sciplots(x, y)

