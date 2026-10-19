import matplotlib.pyplot as plt
import pytest
import sciplots as spl


@pytest.fixture
def ax():
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)


def test_configure_axes_sets_limits_scales_ticks_and_labels(ax):
    result = spl.configure_axes(
        ax,
        xlim=(1, 10),
        ylim=(-2, 2),
        xticks=[1, 5, 10],
        xticklabels=["low", "mid", "high"],
        yticks=[-2, 0, 2],
        yticklabels=["min", "zero", "max"],
        xlabel="Time",
        ylabel="Value",
        xscale="log",
        xtwin=False,
        ytwin=False,
    )

    assert result is ax
    assert ax.get_xlim() == pytest.approx((1, 10))
    assert ax.get_ylim() == pytest.approx((-2, 2))
    assert ax.get_xscale() == "log"
    assert ax.get_xticks() == pytest.approx([1, 5, 10])
    assert [tick.get_text() for tick in ax.get_xticklabels()] == [
        "low",
        "mid",
        "high",
    ]
    assert [tick.get_text() for tick in ax.get_yticklabels()] == [
        "min",
        "zero",
        "max",
    ]
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Value"
    assert ax.sciplots.twins == (None, None)


def test_configure_axes_creates_requested_twins(ax):
    spl.configure_axes(ax, xtwin=True, ytwin=False)

    x_twin, y_twin = ax.sciplots.twins
    assert x_twin is not None
    assert y_twin is None
    assert x_twin in ax.figure.axes


def test_configure_axes_rejects_mismatched_tick_labels(ax):
    with pytest.raises(ValueError, match="x tick labels must have the same length"):
        spl.configure_axes(ax, xticks=[0, 1], xticklabels=["only one"])


def test_style_context_applies_settings_temporarily():
    original_family = plt.rcParams["font.family"]
    original_figsize = plt.rcParams["figure.figsize"]

    with spl.style_context(fig_width_pt=240, aspect_ratio=0.75, font_family="sans-serif"):
        assert plt.rcParams["font.family"] == ["sans-serif"]
        assert plt.rcParams["figure.figsize"] == pytest.approx(
            spl.figure_size(240, 0.75)
        )

    assert plt.rcParams["font.family"] == original_family
    assert plt.rcParams["figure.figsize"] == pytest.approx(original_figsize)


def test_get_params_returns_figure_and_dpi_settings():
    params = spl.get_params(fig_width_pt=300, aspect_ratio=0.5, dpi=150)

    assert params["figure.figsize"] == pytest.approx(spl.figure_size(300, 0.5))
    assert params["figure.dpi"] == 150
    assert params["savefig.dpi"] == 150
