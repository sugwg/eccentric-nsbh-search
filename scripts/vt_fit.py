"""Fit of the O4 sensitive volume-time across the (m1, m2) plane.

data/o4_vt.csv lists the O4a + O4b sensitive volume-time of every injection
set. Each mass point was injected at several eccentricities e20 <= 0.28; the
VT of a mass point is the mean over these. The mass dependence is fit with

    ln VT = c0 + c1 ln Mc + c2 M

where Mc is the chirp mass and M the total mass.
"""
import numpy as np

from style import DATA


def mass_points():
    """Return m1, m2, Mc and VT [Mpc^3 yr] for each injected mass point."""
    table = np.genfromtxt(DATA / "o4_vt.csv", delimiter=",", names=True)
    keys = sorted(set(zip(table["m1"], table["m2"], table["mchirp"])),
                  key=lambda k: k[2])
    vt = [table["vt_total"][(table["m1"] == m1) & (table["m2"] == m2)].mean()
          for m1, m2, _ in keys]
    m1, m2, mc = np.array(keys).T
    return m1, m2, mc, np.array(vt)


def fit_vt():
    """Return a function VT(Mc, M) fit to the injected mass points."""
    m1, m2, mc, vt = mass_points()
    design = np.column_stack([np.ones_like(mc), np.log(mc), m1 + m2])
    c0, c1, c2 = np.linalg.lstsq(design, np.log(vt), rcond=None)[0]
    return lambda mchirp, mtotal: np.exp(c0 + c1 * np.log(mchirp) + c2 * mtotal)
