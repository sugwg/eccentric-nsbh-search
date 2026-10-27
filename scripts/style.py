"""Shared paths and matplotlib settings for all figures."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIGURES = ROOT / "figures"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["cmr10", "Computer Modern Serif", "DejaVu Serif"],
    "font.monospace": ["cmtt10", "Computer Modern Typewriter", "DejaVu Sans Mono"],
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,
    "axes.unicode_minus": False,
})


def save(fig, name, **kwargs):
    FIGURES.mkdir(exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(FIGURES / f"{name}.{ext}", dpi=300, **kwargs)
    plt.close(fig)
    print("wrote", FIGURES / name)
