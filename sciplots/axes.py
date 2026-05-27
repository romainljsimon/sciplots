from typing import Optional, List, Tuple, Union
import matplotlib.pyplot as plt
import matplotlib.axes

class Axes:
    """
    Helper class to configure matplotlib axes properties, including limits, ticks,
    labels, and scales for both primary and twin axes.
    """
    def __init__(
        self, 
        ax: matplotlib.axes.Axes, 
        xlim: Optional[Tuple[float, float]] = None, 
        ylim: Optional[Tuple[float, float]] = None, 
        xticks: Optional[List[float]] = None, 
        yticks: Optional[List[float]] = None,
        xtickslabel: Optional[List[str]] = None, 
        ytickslabel: Optional[List[str]] = None, 
        xlabel: Optional[str] = None, 
        ylabel: Optional[str] = None,
        xscale: str = "linear", 
        yscale: str = "linear", 
        xtwin: bool = True, 
        ytwin: bool = True,
        xtwinlabel: bool = False, 
        ytwinlabel: bool = False, 
        direction: str = 'in'
    ) -> None:
        """
        Initialize the Axes object and configure the main and twin axes.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The main Axes object to configure.
        xlim : tuple, optional
            Limits for the x-axis (min, max). Default is None.
        ylim : tuple, optional
            Limits for the y-axis (min, max). Default is None.
        xticks : list, optional
            Tick positions on the x-axis. Default is None.
        yticks : list, optional
            Tick positions on the y-axis. Default is None.
        xtickslabel : list, optional
            Labels for x-axis ticks. Default is inferred from `xticks`.
        ytickslabel : list, optional
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

        self.xlim, self.ylim = xlim, ylim
        self.xticks, self.yticks = xticks, yticks
        self.xtickslabel = xtickslabel or (list(map(str, xticks)) if xticks else None)
        self.ytickslabel = ytickslabel or (list(map(str, yticks)) if yticks else None)
        self.xscale, self.yscale = xscale, yscale
        self.xtwinlabel, self.ytwinlabel = xtwinlabel, ytwinlabel
        self.direction = direction
        self._configure_axes(ax, "x")
        self._configure_axes(ax, "y")
        if xtwin:    
            self._configure_axes(ax.twiny(), "x", twin=True)
        if ytwin:
            self._configure_axes(ax.twinx(), "y", twin=True)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        
    
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
            self._set_limits_and_ticks(ax, self.xlim, self.xticks, self.xtickslabel, self.xscale, "x", twin)
        elif axis == "y":
            self._set_limits_and_ticks(ax, self.ylim, self.yticks, self.ytickslabel, self.yscale, "y", twin)
        ax.tick_params(direction=self.direction)

    def _set_limits_and_ticks(
        self, 
        ax: matplotlib.axes.Axes, 
        lim: Optional[Tuple[float, float]], 
        ticks: Optional[List[float]], 
        labels: Optional[List[str]], 
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
        getattr(ax, f"set_{axis}scale")(scale) if scale else None
        getattr(ax, f"set_{axis}lim")(lim) if lim else None
        if ticks is not None:
            tick_labels = [] if twin else labels
            getattr(ax, f"set_{axis}ticks")(ticks, labels=tick_labels)
        elif twin:
            pos = "right" if axis == 'y' else 'top'
            twinlabel = self.xtwinlabel if axis == 'x' else self.ytwinlabel
            ax.tick_params(**{f"label{pos}": twinlabel})
        getattr(ax, f"set_{axis}ticks")([], minor=True)