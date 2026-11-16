"""Merger rate density at the parameters of GW200105_162426.

The O4 VT is taken from the fit in vt_fit.py. The O3 VT at these parameters
(0.0637 Gpc^3 yr) is from the sensitivity of the O3 eccentric search of
Dhurkunde et al.; this is the O3 + O4 combination used in the paper.

With no detections the 90% upper limit is R90 = 2.303 / VT. Treating
GW200105_162426 as one eccentric detection, the rate posterior (uniform prior)
is Gamma(2, VT); we quote its median, 68% equal-tailed interval and 90%
upper bound.
"""
import numpy as np

from vt_fit import fit_vt

MC, M1, M2 = 3.41, 8.9, 1.9
VT_O3 = 0.0637  # Gpc^3 yr


def gamma2_quantile(p):
    """Quantile of the Gamma(2, 1) distribution, by bisection."""
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 1.0 - np.exp(-mid) * (1.0 + mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    q = M1 / M2
    mtotal = MC * (q / (1 + q) ** 2) ** -0.6
    vt_o4 = fit_vt()(MC, mtotal) / 1e9  # Gpc^3 yr
    vt_cum = vt_o4 + VT_O3
    med, lo, hi, p90 = (gamma2_quantile(p) for p in (0.5, 0.16, 0.84, 0.9))
    print(f"VT (O4) = {vt_o4:.4f} Gpc^3 yr, VT (O3+O4) = {vt_cum:.4f} Gpc^3 yr")
    print(f"No detection (O4):   R90 <= {np.log(10) / vt_o4:.1f} Gpc^-3 yr^-1")
    print(f"One detection (O3+O4): R = {med / vt_cum:.1f} "
          f"+{(hi - med) / vt_cum:.1f} -{(med - lo) / vt_cum:.1f} Gpc^-3 yr^-1, "
          f"R90 <= {p90 / vt_cum:.1f} Gpc^-3 yr^-1")


if __name__ == "__main__":
    main()
