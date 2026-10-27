"""Figure 4: 90% upper limits on the eccentric NSBH merger rate.

O4 limits use R90 = 2.303 / VT with VT from the fit in vt_fit.py. O3 limits
are from the distance reach of Dhurkunde et al. (data/o3_reach.csv) over 272
days; the e20 = 0.2 limit is scaled by the mean VT ratio of the TEOBResumS
and TaylorF2Ecc banks at e20 ~ 0.28 (data/bank_comparison.csv) to account for
the volume lost by the TaylorF2Ecc templates used in that search. The inset
shows VT beyond the template bank edge (e20 = 0.28) relative to VT inside it.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from style import DATA, save
from vt_fit import fit_vt

O3_YEARS = 272.0 / 365.25
O4_YEARS = 400.90 / 365.25
O4_COLOR, O3_COLOR = "#1b7837", "#525252"
MC_MIN, MC_MAX = 1.70, 4.50
R_MIN, R_MAX = 3.8, 720.0


def taylorf2ecc_gain():
    """Mean VT(TEOBResumS) / VT(TaylorF2Ecc) at e20 ~ 0.28."""
    table = np.genfromtxt(DATA / "bank_comparison.csv", delimiter=",",
                          names=True, dtype=None, encoding="utf-8")
    keep = (table["regime"] == "high_ecc") & (table["bank"] == "TEOBResumS")
    return table["ratio"][keep].mean()


def o3_limit(mc, mc_data, reach_mpc, factor=1.0):
    """Power-law interpolation of the O3 rate limit [Gpc^-3 yr^-1]."""
    vt = 4.0 / 3.0 * np.pi * (reach_mpc / 1e3) ** 3 * O3_YEARS
    slope, intercept = np.polyfit(np.log(mc_data), np.log(2.303 / vt / factor), 1)
    return np.exp(intercept + slope * np.log(mc))


def o4_limit(mc, q, vt_model):
    """O4 rate limit [Gpc^-3 yr^-1] at chirp mass mc and mass ratio q."""
    mtotal = mc * (q / (1 + q) ** 2) ** -0.6
    return 2.303e9 / vt_model(mc, mtotal)


def draw_inset(ax):
    e20, rel, err = np.loadtxt(DATA / "ecc_dropoff.csv", delimiter=",",
                               skiprows=1, unpack=True)
    e20 = np.maximum(e20, 0.28)  # reference point lies just inside the bank edge
    color = "#0072B2"
    ax.axvline(0.28, color=color, ls="--", lw=1.4, alpha=0.85)
    ax.axhline(1.0, color="#666666", ls=":", lw=0.9, alpha=0.5)
    ax.errorbar(e20, rel, yerr=err, fmt="-o", color=color, lw=1.8, ms=3.9,
                capsize=2.0)
    ax.set_xlim(0.276, 0.354)
    ax.set_ylim(0.04, 1.18)
    ax.set_xticks([0.28, 0.31, 0.35])
    ax.set_yticks([0.2, 0.6, 1.0])
    ax.set_xlabel(r"Eccentricity $e_{20}$", fontsize=8.6, labelpad=1.5)
    ax.set_ylabel(r"Rel. $\langle V\tau \rangle$", fontsize=8.6, labelpad=2.0)
    ax.tick_params(labelsize=7.8, pad=1.2)
    ax.grid(True, ls=":", alpha=0.35)


def main():
    vt_model = fit_vt()
    mc_o3, reach_e0, reach_e02 = np.loadtxt(DATA / "o3_reach.csv", delimiter=",",
                                            skiprows=1, unpack=True)
    mc = np.linspace(MC_MIN, MC_MAX, 300)
    o3_circular = o3_limit(mc, mc_o3, reach_e0)
    o3_eccentric = o3_limit(mc, mc_o3, reach_e02, 1 / taylorf2ecc_gain())

    fig, ax = plt.subplots(figsize=(5.1, 4.05))
    ax.grid(True, which="both", ls=":", alpha=0.5)
    ax.set_axisbelow(True)

    ax.fill_between(mc, o4_limit(mc, 4, vt_model), o3_circular, color=O4_COLOR,
                    alpha=0.14, zorder=2)
    ax.fill_between(mc, o3_eccentric, R_MAX, color="white", lw=0, zorder=3)
    ax.fill_between(mc, o3_circular, o3_eccentric, color="#d4d4d4", lw=0, zorder=4)
    ax.plot(mc, o3_eccentric, color=O3_COLOR, ls="-", lw=1.8, zorder=5)
    ax.plot(mc, o3_circular, color=O3_COLOR, ls="--", lw=1.6, zorder=5)

    styles = {2: ("-", 2.1), 4: ("--", 2.1), 8: (":", 2.3)}
    for q, (ls, lw) in styles.items():
        ax.plot(mc, o4_limit(mc, q, vt_model), color=O4_COLOR, ls=ls, lw=lw, zorder=6)

    ax.set_yscale("log")
    ax.set_xlim(MC_MIN, MC_MAX)
    ax.set_ylim(R_MIN, R_MAX)
    ax.set_xlabel(r"Chirp Mass $\mathcal{M}_c\ [M_\odot]$", fontsize=12.5)
    ax.set_ylabel(r"90% Rate Limit $\mathcal{R}_{90\%}\ "
                  r"[\mathrm{Gpc}^{-3}\,\mathrm{yr}^{-1}]$", fontsize=12.5)
    ax.tick_params(labelsize=11)

    # Distance reach R_eff with (4/3) pi R_eff^3 T = VT, using the O4 live time
    scale = 1e3 * (3 * 2.302585 / (4 * np.pi * O4_YEARS)) ** (1 / 3)
    reach = ax.secondary_yaxis("right", functions=(
        lambda r: scale / np.maximum(r, 1e-12) ** (1 / 3),
        lambda d: (scale / np.maximum(d, 1e-12)) ** 3))
    reach.set_ylabel(r"Distance Reach $R_{\mathrm{eff}}\ [\mathrm{Mpc}]$",
                     labelpad=8, fontsize=12)
    reach.set_yticks([120, 150, 200, 250, 300, 350, 450])
    reach.yaxis.set_major_formatter(ticker.ScalarFormatter())
    reach.yaxis.set_minor_formatter(ticker.NullFormatter())
    reach.tick_params(labelsize=10)

    handles = [Patch(facecolor="#d4d4d4", edgecolor=O3_COLOR, label="O3"),
               Patch(facecolor=O4_COLOR, alpha=0.22, label="O4 (Our results)")]
    handles += [Line2D([], [], color=O4_COLOR, ls=ls, lw=2.0, label=f"O4 ($q = {q}$)")
                for q, (ls, _) in styles.items()]
    ax.legend(handles=handles, loc="lower left", framealpha=0.94, fontsize=8.2,
              labelspacing=0.22, borderpad=0.28, handlelength=1.4).set_zorder(10)

    draw_inset(ax.inset_axes([0.52, 0.61, 0.445, 0.36], zorder=12))
    save(fig, "fig4_rate_limits", bbox_inches="tight", pad_inches=0.03)


if __name__ == "__main__":
    main()
