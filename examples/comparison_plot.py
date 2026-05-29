from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import sciplots as spl


OUTPUT_DIR = Path(__file__).parent


def make_data():
    x = np.linspace(1e-3, 1e3, 2)
    return x, x**2


def save_default_plot(x, y):
    fig, ax = plt.subplots()
    inchtopt = 0.0138888889 
    fig.set_size_inches(300 * inchtopt, 300 * inchtopt)
    ax.plot(x, y, label=r"$y = x^2$", color="blue")
    ax.set(
        xlabel=r"$x$",
        ylabel=r"$y(x)$",
        xlim=(1e-3, 1e3),
        ylim=(1e-6, 1e6),
        xscale="log",
        yscale="log",
    )
    ax.xaxis.label.set_size(14)
    ax.yaxis.label.set_size(14)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "comparison_plot_default.pdf")
    plt.close(fig)


def save_sciplots_plot(x, y):
    with spl.style_context(
        fig_width_pt=300,
        aspect_ratio=1.0,
        legend_fontsize=10,
        xtick_labelsize=10,
        ytick_labelsize=10,
    ):
        fig, ax = plt.subplots()
        ax.plot(x, y, label=r"$y = x^2$", color="blue")
        spl.configure_axes(
            ax,
            xlim=(1e-3, 1e3),
            ylim=(1e-6, 1e6),
            xscale="log",
            yscale="log",
            xlabel=r"$x$",
            ylabel=r"$y(x)$",
        )
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(OUTPUT_DIR / "comparison_plot_sciplots.pdf")
        plt.close(fig)


def main():
    x, y = make_data()
    save_default_plot(x, y)
    save_sciplots_plot(x, y)


if __name__ == "__main__":
    main()
