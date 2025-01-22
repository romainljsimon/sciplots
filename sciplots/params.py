import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mc
import colorsys


def update_params(fig_width_pt=400, golden_mean=0.5):
    inches_per_pt = 1.0/72.27               # Convert pt to inch
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    fig_size =  [fig_width, fig_height]

    params = {'backend': 'pdf',
            'axes.labelsize': 12,  
            'legend.fontsize': 7,
            'xtick.labelsize': 8,
            'ytick.labelsize': 8,
            'text.usetex': False,
            'font.family': 'serif',
            'figure.figsize': fig_size}

    plt.rcParams.update(params)

def adjust_lightness(color, amount=0.5):
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], np.max([0, np.min([1, amount * c[1]])]), c[2])
