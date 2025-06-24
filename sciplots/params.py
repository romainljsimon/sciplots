import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mc
import colorsys
import matplotlib.colors as mcol
import matplotlib.cm as cm


def update_params(fig_width_pt=400, golden_mean=0.5, labelsize=12, legend_fontsize=7, xtick_labesize=8, ytick_labelsize=8):
    """
    Update matplotlib's rcParams for consistent figure formatting.

    Parameters
    ----------
    fig_width_pt : float, optional
        Figure width in points (default is 400).
    golden_mean : float, optional
        Ratio to determine figure height from width (default is 0.5).
    labelsize : int, optional
        Font size for axis labels (default is 12).
    legend_fontsize : int, optional
        Font size for legend text (default is 7).
    xtick_labesize : int, optional
        Font size for x-axis tick labels (default is 8).
    ytick_labelsize : int, optional
        Font size for y-axis tick labels (default is 8).
    """
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
    """
    Adjust the lightness of a given color.

    Parameters
    ----------
    color : str or tuple
        Color name or RGB tuple.
    amount : float, optional
        Factor to adjust lightness (default is 0.5, <1 is darker, >1 is lighter).

    Returns
    -------
    tuple
        RGB tuple of the adjusted color.
    """
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], np.max([0, np.min([1, amount * c[1]])]), c[2])

def get_divergent_cmap(data, col1='b', col2='r'):
    """
    Create a divergent colormap between two colors and map data to it.

    Parameters
    ----------
    data : array-like
        Data to map to the colormap.
    col1 : str, optional
        Color name for one end of the colormap (default is 'b').
    col2 : str, optional
        Color name for the other end of the colormap (default is 'r').

    Returns
    -------
    ndarray
        Array of RGBA values mapped from the input data.
    """
    # Make a user-defined colormap.
    cm1 = mcol.LinearSegmentedColormap.from_list(f"{col1}_to_{col2}",[col1, col2])
    cnorm = mcol.Normalize(vmin=min(data),vmax=max(data))
    cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
    cpick.set_array([])
    return cpick.to_rgba(data)
