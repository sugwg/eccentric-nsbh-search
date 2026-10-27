"""Figure 3: O4 sensitive volume-time across the (m1, m2) plane.

Circles mark the injected mass points with their measured VT; the background
is the fit from vt_fit.py.
"""
import numpy as np
import matplotlib.pyplot as plt

from style import save
from vt_fit import fit_vt, mass_points

KNOWN_NSBH = [  # name, m1, m2, label colour
    ("GW230529", 3.6, 1.4, "white"),
    ("GW200115", 5.7, 1.5, "white"),
    ("GW200105", 8.9, 1.9, "black"),
]
MC_LABELS = [(3.52, r"$\mathcal{M}_c=2.5\,M_\odot$"), (5.19, r"$3.0\,M_\odot$"),
             (7.27, r"$3.5\,M_\odot$"), (9.83, r"$4.0\,M_\odot$"),
             (12.89, r"$4.5\,M_\odot$")]
Q_LABELS = [(3.6, 1.80), (5.2, 1.30), (8.5, 1.42), (11.0, 1.37)]
VMIN, VMAX = 35, 315


def main():
    m1, m2, _, vt = mass_points()
    vt = vt / 1e6
    vt_model = fit_vt()

    x, y = np.meshgrid(np.linspace(2.4, 16.0, 600), np.linspace(1.1, 2.36, 600))
    mchirp = (x * y) ** 0.6 / (x + y) ** 0.2

    fig, ax = plt.subplots(figsize=(9.8, 6.7))
    mesh = ax.pcolormesh(x, y, vt_model(mchirp, x + y) / 1e6, shading="gouraud",
                         cmap="viridis", vmin=VMIN, vmax=VMAX)

    q = ax.contour(x, y, x / y, levels=[2, 4, 6, 8, 10], colors="#222222",
                   linestyles="-.", linewidths=1.2, alpha=0.6)
    for text in ax.clabel(q, levels=[2, 4, 6, 8], manual=Q_LABELS,
                          inline_spacing=8, fontsize=12, fmt=r"$q=%d$"):
        text.set_color("white")
    ax.contour(x, y, mchirp, levels=[1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5],
               colors="#111111", linestyles="--", linewidths=1.4, alpha=0.85)
    for xpos, text in MC_LABELS:
        ax.text(xpos, 2.38, text, ha="center", va="bottom", fontsize=11.5,
                clip_on=False)

    ax.scatter(m1, m2, s=1550, c=vt, cmap="viridis", vmin=VMIN, vmax=VMAX,
               edgecolor="black", linewidth=2.0, zorder=5)
    for xi, yi, v in zip(m1, m2, vt):
        ax.text(xi, yi, rf"$\mathbf{{{v:.0f}}}$", ha="center", va="center",
                fontsize=12, color="white" if v < 150 else "black", zorder=6)

    for name, a, b, color in KNOWN_NSBH:
        ax.scatter(a, b, marker="*", s=240, color="#e63946", edgecolor="black",
                   linewidth=1.0, zorder=8)
        ax.text(a, b + 0.055, rf"$\mathbf{{{name}}}$", fontsize=10.5,
                color=color, ha="center", va="bottom", zorder=9)

    cbar = fig.colorbar(mesh, ax=ax, fraction=0.04, pad=0.025,
                        ticks=[50, 100, 150, 200, 250, 300])
    cbar.set_label(r"Sensitive Volume-Time $\langle V\tau \rangle\ "
                   r"[10^6\ \mathrm{Mpc}^3\,\mathrm{yr}]$", fontsize=18, labelpad=8)
    cbar.ax.tick_params(labelsize=15)

    ax.set_xlim(2.4, 15.9)
    ax.set_ylim(1.10, 2.36)
    ax.set_xlabel(r"Primary Mass $m_1\ [M_\odot]$", fontsize=20, labelpad=6)
    ax.set_ylabel(r"Secondary Mass $m_2\ [M_\odot]$", fontsize=20, labelpad=6)
    ax.tick_params(labelsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    save(fig, "fig3_sensitivity_map", bbox_inches="tight", pad_inches=0.04)


if __name__ == "__main__":
    main()
