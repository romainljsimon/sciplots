---
icon: lucide/rocket
---

# sciplots

Small helpers for making consistent, publication-ready Matplotlib figures. Set
figure typography and dimensions, configure axes and twin axes in one call, and
label subplot grids consistently. `sciplots` works with ordinary Matplotlib
figures and axes, so you can keep using your existing plotting and export code.

## Install

Install the package from PyPI:

```bash
pip install sciplots
```

## Quick start

```python
import numpy as np
import matplotlib.pyplot as plt
import sciplots as spl

spl.set_style(figsize=(4.15, 4.15))

x = np.logspace(-1, 2, 100)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y, label="data")

spl.configure_axes(
    ax,
    xlabel="x",
    ylabel="y",
    xscale="log",
    yscale="log",
    xlim=(0.1, 100),
    ylim=(0.01, 10000),
)

ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("plot.pdf")
```

## Set a consistent style

`set_style` updates Matplotlib's global `rcParams`. Customize figure size,
font family, label and tick sizes, legend size, TeX rendering, and DPI. The
default figure size is 400 × 200 points, converted to inches.

```python
spl.set_style(
    figsize=(3.32, 2.49),
    font_family="serif",
    labelsize=10,
    xtick_labelsize=8,
    ytick_labelsize=8,
    dpi=300,
)
```

For settings that should apply only to a particular plot or notebook section,
use `style_context`. Matplotlib restores the previous settings when the block
ends:

```python
with spl.style_context(figsize=(3.32, 2.49), font_family="serif"):
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
```

Use `get_params` to build the corresponding `rcParams` dictionary without
applying it. `update_params` is also available as the longer name for
`set_style`.

## Configure axes

`configure_axes` sets limits, scales, ticks, tick labels, and axis labels on an
existing `Axes`. It returns that same axes object. By default it also creates
top and right twin axes; disable either with `xtwin=False` or `ytwin=False`.
Twin tick labels are hidden unless requested with `xtwinlabel=True` or
`ytwinlabel=True`.

```python
spl.configure_axes(
    ax,
    xlim=(0, 10),
    ylim=(0, 100),
    xticks=[0, 5, 10],
    xticklabels=["start", "middle", "end"],
    xlabel="Time",
    ylabel="Value",
    xtwin=False,
    ytwin=False,
)
```

If limits are omitted, the helper uses the first and last values of the first
plotted line when one is available. If tick positions are provided without
custom labels, their string representations are used. Access created twin
axes through `ax.sciplots.twins`, which returns `(x_twin, y_twin)`:

```python
ax = spl.configure_axes(ax, xtwin=True, ytwin=True)
x_twin, y_twin = ax.sciplots.twins
```

## Label panels and style spines

`label_panels` accepts a single axes or an array of axes, and labels them in
row-major order. Labels default to A, B, C, and so on. Its `x` and `y`
positions use axes coordinates, and additional text options are passed to
`Axes.text`:

```python
fig, axes = plt.subplots(1, 2)
spl.label_panels(axes, labels=["A", "B"], fontsize=14, x=0.03, y=0.97)
```

Use `despine` to hide selected spines. It hides the top and right spines by
default and also applies to twin axes created by `configure_axes`:

```python
spl.despine(ax)
```

## Other utilities

- `adjust_lightness(color, amount=0.5)` returns an RGB color with adjusted
  lightness; amounts below 1 darken and amounts above 1 lighten.
- `get_divergent_cmap(data, col1="b", col2="r")` maps values to a linear
  two-color gradient and returns RGBA colors.

All helpers are available from the top-level `sciplots` package as `spl.*`.
