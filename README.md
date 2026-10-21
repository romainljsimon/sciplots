# sciplots

Simple plotting utilities for `matplotlib` with clean defaults, optional twin
axes, and helpers for publication-sized figures.

## Quick start

```python
import matplotlib.pyplot as plt
import sciplots as spl

spl.set_style(fig_width_pt=300, aspect_ratio=1.0)

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

## Temporary style

Use `style_context` when you only want the style to apply to one plot or one
section of a notebook:

```python
with spl.style_context(fig_width_pt=240, aspect_ratio=0.75, font_family="serif"):
    fig, ax = plt.subplots()
    ax.plot(x, y)
```

## Axes helper

`configure_axes` returns the original Matplotlib axes, so it fits naturally into
existing plotting code. The underlying helper is attached to `ax.sciplots`:

```python
ax = spl.configure_axes(ax, xtwin=True, ytwin=True)
x_twin, y_twin = ax.sciplots.twins
```

Use `xticklabels` and `yticklabels` to set custom tick labels:

```python
spl.configure_axes(
    ax,
    xticks=[0, 1, 2],
    xticklabels=["low", "mid", "high"],
)
```

## Panel labels

Add consistent labels to a subplot grid. Labels default to A, B, C, and
so on, and can be customized with `x`, `y`, and `Axes.text` keyword arguments:

```python
fig, axes = plt.subplots(1, 2)
spl.label_panels(axes, labels=["A", "B"], fontsize=14, x=0.03, y=0.97)
```
