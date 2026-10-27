"""Figure 2: filtering throughput of the multiband search and pycbc_inspiral.

Each row of data/throughput.csv is one detector's analysis of one week of O4a
data, giving templates x seconds of data filtered per core-second (job setup
excluded). Bars show the equal-weight mean over analyses for each pipeline.
"""
import numpy as np
import matplotlib.pyplot as plt

from style import DATA, save

PIPELINES = [("multiband", "#d1495b"), ("pycbc_inspiral", "#2e6f95")]


def label(value):
    if value >= 1e4:
        return f"{value / 1e3:.0f}k"
    if value >= 1e3:
        return f"{value / 1e3:.1f}k"
    return f"{value:.0f}"


def main():
    table = np.genfromtxt(DATA / "throughput.csv", delimiter=",", names=True,
                          dtype=None, encoding="utf-8")
    means = [table["templates_per_core"][table["pipeline"] == name].mean()
             for name, _ in PIPELINES]
    top = max(means)

    fig, ax = plt.subplots(figsize=(7.5, 6.5))
    for i, ((name, color), mean) in enumerate(zip(PIPELINES, means)):
        ax.bar(i, mean, 0.55, color=color, zorder=3)
        ax.text(i, mean + 0.028 * top, rf"$\mathbf{{{label(mean)}}}$",
                ha="center", fontsize=18)

    height, drop = 1.17 * top, 0.035 * top
    ax.plot([0, 0, 1, 1], [height - drop, height, height, height - drop],
            color="0.35", lw=1.3, clip_on=False)
    ax.text(0.5, 1.015 * height, rf"$\times{means[0] / means[1]:.1f}$",
            ha="center", va="bottom", fontsize=18, color="0.2")

    ax.set_ylim(0, 1.32 * top)
    ax.set_xlim(-0.65, 1.65)
    ax.set_xticks([0, 1])
    ax.set_xticklabels([name for name, _ in PIPELINES], fontsize=18)
    ax.get_xticklabels()[1].set_fontfamily("monospace")
    ax.tick_params(axis="x", length=0, pad=8)
    ax.tick_params(axis="y", labelsize=15)
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: "0" if v == 0 else f"{v / 1e3:.0f}k"))
    ax.set_ylabel("Templates per core, setup excluded", fontsize=17)
    ax.grid(True, axis="y", alpha=0.3, zorder=0)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.11)
    save(fig, "fig2_throughput")


if __name__ == "__main__":
    main()
