"""Figure 16: sensitive VT of each template bank relative to TaylorF2Ecc.

data/bank_comparison.csv gives VT for one week of O4a data, for two injection
sets (aligned and precessing spin) in two eccentricity regimes, at three IFAR
thresholds. Ratio errors account for the banks searching the same injections.
"""
import numpy as np
import matplotlib.pyplot as plt

from style import DATA, save

REGIMES = [("high_ecc", r"$e_{20} \simeq 0.28$"), ("low_ecc", r"$e_{20} \leq 0.1$")]
INJECTIONS = [("aligned", "higher-order modes,\naligned spin", "o", True, 0),
              ("precessing", "higher-order modes,\nprecessing", "s", False, 5)]
BANKS = ["TaylorF2", "TaylorF2Ecc", "TEOBResumS"]
IFARS = [1, 10, 100]
COLORS = ["#7b7fd4", "#e8743b", "#6aba7f"]


def main():
    table = np.genfromtxt(DATA / "bank_comparison.csv", delimiter=",", names=True,
                          dtype=None, encoding="utf-8")

    plt.rcParams.update({"font.size": 12, "axes.labelsize": 14,
                         "axes.titlesize": 14, "xtick.labelsize": 13,
                         "ytick.labelsize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.4), sharey=True)

    for ax, (regime, title) in zip(axes, REGIMES):
        for s, (inj, _, marker, filled, caps) in enumerate(INJECTIONS):
            for c, ifar in enumerate(IFARS):
                for b, bank in enumerate(BANKS):
                    row = table[(table["regime"] == regime)
                                & (table["injections"] == inj)
                                & (table["ifar_yr"] == ifar)
                                & (table["bank"] == bank)][0]
                    ax.errorbar(b + 0.22 * (c - 1) + 0.085 * (s - 0.5),
                                row["ratio"], yerr=row["ratio_err"],
                                marker=marker, ms=7, color=COLORS[c],
                                mfc=COLORS[c] if filled else "white",
                                mec=COLORS[c], mew=1.4, elinewidth=2,
                                capsize=caps, capthick=1.6)
        ax.axhline(1.0, color="k", lw=1.2)
        ax.set_xticks(range(len(BANKS)))
        ax.set_xticklabels(BANKS)
        ax.set_xlim(-0.55, len(BANKS) - 0.45)
        ax.set_xlabel("template bank")
        ax.set_title(title)
        ax.grid(axis="y", alpha=0.3)

    axes[0].set_ylabel("$VT$ / $VT$(TaylorF2Ecc bank)")
    axes[0].legend([plt.Line2D([], [], color=c, lw=3) for c in COLORS],
                   [f"IFAR = {i} yr" for i in IFARS], loc="center left",
                   fontsize=10.5, title="threshold", title_fontsize=11)
    axes[1].legend([plt.Line2D([], [], color="0.3", ls="none", marker=m, ms=7,
                               mfc="0.3" if f else "white", mec="0.3", mew=1.4)
                    for _, _, m, f, _ in INJECTIONS],
                   [label for _, label, _, _, _ in INJECTIONS], loc="lower right",
                   fontsize=10.5, title="injection set", title_fontsize=11,
                   labelspacing=0.8)
    fig.subplots_adjust(wspace=0.06)
    save(fig, "fig16_bank_comparison", bbox_inches="tight")


if __name__ == "__main__":
    main()
