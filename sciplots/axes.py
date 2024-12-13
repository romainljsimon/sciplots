import matplotlib.pyplot as plt

class Axes:
    """
    A helper class to configure the properties of matplotlib axes, including limits, ticks,
    labels, and scales for both primary and twin axes.

    Attributes:
        xlim (tuple, optional): Limits for the x-axis (min, max). Default is None.
        ylim (tuple, optional): Limits for the y-axis (min, max). Default is None.
        xticks (list, optional): Tick positions on the x-axis. Default is None.
        yticks (list, optional): Tick positions on the y-axis. Default is None.
        xtickslabel (list, optional): Labels for x-axis ticks. Default is inferred from `xticks`.
        ytickslabel (list, optional): Labels for y-axis ticks. Default is inferred from `yticks`.
        xscale (str, optional): Scale type for the x-axis (e.g., 'linear', 'log'). Default is None.
        yscale (str, optional): Scale type for the y-axis (e.g., 'linear', 'log'). Default is None.
    """
    def __init__(self, ax, xlim=None, ylim=None, xticks=None, yticks=None, 
                 xtickslabel=None, ytickslabel=None, xscale=None, yscale=None):
        """
        Initialize the Axes object and configure the main and twin axes.

        Args:
            ax (matplotlib.axes.Axes): The main Axes object to configure.
            xlim (tuple, optional): Limits for the x-axis (min, max). Default is None.
            ylim (tuple, optional): Limits for the y-axis (min, max). Default is None.
            xticks (list, optional): Tick positions on the x-axis. Default is None.
            yticks (list, optional): Tick positions on the y-axis. Default is None.
            xtickslabel (list, optional): Labels for x-axis ticks. Default is inferred from `xticks`.
            ytickslabel (list, optional): Labels for y-axis ticks. Default is inferred from `yticks`.
            xscale (str, optional): Scale type for the x-axis (e.g., 'linear', 'log'). Default is None.
            yscale (str, optional): Scale type for the y-axis (e.g., 'linear', 'log'). Default is None.
        """
        self.xlim, self.ylim = xlim, ylim
        self.xticks, self.yticks = xticks, yticks
        self.xtickslabel = xtickslabel or (list(map(str, xticks)) if xticks else None)
        self.ytickslabel = ytickslabel or (list(map(str, yticks)) if yticks else None)
        self.xscale, self.yscale = xscale, yscale

        self._configure_axes(ax, "x", twin=False)
        self._configure_axes(ax.twiny(), "x", twin=True)
        self._configure_axes(ax, "y", twin=False)
        self._configure_axes(ax.twinx(), "y", twin=True)

    def _configure_axes(self, ax, axis, twin):
        """
        Configure the properties of a single axis (x or y).

        Args:
            ax (matplotlib.axes.Axes): The Axes object to configure.
            axis (str): The axis to configure ('x' or 'y').
            twin (bool): Whether the axis is a twin axis. Default is False.
        """
        if axis == "x":
            self._set_limits_and_ticks(ax, self.xlim, self.xticks, self.xtickslabel, self.xscale, twin, "x")
        elif axis == "y":
            self._set_limits_and_ticks(ax, self.ylim, self.yticks, self.ytickslabel, self.yscale, twin, "y")
        ax.tick_params(direction='in')

    def _set_limits_and_ticks(self, ax, lim, ticks, labels, scale, twin, axis):
        """
        Set limits, ticks, labels, and scale for a specific axis.

        Args:
            ax (matplotlib.axes.Axes): The Axes object to configure.
            lim (tuple, optional): Axis limits (min, max). Default is None.
            ticks (list, optional): Tick positions. Default is None.
            labels (list, optional): Tick labels. Default is inferred from `ticks`.
            scale (str, optional): Scale type (e.g., 'linear', 'log'). Default is None.
            twin (bool): Whether the axis is a twin axis. Default is False.
            axis (str): The axis to configure ('x' or 'y').
        """
        # Set scale, limits, and ticks
        getattr(ax, f"set_{axis}scale")(scale) if scale else None
        getattr(ax, f"set_{axis}lim")(lim) if lim else None
        if ticks is not None:
            tick_labels = [] if twin else labels
            getattr(ax, f"set_{axis}ticks")(ticks, labels=tick_labels)
        elif twin:
            pos = "right" if axis == 'y' else 'top'
            ax.tick_params(**{f"label{pos}": False})
        getattr(ax, f"set_{axis}ticks")([], minor=True)