"""Helpers for styling Matplotlib axes spines."""

import matplotlib.axes


def despine(ax, *, top: bool = True, right: bool = True,
            left: bool = False, bottom: bool = False):
    """Hide selected spines on one or more Matplotlib axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes or iterable of Axes
        Axes whose spines to update.
    top, right, left, bottom : bool, optional
        Whether to hide each corresponding spine. The top and right spines are
        hidden by default.

    Returns
    -------
    Axes or list of Axes
        The input axes, allowing the helper to fit into plotting workflows.
    """
    if isinstance(ax, matplotlib.axes.Axes):
        axes = [ax]
        result = ax
    else:
        axes = list(ax)
        result = axes

    if not all(isinstance(item, matplotlib.axes.Axes) for item in axes):
        raise TypeError("ax must be a Matplotlib Axes or an iterable of Axes")

    hidden = {"top": top, "right": right, "left": left, "bottom": bottom}
    all_axes = list(axes)
    for item in axes:
        helper = getattr(item, "sciplots", None)
        if helper is not None:
            all_axes.extend(twin for twin in helper.twins if twin is not None)

    for item in all_axes:
        for name, should_hide in hidden.items():
            if should_hide:
                item.spines[name].set_visible(False)
                item.tick_params(
                    **{name: False, f"label{name}": False}
                )

    return result
