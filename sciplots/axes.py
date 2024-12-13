import matplotlib.pyplot as plt

class Axes():

    def __init__(self, ax, xlim=None, ylim=None, xticks=None, yticks=None, xtickslabel=None, ytickslabel=None):
        self.xlim, self.ylim = xlim, ylim
        self.xticks, self.yticks = xticks, yticks
        self.xtickslabel, self.ytickslabel = xtickslabel, ytickslabel
        self._labels()
        self._configure_axis(ax)
        self._configure_axis(ax.twiny(), twin=True)
        self._configure_axis(ax, axis="y")
        self._configure_axis(ax.twinx(), axis="y", twin=True)

    def _configure_axis(self, ax, axis="x", twin=False):
        if axis == "x":
            if self.xticks is not None:
                labels = self.xtickslabel if not twin else []
                ax.set_xticks(self.xticks, labels=labels)
            ax.set_xticks([], minor=True)
        elif axis == "y":
            if self.yticks is not None:
                labels = self.ytickslabel if not twin else []
                ax.set_yticks(self.yticks, labels=self.ytickslabel)
            ax.set_yticks([], minor=True)
        ax.tick_params(direction='in')

    def _labels(self):
        self.xtickslabel = self.xtickslabel or (list(map(str, self.xticks)) if self.xticks else None)
        self.ytickslabel = self.ytickslabel or (list(map(str, self.yticks)) if self.yticks else None)
        