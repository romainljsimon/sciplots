import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mc
import colorsys
import matplotlib.colors as mcol
import matplotlib.cm as cm


def update_params(fig_width_pt=400, golden_mean=0.5):
    inches_per_pt = 1.0/72.27               # Convert pt to inch
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    fig_size =  [fig_width, fig_height]

    params = {'backend': 'pdf',
            'axes.labelsize': labelsize,  
            'legend.fontsize': legend_fontsize,
            'xtick.labelsize': xtick_labesize,
            'ytick.labelsize': ytick_labelsize,
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

def get_divergent_cmap(data, col1='b', col2='r'):
    # Make a user-defined colormap.
    cm1 = mcol.LinearSegmentedColormap.from_list(f"{col1}_to_{col2}",[col1, col2])
    cnorm = mcol.Normalize(vmin=min(data),vmax=max(data))
    cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
    cpick.set_array([])
    return cpick.to_rgba(data)
