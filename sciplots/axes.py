from typing import Optional, Sequence, Tuple
import matplotlib.axes

class Axes:
    """
    Helper class to configure matplotlib axes properties, including limits, ticks,
    labels, and scales for both primary and twin axes.

    Most users should call :func:`configure_axes` instead of instantiating this
    class directly.
    """
    def __init__(
        self, 
        ax: matplotlib.axes.Axes, 
        xlim: Optional[Tuple[float, float]] = None, 
        ylim: Optional[Tuple[float, float]] = None, 
        xticks: Optional[Sequence[float]] = None, 
        yticks: Optional[Sequence[float]] = None,
        xticklabels: Optional[Sequence[str]] = None,
        yticklabels: Optional[Sequence[str]] = None,
        xlabel: Optional[str] = None, 
        ylabel: Optional[str] = None,
        xscale: str = "linear", 
        yscale: str = "linear", 
        xtwin: bool = True, 
        ytwin: bool = True,
        xtwinlabel: bool = False, 
        ytwinlabel: bool = False, 
        direction: str = 'in',
        hide_minor_ticks: bool = True,
    ) -> None:
        """
        Initialize the Axes object and configure the main and twin axes.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The main Axes object to configure.
        xlim : tuple, optional
            Limits for the x-axis (min, max). If omitted, use the first and
            last x values of the first plotted line when available.
        ylim : tuple, optional
            Limits for the y-axis (min, max). If omitted, use the first and
            last y values of the first plotted line when available.
        xticks : list, optional
            Tick positions on the x-axis. Default is None.
        yticks : list, optional
            Tick positions on the y-axis. Default is None.
        xticklabels : list, optional
            Labels for x-axis ticks. Default is inferred from `xticks`.
        yticklabels : list, optional
            Labels for y-axis ticks. Default is inferred from `yticks`.
        xlabel : str, optional
            Label for x-axis. Default is None.
        ylabel : str, optional
            Label for y-axis. Default is None.
        xscale : str, optional
            Scale type for the x-axis (e.g., 'linear', 'log'). Default is linear.
        yscale : str, optional
            Scale type for the y-axis (e.g., 'linear', 'log'). Default is linear.
        """

        self.ax = ax
        self.x_twin = None
        self.y_twin = None
        self.xlim = xlim if xlim is not None else self._line_data_limits(ax, "x")
        self.ylim = ylim if ylim is not None else self._line_data_limits(ax, "y")
        self.xticks = self._as_list(xticks)
        self.yticks = self._as_list(yticks)
        self.xticklabels = self._get_tick_labels(self.xticks, xticklabels, "x")
        self.yticklabels = self._get_tick_labels(self.yticks, yticklabels, "y")
        self.xscale, self.yscale = xscale, yscale
        self.xtwinlabel, self.ytwinlabel = xtwinlabel, ytwinlabel
        self.direction = direction
        self.hide_minor_ticks = hide_minor_ticks
        self._configure_axes(ax, "x")
        self._configure_axes(ax, "y")
        if xtwin:    
            self.x_twin = ax.twiny()
            self._configure_axes(self.x_twin, "x", twin=True)
        if ytwin:
            self.y_twin = ax.twinx()
            self._configure_axes(self.y_twin, "y", twin=True)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

    @property
    def twins(self):
        """Return the created twin axes as ``(x_twin, y_twin)``."""
        return self.x_twin, self.y_twin

    @staticmethod
    def _as_list(values):
        if values is None:
            return None
        return list(values)

    @staticmethod
    def _get_tick_labels(ticks, labels, axis):
        if labels is None:
            return list(map(str, ticks)) if ticks is not None else None
        labels = list(labels)
        if ticks is not None and len(labels) != len(ticks):
            raise ValueError(
                f"{axis} tick labels must have the same length as {axis} ticks"
            )
        return labels

    @staticmethod
    def _line_data_limits(ax: matplotlib.axes.Axes, axis: str):
        """Return the first and last data values from the first plotted line."""
        if not ax.lines:
            return None
        data = getattr(ax.lines[0], f"get_{axis}data")()
        if len(data) == 0:
            return None
        return data[0], data[-1]
        
    
    def _configure_axes(self, ax: matplotlib.axes.Axes, axis: str, twin: bool = False) -> None:
        """
        Configure the properties of a single axis (x or y).

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The Axes object to configure.
        axis : str
            The axis to configure ('x' or 'y').
        twin : bool
            Whether the axis is a twin axis.
        """
        if axis == "x":
            self._set_limits_and_ticks(ax, self.xlim, self.xticks, self.xticklabels, self.xscale, "x", twin)
        elif axis == "y":
            self._set_limits_and_ticks(ax, self.ylim, self.yticks, self.yticklabels, self.yscale, "y", twin)
        ax.tick_params(direction=self.direction)

    def _set_limits_and_ticks(
        self, 
        ax: matplotlib.axes.Axes, 
        lim: Optional[Tuple[float, float]], 
        ticks: Optional[Sequence[float]], 
        labels: Optional[Sequence[str]], 
        scale: str, 
        axis: str, 
        twin: bool
    ) -> None:
        """
        Set limits, ticks, labels, and scale for a specific axis.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The Axes object to configure.
        lim : tuple, optional
            Axis limits (min, max). Default is None.
        ticks : list, optional
            Tick positions. Default is None.
        labels : list, optional
            Tick labels. Default is inferred from `ticks`.
        scale : str, optional
            Scale type (e.g., 'linear', 'log'). Default is None.
        twin : bool
            Whether the axis is a twin axis.
        axis : str
            The axis to configure ('x' or 'y').
        """
        # Set scale, limits, and ticks
        if scale:
            getattr(ax, f"set_{axis}scale")(scale)
        if lim is not None:
            getattr(ax, f"set_{axis}lim")(lim)
        if ticks is not None:
            tick_labels = [] if twin else labels
            getattr(ax, f"set_{axis}ticks")(ticks, labels=tick_labels)
        elif twin:
            pos = "right" if axis == 'y' else 'top'
            twinlabel = self.xtwinlabel if axis == 'x' else self.ytwinlabel
            ax.tick_params(**{f"label{pos}": twinlabel})
        if self.hide_minor_ticks:
            getattr(ax, f"set_{axis}ticks")([], minor=True)


def configure_axes(ax: matplotlib.axes.Axes, **kwargs) -> matplotlib.axes.Axes:
    """
    Configure an existing Matplotlib axes and return it for chaining.

    The :class:`Axes` helper object is stored on ``ax.sciplots`` so twin axes
    remain accessible as ``ax.sciplots.x_twin`` and ``ax.sciplots.y_twin``.
    """
    ax.sciplots = Axes(ax, **kwargs)
    return ax
