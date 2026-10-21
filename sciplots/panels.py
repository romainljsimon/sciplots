"""Helpers for labeling multi-panel figures."""

from string import ascii_uppercase
from typing import List, Optional, Sequence

import matplotlib.axes
import numpy as np


def label_panels(
    axes,
    labels: Optional[Sequence[str]] = None,
    *,
    x: float = 0.03,
    y: float = 0.97,
    **text_kwargs,
) -> List:
    """Add consistent panel labels to one or more Matplotlib axes.

    ``axes`` may be a single axes or an iterable/NumPy array of axes. Arrays
    are labeled in row-major order. Labels default to A, B, C, and so on.
    ``x`` and ``y`` are positions in axes coordinates; extra keyword arguments
    are passed to ``Axes.text``.

    Returns the created text artists in axes order.
    """
    if isinstance(axes, matplotlib.axes.Axes):
        axes = [axes]
    else:
        axes = list(np.asarray(axes, dtype=object).ravel())
    if not axes:
        return []
    if not all(isinstance(ax, matplotlib.axes.Axes) for ax in axes):
        raise TypeError("axes must contain only Matplotlib Axes objects")

    if labels is None:
        labels = [
            ascii_uppercase[i % 26] + (str(i // 26) if i >= 26 else "")
            for i in range(len(axes))
        ]
    else:
        labels = list(labels)
        if len(labels) != len(axes):
            raise ValueError("the number of panel labels must match the number of axes")

    style = {"fontsize": 12, "color": "black"}
    style.update(text_kwargs)
    return [
        ax.text(x, y, label, transform=ax.transAxes, ha="left", va="top", **style)
        for ax, label in zip(axes, labels)
    ]
