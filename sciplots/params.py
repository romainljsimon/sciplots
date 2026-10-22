from typing import Any, Dict, Optional, Sequence, Tuple, Union

import numpy as np
import colorsys
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.colors as mcol
import matplotlib.cm as cm
from matplotlib import use


Color = Union[str, Tuple[float, float, float]]
Number = Union[int, float]
RcParams = Dict[str, Any]


def get_params(
    figsize: Tuple[Number, Number] = (400 / 72.27, 200 / 72.27),
    labelsize: Number = 12,
    legend_fontsize: Number = 7,
    xtick_labelsize: Number = 8,
    ytick_labelsize: Number = 8,
    font_family: Union[str, Sequence[str]] = "serif",
    usetex: bool = False,
    dpi: Optional[Number] = None,
) -> RcParams:
    """
    Build the rcParams dictionary used by :func:`update_params`.

    This is useful when you want to inspect, merge, or pass the parameters to
    ``plt.rc_context`` yourself.

    Parameters
    ----------
    figsize : tuple of int or float, optional
        Figure size as ``(width, height)`` in inches, following Matplotlib.
    labelsize : int or float, optional
        Font size for axis labels.
    legend_fontsize : int or float, optional
        Font size for legend text.
    xtick_labelsize : int or float, optional
        Font size for x-axis tick labels.
    ytick_labelsize : int or float, optional
        Font size for y-axis tick labels.
    font_family : str or sequence of str, optional
        Font family or ordered list of font families.
    usetex : bool, optional
        Whether to render text with TeX.
    dpi : int or float, optional
        DPI used for figures and saved output. Default is None.

    Returns
    -------
    dict
        Matplotlib rcParams values.
    """
    params = {
        "axes.labelsize": labelsize,
        "legend.fontsize": legend_fontsize,
        "xtick.labelsize": xtick_labelsize,
        "ytick.labelsize": ytick_labelsize,
        "text.usetex": usetex,
        "font.family": font_family,
        "figure.figsize": figsize,
    }
    if dpi is not None:
        params["figure.dpi"] = dpi
        params["savefig.dpi"] = dpi
    return params


def update_params(
    figsize: Tuple[Number, Number] = (400 / 72.27, 200 / 72.27),
    labelsize: Number = 12,
    legend_fontsize: Number = 7,
    xtick_labelsize: Number = 8,
    ytick_labelsize: Number = 8,
    backend: Optional[str] = None,
    font_family: Union[str, Sequence[str]] = "serif",
    usetex: bool = False,
    dpi: Optional[Number] = None,
) -> RcParams:
    """
    Update matplotlib's rcParams for consistent figure formatting.

    Parameters
    ----------
    figsize : tuple of int or float, optional
        Figure size as ``(width, height)`` in inches, following Matplotlib.
    labelsize : int or float, optional
        Font size for axis labels (default is 12).
    legend_fontsize : int or float, optional
        Font size for legend text (default is 7).
    xtick_labelsize : int or float, optional
        Font size for x-axis tick labels (default is 8).
    ytick_labelsize : int or float, optional
        Font size for y-axis tick labels (default is 8).
    backend : str, optional
        Matplotlib backend to use (default is None, which uses the current backend).
    font_family : str or sequence of str, optional
        Font family or ordered list of font families.
    usetex : bool, optional
        Whether to render text with TeX.
    dpi : int or float, optional
        DPI used for figures and saved output. Default is None.

    Returns
    -------
    dict
        The rcParams values that were applied.
    """
    if backend is not None:
        use(backend)
    params = get_params(
        figsize=figsize,
        labelsize=labelsize,
        legend_fontsize=legend_fontsize,
        xtick_labelsize=xtick_labelsize,
        ytick_labelsize=ytick_labelsize,
        font_family=font_family,
        usetex=usetex,
        dpi=dpi,
    )
    plt.rcParams.update(params)
    return params


set_style = update_params


def style_context(
    *args: Any, backend: Optional[str] = None, **kwargs: Any
):
    """
    Temporarily apply sciplots style settings inside a ``with`` block.

    Examples
    --------
    >>> with style_context(figsize=(4.15, 4.15)):
    ...     fig, ax = plt.subplots()
    """
    if backend is not None:
        use(backend)
    return plt.rc_context(get_params(*args, **kwargs))


def adjust_lightness(color: Color, amount: Number = 0.5) -> Tuple[float, float, float]:
    """
    Adjust the lightness of a given color.

    Parameters
    ----------
    color : str or tuple of float
        Matplotlib color name or RGB tuple.
    amount : int or float, optional
        Factor to adjust lightness (default is 0.5, <1 is darker, >1 is lighter).

    Returns
    -------
    tuple
        RGB tuple of the adjusted color.
    """
    try:
        c = mc.cnames[color]
    except (KeyError, TypeError):
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], np.max([0, np.min([1, amount * c[1]])]), c[2])


def get_divergent_cmap(
    data: Union[Sequence[Number], np.ndarray], col1: str = "b", col2: str = "r"
) -> np.ndarray:
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
