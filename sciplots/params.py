import matplotlib.pyplot as plt


def update_params(fig_width_pt=400, golden_mean=0.5):
    fig_width_pt = 400     # Get this from LaTeX using \the\columnwidth
    inches_per_pt = 1.0/72.27               # Convert pt to inch
    golden_mean = 0.4     # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    fig_size =  [fig_width, fig_height]

    params = {#'backend': 'macosx',
            'axes.labelsize': 12,  
            'legend.fontsize': 7,
            'xtick.labelsize': 8,
            'ytick.labelsize': 8,
            'text.usetex': False,
            'font.family': 'serif',
            'figure.figsize': fig_size}

    plt.rcParams.update(params)
